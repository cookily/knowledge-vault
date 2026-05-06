#!/usr/bin/env python3
"""
compiled-manifest.py - 编译清单管理工具

用法：
    python compiled-manifest.py status          # 查看编译状态
    python compiled-manifest.py check          # 检查哪些文件需要编译
    python compiled-manifest.py add <raw> <summary>   # 标记已编译
    python compiled-manifest.py remove <raw>   # 标记未编译
    python compiled-manifest.py reset          # 清空清单（慎用）
"""

import json
import os
import hashlib
from pathlib import Path
from datetime import datetime, timezone

MANIFEST_PATH = Path("compiled-manifest.json")
MANIFEST_TEMPLATE = {
    "_comment": "知识库编译清单 - 由 compile-manifest.py 管理，请勿手动编辑",
    "_version": "1.0",
    "_description": "记录 raw/ 文件与 wiki/summaries/ 摘要的对应关系及文件 hash，用于增量编译",
    "entries": {}
}

def load_manifest():
    """加载清单文件，不存在则创建"""
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("⚠️  清单文件损坏，将重新创建")
    return MANIFEST_TEMPLATE.copy()

def save_manifest(manifest):
    """保存清单文件"""
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def file_hash(filepath: Path) -> str:
    """计算文件的 SHA256 hash"""
    if not filepath.exists():
        return ""
    sha = hashlib.sha256()
    sha.update(filepath.read_bytes())
    return sha.hexdigest()[:16]  # 只取前16位，够用

def scan_raw_files():
    """扫描 raw/ 目录下的所有 Markdown 文件"""
    raw_dir = Path.cwd() / "raw"
    if not raw_dir.exists():
        return {}

    files = {}
    cwd = Path.cwd()
    for f in raw_dir.rglob("*.md"):
        # 跳过说明文件
        if f.name in ["该文件夹存放外部资料（只进不改）.md", "该文件夹是自己整理的文件（可修改）.md"]:
            continue
        try:
            rel_path = str(f.relative_to(cwd))
        except ValueError:
            rel_path = str(f.resolve())
        files[rel_path] = {
            "path": rel_path,
            "hash": file_hash(f),
            "mtime": f.stat().st_mtime,
            "name": f.stem,
            "filename": f.name  # 保存原始文件名用于匹配
        }
    return files

def scan_summaries():
    """扫描 wiki/summaries/ 目录下的所有摘要文件，提取 source frontmatter"""
    summaries_dir = Path.cwd() / "wiki" / "summaries"
    if not summaries_dir.exists():
        return {}

    summaries = {}
    for f in summaries_dir.glob("*.md"):
        try:
            rel_path = str(f.relative_to(Path.cwd()))
        except ValueError:
            rel_path = str(f.resolve())
        content = f.read_text(encoding="utf-8", errors="replace")

        # 解析 frontmatter
        source = None
        for line in content.split("\n"):
            if line.startswith("source:"):
                source = line.split("source:", 1)[1].strip()
                # 去掉开头的 [[ 和 ]] 包裹
                if source.startswith("[["):
                    source = source.strip("[]").strip()
                break

        summaries[rel_path] = {
            "path": rel_path,
            "source": source,
            "title": extract_title(content),
            "filename": f.name
        }
    return summaries

def extract_title(content: str) -> str:
    """从 frontmatter 或正文提取标题"""
    for line in content.split("\n"):
        if line.startswith("title:"):
            return line.split("title:", 1)[1].strip().strip('"')
    # 第二个 # 开头的行
    for line in content.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""

def normalize_path(p: str) -> str:
    """标准化路径：统一斜杠、去除末尾斜杠"""
    return p.replace("\\", "/").rstrip("/")

def path_ends_with(text: str, keyword: str) -> bool:
    """检查路径/文件名是否包含关键词（忽略编码问题）"""
    try:
        return keyword.encode('gbk', errors='ignore').decode('gbk', errors='ignore') in text
    except:
        return keyword in text

