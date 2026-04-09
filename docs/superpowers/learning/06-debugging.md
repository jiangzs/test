# 第六章：系统调试 (systematic-debugging)

## 何时使用
- 遇到任何 bug 时
- 测试失败时
- 意外行为出现时
- 在提出修复方案之前

## 核心原则

1. **不要猜测** - 使用系统化方法
2. **不要暴力绕过** - 找到根本原因
3. **不要重复相同操作** - 期望不同结果
4. **必要时寻求帮助** - 向用户确认

## 使用流程

```
1. 调用 `Skill: superpowers:systematic-debugging`
2. 复现问题
3. 收集信息（日志、错误消息）
4. 提出假设
5. 验证假设
6. 找到根本原因
7. 实施修复
8. 验证修复
```

## 示例场景

### 场景 1: 测试失败
```
失败信息：
AssertionError: expected 5, got 4

错误做法：
- 反复运行测试期望通过
- 直接修改代码尝试"修复"

正确做法：
1. 调用 systematic-debugging
2. 检查测试输入和预期
3. 检查函数实现
4. 添加调试输出
5. 找到差异原因
```

### 场景 2: API 调用失败
```
错误：ConnectionError: Timeout

错误做法：
- 重试相同调用
- 增加超时时间

正确做法：
1. 调用 systematic-debugging
2. 检查网络连接
3. 检查 API 端点
4. 检查认证
5. 逐步排查
```

## 调试工具

### Python
```bash
# 添加调试输出
import pdb; pdb.set_trace()

# 运行单测试
pytest tests/test_file.py::test_name -v -s
```

### JavaScript
```bash
# 使用 node 调试
node --inspect app.js

# 添加 console.log
console.log('debug:', value)
```

## 常见误区

| 错误做法 | 正确做法 |
|----------|----------|
| 反复重试 | 分析原因 |
| 盲目修改 | 验证假设 |
| 忽略错误 | 调查错误 |
| 一次改多处 | 一次改一处 |

## 练习
1. 故意在一个函数中引入 bug
2. 使用 debugging 技能定位问题
3. 记录调试过程
