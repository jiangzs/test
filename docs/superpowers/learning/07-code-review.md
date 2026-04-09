# 第七章：代码审查 (requesting/receiving-code-review)

## 两个技能

### requesting-code-review
- 完成任务时使用
- 实现主要功能后
- 合并到主分支前

### receiving-code-review
- 收到审查反馈时使用
- 实现建议之前
- 反馈不清晰或技术有问题时

## requesting-code-review 使用流程

```
1. 确保工作完成
2. 所有测试通过
3. 调用 `Skill: superpowers:requesting-code-review`
4. 提供审查模板
```

### 审查模板
```markdown
## 审查清单

### 功能正确性
- [ ] 实现符合需求
- [ ] 边界情况处理
- [ ] 错误处理完善

### 代码质量
- [ ] 代码清晰可读
- [ ] 命名有意义
- [ ] 无重复代码

### 测试
- [ ] 测试覆盖主要路径
- [ ] 测试覆盖边界情况
- [ ] 所有测试通过
```

## receiving-code-review 使用流程

```
1. 收到审查反馈
2. 调用 `Skill: superpowers:receiving-code-review`
3. 技术严谨验证
4. 不盲目实现
```

### 处理模糊反馈
```
审查者："这个函数需要更好的错误处理"

错误做法：
- 立即添加 try/catch

正确做法：
1. 调用 receiving-code-review
2. 分析具体问题
3. 询问澄清（如需要）
4. 针对性修复
```

## 示例场景

### 场景 1: 请求审查
```
功能完成后：

你：我将使用 requesting-code-review 请求审查。

[调用 Skill: superpowers:requesting-code-review]

审查请求已创建，等待反馈。
```

### 场景 2: 接收审查
```
收到反馈后：

审查者："建议提取这个逻辑为独立函数"

你：我将使用 receiving-code-review 分析这个建议。

[调用 Skill: superpowers:receiving-code-review]

分析结果：
- 建议合理：逻辑确实可以独立
- 重构后提高可读性
- 实现这个建议
```

## 最佳实践

### 请求审查时
- 提供清晰的变更说明
- 标注高风险变更
- 主动寻求特定反馈

### 接收审查时
- 不防御性回应
- 寻求技术严谨性
- 验证每个建议

## 练习
1. 完成一个小功能
2. 使用 requesting-code-review 请求审查
3. 根据反馈使用 receiving-code-review 处理