def filename_fuzzy_match(raw_path: str, summary_source: str, summary_filename: str) -> bool:
    """
    判断摘要是否对应某个 raw 文件。
    匹配策略（保守，仅在 source 明确指向文件时才匹配）：
    1. source frontmatter 是 URL：提取 URL 关键词与 raw 文件名匹配（≥6 字符）
    2. source frontmatter 是文件路径（.md 或 raw/ 开头）：路径包含匹配
    3. source 是目录路径（如 raw/personal/openclaw/）：仅当文件名完全相同时匹配
    不使用模糊文件名匹配（避免误匹配）。
    """
    import os
    import re

    raw_name = os.path.basename(raw_path).replace('.md', '')
    summary_name = summary_filename.replace('.md', '')

    if summary_source:
        src = summary_source.strip()
        # 标准化路径分隔符
        src_norm = src.replace('/', os.sep)
        raw_norm = raw_path.replace('/', os.sep)

        # 情况1：source 是 URL → 从 URL 提取关键词匹配 raw 文件名
        if '://' in src:
            url_kw = src.rsplit('/', 1)[-1].replace('.md', '').lower()
            url_kw_clean = re.sub(r'[^\w一-鿿]', '', url_kw)
            raw_kw_clean = re.sub(r'[^\w一-鿿]', '', raw_name).lower()
            if len(url_kw_clean) >= 6 and url_kw_clean[:6] in raw_kw_clean:
                return True

        # 情况2：source 指向具体 raw 文件（以 .md 结尾）→ 路径或文件名匹配
        elif src.endswith('.md'):
            # 路径包含匹配 或 文件名匹配（忽略标点符号）
            if src_norm in raw_norm or raw_norm in src_norm:
                return True
            # 文件名模糊匹配（忽略标点/空格，至少10个字符相同）
            if raw_name and summary_name:
                raw_clean = re.sub(r'[^\w一-鿿]', '', raw_name).lower()
                sum_clean = re.sub(r'[^\w一-鿿]', '', summary_name).lower()
                # 取两个字符串的公共前缀长度
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

        # 情况3：source 是目录路径（如 raw/personal/openclaw/）→ 仅当文件名模糊相同时匹配
        elif src.endswith('/') or src.endswith(os.sep) or not src:
            if raw_name and summary_name:
                raw_clean = re.sub(r'[^\w一-鿿]', '', raw_name).lower()
                sum_clean = re.sub(r'[^\w一-鿿]', '', summary_name).lower()
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

    return False

def status():
    """显示编译状态"""
    manifest = load_manifest()
    raw_files = scan_raw_files()
    summaries = scan_summaries()

    # 构建 source → summary 映射（使用保守的模糊匹配）
    source_map = {}
    for r_path, r_info in raw_files.items():
        for s_path, s_info in summaries.items():
            if filename_fuzzy_match(r_path, s_info["source"], s_info["filename"]):
                source_map[r_path] = s_path
                break  # 每个 raw 文件只匹配一个摘要

    # 按 manifest entries 分类（manifest 是编译清单的事实来源）
    compiled_unchanged = []
    needs_update = []
    manifest_paths = set(manifest["entries"].keys())

    for r_path, r_info in raw_files.items():
        if r_path in manifest_paths:
            manifest_entry = manifest["entries"][r_path]
            if manifest_entry["hash"] == r_info["hash"]:
                compiled_unchanged.append(r_path)
            else:
                needs_update.append(r_path)

    # 按 source_map 分类（已有摘要但未加入清单）
    has_summary_untracked = []
    not_compiled = []

    for r_path, r_info in raw_files.items():
        if r_path not in manifest_paths:
            if r_path in source_map:
                # 只添加有效的摘要路径
                summary_path = source_map[r_path]
                has_summary_untracked.append((r_path, summary_path))
            else:
                not_compiled.append(r_path)

    print(f"\n=== Compile Status Report ===")
    print(f"   Compiled (unchanged): {len(compiled_unchanged)}")
    print(f"   Needs update (in manifest, hash changed): {len(needs_update)}")
    print(f"   Has summary (not in manifest): {len(has_summary_untracked)}")
    print(f"   Not compiled (no matching summary): {len(not_compiled)}")
    print(f"   Total raw files: {len(raw_files)}")
    print(f"   Total summary files: {len(summaries)}")

    if has_summary_untracked:
        print(f"\n[HAS SUMMARY - NOT IN MANIFEST] ({len(has_summary_untracked)} files):")
        for r, s in has_summary_untracked[:10]:
            print(f"   + {r}")
            print(f"     -> {s}")
        if len(has_summary_untracked) > 10:
            print(f"   ... and {len(has_summary_untracked) - 10} more")

    if not_compiled:
        print(f"\n[NOT COMPILED] ({len(not_compiled)} files):")
        for f in not_compiled[:10]:
            print(f"   - {f}")
        if len(not_compiled) > 10:
            print(f"   ... and {len(not_compiled) - 10} more")

    if needs_update:
        print(f"\n[NEEDS UPDATE] ({len(needs_update)} files):")
        for r_path in needs_update[:10]:
            print(f"   ~ {r_path}")

    return raw_files, source_map

