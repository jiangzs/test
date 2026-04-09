# 第三章：编写计划 (writing-plans)

## 何时使用
- 有规范或需求文档的多步骤任务
- 在触碰代码之前
- 需要为其他开发者（或代理）编写详细实现指南

## 输出位置
`docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`

## 计划文档结构

### 必需的头部
```markdown
# [功能名称] 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development

**Goal:** [一句话描述构建内容]
**Architecture:** [2-3 句关于方法的说明]
**Tech Stack:** [关键技术/库]
```

### 任务结构
```markdown
### Task N: [组件名称]

**Files:**
- Create: `path/to/file.py`
- Modify: `path/to/existing.py:123-145`
- Test: `tests/path/to/test.py`

- [ ] **Step 1: 编写失败测试**
- [ ] **Step 2: 运行测试验证失败**
- [ ] **Step 3: 编写最小实现**
- [ ] **Step 4: 运行测试验证通过**
- [ ] **Step 5: 提交**
```

## 禁止的占位符
- "TBD", "TODO", "implement later"
- "添加适当的错误处理"（无具体代码）
- "为上述内容编写测试"（无实际测试代码）
- "与任务 N 类似"（重复代码）

## 示例：斐波那契函数
```markdown
# 斐波那契函数实现计划

**Goal:** 实现计算斐波那契数列的函数

**Architecture:** 使用递归实现，添加记忆化优化性能

**Tech Stack:** Python, pytest

### Task 1: 基础实现

**Files:**
- Create: `src/fibonacci.py`
- Test: `tests/test_fibonacci.py`

- [ ] **Step 1: 编写失败测试**

```python
def test_fibonacci_first_ten():
    result = [fibonacci(i) for i in range(10)]
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

- [ ] **Step 2: 运行测试验证失败**

```bash
pytest tests/test_fibonacci.py::test_fibonacci_first_ten -v
# 预期：FAIL - fibonacci not defined
```

- [ ] **Step 3: 编写最小实现**

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
```

## 自我审查清单
- [ ] 所有文件路径具体明确
- [ ] 每个步骤包含实际代码
- [ ] 命令包含预期输出
- [ ] 没有占位符或 TODO

## 练习
1. 选择一个小型功能
2. 使用 writing-plans 技能创建完整实现计划
3. 使用自我审查清单验证计划
