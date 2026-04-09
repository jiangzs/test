# 第十章：Git Worktrees (using-git-worktrees)

## 何时使用
- 开始需要隔离的功能工作
- 执行实现计划之前
- 需要与主工作区隔离时

## 核心优势
- 隔离的实验环境
- 不影响主分支
- 可以轻松放弃或保留
- 多分支同时工作

## 使用流程

```
1. 调用 `Skill: superpowers:using-git-worktrees`
2. 自动创建工作树
3. 在隔离环境中工作
4. 完成后退出工作树
```

## 目录选择优先级

1. **检查现有目录**
   - `.worktrees/` (推荐，隐藏)
   - `worktrees/` (备选)

2. **检查 CLAUDE.md**
   - 如有指定，使用指定位置

3. **询问用户**
   - 项目本地：`.worktrees/`
   - 全局位置：`~/.config/superpowers/worktrees/`

## 安全验证

### 验证目录被忽略
```bash
# 检查工作树目录是否在.gitignore 中
git check-ignore -q .worktrees
```

### 如未被忽略
```bash
# 添加到.gitignore
echo ".worktrees/" >> .gitignore
git add .gitignore
git commit -m "chore: add .gitignore"
```

## 示例会话

### 创建功能工作树
```
开始新功能前：

1. 调用 using-git-worktrees
2. 自动创建 .claude/worktrees/feature-auth
3. 在新分支 feature-auth 上工作
4. 完成后使用 ExitWorktree
```

### 退出工作树
```
工作完成后：

1. 选择保持（keep）或删除（remove）
2. keep: 保留文件和分支
3. remove: 删除工作树和分支
```

## 常用命令

```bash
# 创建工作时
git worktree add .worktrees/feature -b feature-auth

# 列出工作树
git worktree list

# 删除工作树
git worktree remove .worktrees/feature
```

## 练习
1. 创建一个功能工作树
2. 进行一些实验性更改
3. 练习保持和移除工作树