def check():
    """检查需要编译的文件（用于自动化）"""
    manifest = load_manifest()
    raw_files = scan_raw_files()
    summaries = scan_summaries()

    # 构建 source → summary 映射
    source_map = {}
    for r_path, r_info in raw_files.items():
        for s_path, s_info in summaries.items():
            if filename_fuzzy_match(r_path, s_info["source"], s_info["filename"]):
                source_map[r_path] = s_path
                break

    to_compile = []
    to_update = []
    manifest_paths = set(manifest["entries"].keys())

    for r_path, r_info in raw_files.items():
        if r_path not in manifest_paths:
            if r_path not in source_map:
                to_compile.append(r_path)  # 真正未编译
            # else: 有摘要但未加入清单，不算待编译
        else:
            manifest_entry = manifest["entries"][r_path]
            if manifest_entry["hash"] != r_info["hash"]:
                to_update.append(r_path)  # 文件已修改，需重新编译

    return to_compile, to_update

def add(raw_path: str, summary_path: str):
    """标记文件已编译"""
    manifest = load_manifest()
    raw_files = scan_raw_files()

    # 尝试多种路径格式匹配
    matched_key = None
    for key in raw_files:
        if raw_path in key or key in raw_path:
            matched_key = key
            break

    if not matched_key:
        # 尝试用文件名匹配
        raw_name = Path(raw_path).name
        for key in raw_files:
            if raw_name in key or key.endswith(raw_name):
                matched_key = key
                break

    if not matched_key:
        print(f"[ERROR] File not found: {raw_path}")
        return

    manifest["entries"][matched_key] = {
        "summary": summary_path,
        "hash": raw_files[matched_key]["hash"],
        "compiled_at": datetime.now(timezone.utc).isoformat()
    }
    save_manifest(manifest)
    print(f"[OK] Marked: {matched_key} -> {summary_path}")

def remove(raw_path: str):
    """标记文件未编译（删除清单记录）"""
    manifest = load_manifest()
    if raw_path in manifest["entries"]:
        del manifest["entries"][raw_path]
        save_manifest(manifest)
        print(f"[OK] Removed: {raw_path}")
    else:
        print(f"[WARN] Not found in manifest: {raw_path}")

def reset():
    """清空清单（慎用）"""
    global MANIFEST_TEMPLATE
    save_manifest(MANIFEST_TEMPLATE.copy())
    print("[DONE] Manifest cleared")

def main():
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "status":
        status()
    elif cmd == "check":
        to_compile, to_update = check()
        print(f"\n[TO COMPILE]: {len(to_compile)}")
        print(f"[TO UPDATE]: {len(to_update)}")
        if to_compile:
            for f in to_compile:
                print(f"  + {f}")
        if to_update:
            for f in to_update:
                print(f"  ~ {f}")
    elif cmd == "add" and len(sys.argv) >= 4:
        add(sys.argv[2], sys.argv[3])
    elif cmd == "remove" and len(sys.argv) >= 3:
        remove(sys.argv[2])
    elif cmd == "reset":
        confirm = input("Confirm reset? Type 'yes': ")
        if confirm == "yes":
            reset()
        else:
            print("Cancelled")
    else:
        print(__doc__)

if __name__ == "__main__":
    main()