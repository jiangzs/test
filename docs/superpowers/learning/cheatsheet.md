# Superpowers 技能速查表

## 快速决策树

```
开始任务
    ↓
是创意工作吗？→ brainstorming
    ↓
需要计划吗？→ writing-plans
    ↓
开始实现 → using-git-worktrees
    ↓
写代码前？→ test-driven-development
    ↓
遇到 Bug？→ systematic-debugging
    ↓
需要并行？→ dispatching-parallel-agents
    ↓
即将完成？→ verification-before-completion
    ↓
请求审查？→ requesting-code-review
```

## 技能触发条件

| 场景 | 技能 |
|------|------|
| 构建新功能 | brainstorming → writing-plans |
| 修复 Bug | debugging → TDD |
| 完成任务 | verification → code-review |
| 多任务 | dispatching-parallel-agents |
| 写代码前 | TDD |
| 测试失败 | debugging |
| 合并前 | verification → code-review |

## 核心技能列表

| 技能 | 用途 | 调用时机 |
|------|------|----------|
| brainstorming | 探索需求和设计 | 创意工作前 |
| writing-plans | 创建实现计划 | 触碰代码前 |
| executing-plans | 执行书面计划 | 有计划后 |
| TDD | 测试驱动开发 | 写实现代码前 |
| debugging | 系统化调试 | 遇到 Bug 时 |
| verification | 验证完成 | 声明完成前 |
| code-review | 代码审查 | 合并/提交前 |
| worktrees | 隔离工作环境 | 开始新功能前 |

## 核心规则 reminder

1. **1% 规则** - 可能适用就调用
2. **用户指令优先** - 用户指令 > 技能规则 > 默认行为
3. **不要跳过技能** - 即使看起来简单
4. **证据先于断言** - 验证后再声明完成

## 常用命令

```bash
# 调用技能
Skill: superpowers:<skill-name>

# 创建任务列表
TaskCreate

# 更新任务状态
TaskUpdate: status=in_progress/completed
```

## 文件位置约定
- 计划：`docs/superpowers/plans/YYYY-MM-DD-<feature>.md`
- 课程：`docs/superpowers/learning/`
- 速查表：`docs/superpowers/learning/cheatsheet.md`
