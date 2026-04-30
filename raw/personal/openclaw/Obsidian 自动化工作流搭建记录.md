# Obsidian 自动化工作流搭建记录

## 项目说明

使用 Node.js + `obsidian-cli` + Git 实现 AI 自动创建笔记，并自动同步到 Gitee 远程仓库。

## 目录结构

- **Obsidian Vault 根目录：** `F:\Obsidian_workspace\`
- **AI 创建笔记默认目录：** `F:\Obsidian_workspace\openclaw-note\`
- **自动化脚本：** `C:\Users\chenyl\.openclaw\workspace\obsidian-automation\`

## 已完成配置

- ✅ obsidian-cli 已安装 (`obsidian --version` 验证可用)
- ✅ 自动化脚本创建完成
- ✅ 配置文件已设置：
  - `vaultPath`: `F:/Obsidian_workspace`
  - `defaultFolder`: `openclaw-note`
- ✅ Git 初始化完成
- ✅ Gitee 远程已添加：`https://gitee.com/chenyl_obsidian/openclaw-note.git`
- ✅ 第一个提交已完成

## 使用方法

### 创建新笔记

```bash
cd C:\Users\chenyl\.openclaw\workspace\obsidian-automation
node obsidian.js create "笔记标题" "笔记内容" [可选文件夹]
```

### 同步所有变更到 Gitee

```bash
cd F:\Obsidian_workspace\openclaw-note
node C:\Users\chenyl\.openclaw\workspace\obsidian-automation\git-sync.js
```

## 遇到的问题及解决

### 问题 1：推送错误 `error: src refspec master does not match any`

**原因：** 本地分支名是 `main`，推送时用了 `master`。

**解决：** 使用 `git push -u origin main` 而不是 `master`。

### 问题 2：`LF will be replaced by CRLF` 警告

**原因：** Git 换行符自动转换警告，正常现象，不影响使用。

**解决：** 无需处理，Git 会自动处理。

### 问题 3：`fatal: unknown write failure on standard output`

**原因：** 可能是 PowerShell 输出缓冲区问题，**不影响提交**，提交实际上已经成功。

**解决：** 下次直接同步即可，如果提示"没有变更"说明已经提交成功。

## 优点

- 所有笔记仍在本地 Obsidian 中正常编辑
- AI 可以帮你快速创建笔记骨架
- 自动备份到 Gitee 远程仓库
- 保留完整的 Git 版本历史
