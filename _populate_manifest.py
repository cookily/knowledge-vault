#!/usr/bin/env python3
"""
_populate_manifest.py - 增量更新编译清单

用法：
    python _populate_manifest.py          # 增量更新（不破坏已有条目）
    python _populate_manifest.py --reset   # 完全重写（慎用）

增量模式：
- 读取已有清单，不清空
- 对已在清单中的文件，更新 hash 和 compiled_at
- 对不在清单中的文件，用模糊匹配找对应 summary，找到则追加
- 已有的条目顺序和内容不变
"""

import json
import re
import hashlib
import os
from pathlib import Path
from datetime import datetime, timezone

MANIFEST_PATH = Path("compiled-manifest.json")


def load_manifest():
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("[WARN] Manifest corrupted, will rebuild")
    return {"_comment": "compiled manifest", "_version": "1.0", "entries": {}}


def save_manifest(manifest):
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def scan_raw_files():
    """扫描 raw/ 目录，返回 {相对路径: hash}"""
    raw_dir = Path.cwd() / "raw"
    if not raw_dir.exists():
        return {}
    cwd = Path.cwd()
    files = {}
    for f in raw_dir.rglob("*.md"):
        if f.name in ["该文件夹存放外部资料（只进不改）.md", "该文件夹是自己整理的文件（可修改）.md"]:
            continue
        try:
            rel = str(f.relative_to(cwd))
        except ValueError:
            rel = str(f.resolve())
        files[rel] = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
    return files


def scan_summaries():
    """扫描 wiki/summaries/，返回 {filename: source}"""
    summaries_dir = Path.cwd() / "wiki" / "summaries"
    if not summaries_dir.exists():
        return {}
    summaries = {}
    for f in summaries_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8", errors="replace")
        source = None
        for line in content.split("\n"):
            if line.startswith("source:"):
                src = line.split("source:", 1)[1].strip()
                if src.startswith("[["):
                    src = src.strip("[]").strip()
                source = src
                break
        summaries[f.name] = source
    return summaries


def filename_fuzzy_match(raw_path: str, summary_source: str, summary_filename: str) -> bool:
    """
    与 compiled-manifest.py 保持一致的匹配逻辑。
    """
    raw_name = os.path.basename(raw_path).replace(".md", "")
    summary_name = summary_filename.replace(".md", "")

    if summary_source:
        src = summary_source.strip()
        src_norm = src.replace("/", os.sep)
        raw_norm = raw_path.replace("/", os.sep)

        # 情况1：source 是 URL → 从 URL 提取关键词匹配
        if "://" in src:
            url_kw = src.rsplit("/", 1)[-1].replace(".md", "").lower()
            url_kw_clean = re.sub(r"[^\w一-鿿]", "", url_kw)
            raw_kw_clean = re.sub(r"[^\w一-鿿]", "", raw_name).lower()
            if len(url_kw_clean) >= 6 and url_kw_clean[:6] in raw_kw_clean:
                return True

        # 情况2：source 指向具体文件（.md 结尾）→ 路径或文件名匹配
        elif src.endswith(".md"):
            if src_norm in raw_norm or raw_norm in src_norm:
                return True
            if raw_name == summary_name:
                return True
            raw_clean = re.sub(r"[^\w一-鿿]", "", raw_name).lower()
            sum_clean = re.sub(r"[^\w一-鿿]", "", summary_name).lower()
            min_len = min(len(raw_clean), len(sum_clean))
            if min_len >= 10:
                prefix_len = 0
                for i in range(min_len):
                    if raw_clean[i] == sum_clean[i]:
                        prefix_len = i + 1
                    else:
                        break
                if prefix_len >= 10:
                    return True

        # 情况3：source 是目录路径（如 raw/personal/openclaw/）→ 仅当文件名完全相同时匹配
        elif src.endswith("/") or src.endswith(os.sep) or not src:
            if raw_name == summary_name:
                return True

    return False


def incremental_update():
    """增量更新：更新已有条目，新增匹配的条目"""
    manifest = load_manifest()
    raw_files = scan_raw_files()
    summaries = scan_summaries()

    updated = 0
    added = 0
    skipped = 0
    now = datetime.now(timezone.utc).isoformat()

    # 已有条目顺序
    original_order = list(manifest["entries"].keys())

    # 更新已有条目
    for raw_path, new_hash in raw_files.items():
        if raw_path in manifest["entries"]:
            manifest["entries"][raw_path]["hash"] = new_hash
            manifest["entries"][raw_path]["compiled_at"] = now
            updated += 1

    # 新增未收录的文件
    new_entries = {}
    for raw_path, raw_hash in raw_files.items():
        if raw_path in manifest["entries"]:
            continue  # 已在清单中

        # 用模糊匹配找对应 summary
        matched_summary = None
        for sum_filename, sum_source in summaries.items():
            if filename_fuzzy_match(raw_path, sum_source, sum_filename):
                matched_summary = f"wiki/summaries/{sum_filename}"
                break

        if matched_summary:
            new_entries[raw_path] = {
                "summary": matched_summary,
                "hash": raw_hash,
                "compiled_at": now
            }
            added += 1
        else:
            skipped += 1

    # 将新条目追加到原清单后面
    for raw_path, entry in new_entries.items():
        manifest["entries"][raw_path] = entry

    save_manifest(manifest)

    print(f"[OK] Incremental update done")
    print(f"  Updated: {updated}")
    print(f"  Added: {added} (matched summary)")
    print(f"  Skipped: {skipped} (no matching summary)")
    print(f"  Total: {len(manifest['entries'])} entries")


def full_rebuild():
    """完全重写：清空清单，重新匹配所有文件"""
    manifest = load_manifest()
    raw_files = scan_raw_files()
    summaries = scan_summaries()

    now = datetime.now(timezone.utc).isoformat()
    entries = {}
    matched = 0
    skipped = 0

    for raw_path, raw_hash in raw_files.items():
        matched_summary = None
        for sum_filename, sum_source in summaries.items():
            if filename_fuzzy_match(raw_path, sum_source, sum_filename):
                matched_summary = f"wiki/summaries/{sum_filename}"
                break

        if matched_summary:
            entries[raw_path] = {
                "summary": matched_summary,
                "hash": raw_hash,
                "compiled_at": now
            }
            matched += 1
        else:
            skipped += 1

    manifest["entries"] = entries
    save_manifest(manifest)

    print(f"[RESET] Full rebuild done")
    print(f"  Matched: {matched}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {len(entries)} entries")


def main():
    import sys
    if "--reset" in sys.argv:
        confirm = input("完全重写将清空清单，确认？输入 'yes': ")
        if confirm == "yes":
            full_rebuild()
        else:
            print("已取消")
    else:
        incremental_update()


if __name__ == "__main__":
    main()
