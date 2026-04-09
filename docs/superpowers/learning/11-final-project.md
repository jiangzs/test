# 第十一章：综合实践项目

## 项目目标
使用所有学到的技能完成一个完整的功能开发

## 项目：待办事项 API

### 功能需求
1. 创建待办事项
2. 读取待办事项列表
3. 更新待办事项状态
4. 删除待办事项
5. 输入验证
6. 错误处理

### 技术栈
- Python 3.8+
- Flask (API 框架)
- pytest (测试)

## 使用技能流程

```
1. brainstorming - 探索需求和设计
2. writing-plans - 创建详细实现计划
3. using-git-worktrees - 创建隔离环境
4. test-driven-development - 为每个功能编写测试
5. executing-plans/subagent-driven-development - 执行计划
6. systematic-debugging - 修复任何问题
7. verification-before-completion - 验证完成
8. requesting-code-review - 请求最终审查
```

## 项目结构

```
todo-api/
├── src/
│   ├── app.py
│   ├── models.py
│   └── routes.py
├── tests/
│   ├── test_routes.py
│   └── test_models.py
├── requirements.txt
└── README.md
```

## 任务分解

### Task 1: 项目设置
- 创建目录结构
- 安装依赖
- 配置测试环境

### Task 2: 数据模型
- 实现 Todo 类
- 添加验证逻辑

### Task 3: 创建 API
- POST /todos
- GET /todos
- PUT /todos/<id>
- DELETE /todos/<id>

### Task 4: 错误处理
- 输入验证
- 404 处理
- 500 处理

## 提交检查单

- [ ] 所有测试通过
- [ ] 代码通过审查
- [ ] 文档完整
- [ ] 可以合并到主分支

## 练习
完整实现待办事项 API，遵循上述技能流程
