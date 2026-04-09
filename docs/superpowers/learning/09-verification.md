# 第九章：验证完成 (verification-before-completion)

## 何时使用
- 即将声明工作完成时
- 声称问题已修复时
- 提交或创建 PR 之前
- 合并到主分支之前

## 核心原则
> 证据先于断言

## 使用流程

```
1. 调用 `Skill: superpowers:verification-before-completion`
2. 运行验证命令
3. 确认输出
4. 然后才能声明成功
```

## 验证检查单

### 代码验证
- [ ] 所有测试通过
- [ ] 没有 lint 错误
- [ ] 构建成功
- [ ] 类型检查通过

### 功能验证
- [ ] 需求全部实现
- [ ] 边界情况处理
- [ ] 错误处理完善

### 文档验证
- [ ] 代码注释完整
- [ ] README 已更新
- [ ] 变更记录清晰

### Git 验证
- [ ] 提交信息清晰
- [ ] 没有临时文件
- [ ] 分支最新状态

## 示例命令

### Python 项目
```bash
# 运行测试
pytest tests/ -v

# 运行 lint
flake8 src/

# 类型检查
mypy src/

# 构建
python -m build
```

### Node.js 项目
```bash
# 运行测试
npm test

# 运行 lint
npm run lint

# 类型检查
npm run typecheck

# 构建
npm run build
```

### Git 验证
```bash
# 检查状态
git status

# 查看变更
git diff main

# 提交历史
git log --oneline -5
```

## 完整示例

### 验证会话
```
你：我将使用 verification-before-completion 验证工作。

[调用 Skill: superpowers:verification-before-completion]

验证步骤：
1. 运行测试... ✅ 47 passed
2. 运行 lint... ✅ No issues
3. 构建项目... ✅ Success
4. 检查 git 状态... ✅ Clean

所有验证通过，工作可以提交。
```

## 如果验证失败

```
验证失败处理流程：
1. 记录失败内容
2. 调用 systematic-debugging
3. 修复问题
4. 重新运行验证
5. 全部通过前不声明完成
```

## 练习
1. 完成一个小功能
2. 使用 verification 技能验证
3. 记录验证结果
