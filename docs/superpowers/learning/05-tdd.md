# 第五章：测试驱动开发 (test-driven-development)

## 何时使用
- 实现任何功能之前
- 修复任何 bug 之前
- 在编写实现代码之前

## TDD 循环

```
1. 编写失败测试 → 2. 运行验证失败 → 3. 编写最小实现 → 4. 运行验证通过 → 5. 重构（可选）→ 重复
```

## 使用流程

1. 调用 `Skill: superpowers:test-driven-development`
2. 遵循技能指导编写测试
3. 实现最少的代码让测试通过
4. 提交

## 完整示例：斐波那契函数

### 第一轮：第一个测试
```python
# Step 1: 编写失败测试
def test_fibonacci_zero():
    assert fibonacci(0) == 0

# Step 2: 运行验证失败
# pytest tests/test_fibonacci.py -v
# ERROR: NameError: name 'fibonacci' is not defined

# Step 3: 编写最小实现
def fibonacci(n):
    return 0

# Step 4: 运行验证通过
# pytest tests/test_fibonacci.py -v
# 1 passed
```

### 第二轮：更多测试
```python
# Step 1: 添加新测试
def test_fibonacci_one():
    assert fibonacci(1) == 1

# Step 2: 运行验证失败
# FAILED: fibonacci(1) returned 0, expected 1

# Step 3: 更新实现
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Step 4: 运行验证通过
# 2 passed
```

### 第三轮：完整测试
```python
def test_fibonacci_first_ten():
    result = [fibonacci(i) for i in range(10)]
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 提交历史示例
```
abc123 - test: 添加 fibonacci(0) 测试
def456 - feat: 实现 fibonacci(0) 返回 0
ghi789 - test: 添加 fibonacci(1) 测试
jkl012 - feat: 实现 fibonacci(1) 返回 1
mno345 - test: 添加前十项测试
pqr678 - feat: 实现完整斐波那契逻辑
```

## 最佳实践

### 好的测试
- 测试具体行为
- 一次测试一个概念
- 使用描述性名称
- 包含预期值

### 避免的陷阱
- 不要一次写多个测试
- 不要跳过失败验证
- 不要实现多余功能
- 不要忘记提交

## 练习
1. 选择一个简单函数（如计算器）
2. 使用 TDD 技能实现
3. 确保每个功能都有对应测试
