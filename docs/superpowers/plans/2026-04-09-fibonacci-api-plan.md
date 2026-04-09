# 斐波那契 Web API 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 实现一个基于 FastAPI 的 Web API，提供两个端点用于计算斐波那契数和序列。

**Architecture:** 采用分层架构：路由层 (routes) 处理 HTTP 请求，核心层 (core) 处理斐波那契计算逻辑。使用 Pydantic 模型定义请求/响应结构。

**Tech Stack:** FastAPI, Pydantic, pytest, httpx (测试客户端)

---

## 文件结构

| 文件 | 类型 | 说明 |
|------|------|------|
| `src/core/fibonacci.py` | Create | 斐波那契计算核心逻辑 |
| `src/api/responses.py` | Create | API 响应模型定义 |
| `src/api/routes.py` | Create | API 路由定义 |
| `src/main.py` | Create | FastAPI 应用入口 |
| `tests/test_api.py` | Create | API 端点测试 |
| `requirements.txt` | Create | 项目依赖 |

---

### Task 1: 项目依赖和核心逻辑

**Files:**
- Create: `requirements.txt`
- Create: `src/core/fibonacci.py`

- [ ] **Step 1: 创建 requirements.txt**

```txt
fastapi==0.109.0
uvicorn==0.27.0
pydantic==2.5.3
pytest==8.3.4
httpx==0.26.0
```

- [ ] **Step 2: 创建核心逻辑文件**

```python
# src/core/fibonacci.py
"""斐波那契数列计算核心模块。"""


def fibonacci(n: int) -> int:
    """
    计算第 n 个斐波那契数。

    Args:
        n: 斐波那契数列的索引 (n >= 0)

    Returns:
        第 n 个斐波那契数

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_sequence(count: int) -> list[int]:
    """
    生成前 count 项斐波那契序列。

    Args:
        count: 要生成的项数 (count >= 1)

    Returns:
        包含前 count 项斐波那契数的列表

    Examples:
        >>> fibonacci_sequence(1)
        [0]
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci_sequence(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    if count < 1:
        raise ValueError("count 必须是正整数")
    return [fibonacci(i) for i in range(count)]
```

- [ ] **Step 3: 创建核心逻辑的测试**

```python
# tests/test_core_fibonacci.py
"""斐波那契核心逻辑测试。"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from core.fibonacci import fibonacci, fibonacci_sequence


class TestFibonacci:
    """fibonacci() 函数测试。"""

    def test_fibonacci_zero(self):
        """测试 n=0 的情况。"""
        assert fibonacci(0) == 0

    def test_fibonacci_one(self):
        """测试 n=1 的情况。"""
        assert fibonacci(1) == 1

    def test_fibonacci_ten(self):
        """测试 n=10 的情况。"""
        assert fibonacci(10) == 55

    def test_fibonacci_negative(self):
        """测试负数输入应该抛出异常。"""
        with pytest.raises(ValueError, match="必须是非负整数"):
            fibonacci(-1)


class TestFibonacciSequence:
    """fibonacci_sequence() 函数测试。"""

    def test_sequence_one(self):
        """测试 count=1 的情况。"""
        assert fibonacci_sequence(1) == [0]

    def test_sequence_five(self):
        """测试 count=5 的情况。"""
        assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]

    def test_sequence_ten(self):
        """测试 count=10 的情况。"""
        assert fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_sequence_invalid_count(self):
        """测试 count=0 应该抛出异常。"""
        with pytest.raises(ValueError, match="必须是正整数"):
            fibonacci_sequence(0)
```

- [ ] **Step 4: 运行测试验证失败**

```bash
cd /Users/johnzs/test
pip install -r requirements.txt
pytest tests/test_core_fibonacci.py -v
```

预期：FAIL（因为模块路径还未正确设置）

- [ ] **Step 5: 创建 src/core/__init__.py**

```python
# src/core/__init__.py
"""核心斐波那契计算模块。"""
from .fibonacci import fibonacci, fibonacci_sequence

__all__ = ["fibonacci", "fibonacci_sequence"]
```

- [ ] **Step 6: 运行测试验证通过**

```bash
pytest tests/test_core_fibonacci.py -v
```

预期：8 个测试全部 PASS

- [ ] **Step 7: 提交**

```bash
git add requirements.txt src/core/ tests/test_core_fibonacci.py
git commit -m "feat: 添加斐波那契核心计算逻辑和测试"
```

---

### Task 2: API 响应模型

**Files:**
- Create: `src/api/__init__.py`
- Create: `src/api/responses.py`

- [ ] **Step 1: 创建 api 模块初始化文件**

```python
# src/api/__init__.py
"""API 模块。"""
```

- [ ] **Step 2: 创建响应模型**

```python
# src/api/responses.py
"""API 响应模型定义。"""
from pydantic import BaseModel


class FibonacciResponse(BaseModel):
    """单个斐波那契数的响应模型。"""
    n: int
    result: int


class FibonacciSequenceResponse(BaseModel):
    """斐波那契序列的响应模型。"""
    count: int
    sequence: list[int]


class ErrorResponse(BaseModel):
    """错误响应模型。"""
    detail: str
    error_code: str
```

- [ ] **Step 3: 创建响应模型的测试**

```python
# tests/test_responses.py
"""API 响应模型测试。"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from api.responses import FibonacciResponse, FibonacciSequenceResponse, ErrorResponse


class TestFibonacciResponse:
    """测试 FibonacciResponse 模型。"""

    def test_fibonacci_response_creation(self):
        """测试创建 FibonacciResponse 实例。"""
        response = FibonacciResponse(n=10, result=55)
        assert response.n == 10
        assert response.result == 55

    def test_fibonacci_response_dict(self):
        """测试 FibonacciResponse 转换为字典。"""
        response = FibonacciResponse(n=10, result=55)
        assert response.model_dump() == {"n": 10, "result": 55}


class TestFibonacciSequenceResponse:
    """测试 FibonacciSequenceResponse 模型。"""

    def test_sequence_response_creation(self):
        """测试创建 FibonacciSequenceResponse 实例。"""
        response = FibonacciSequenceResponse(count=5, sequence=[0, 1, 1, 2, 3])
        assert response.count == 5
        assert response.sequence == [0, 1, 1, 2, 3]


class TestErrorResponse:
    """测试 ErrorResponse 模型。"""

    def test_error_response_creation(self):
        """测试创建 ErrorResponse 实例。"""
        response = ErrorResponse(detail="参数无效", error_code="INVALID_PARAMETER")
        assert response.detail == "参数无效"
        assert response.error_code == "INVALID_PARAMETER"
```

- [ ] **Step 4: 运行测试验证通过**

```bash
pytest tests/test_responses.py -v
```

预期：4 个测试全部 PASS

- [ ] **Step 5: 提交**

```bash
git add src/api/ tests/test_responses.py
git commit -m "feat: 添加 API 响应模型和测试"
```

---

### Task 3: API 路由定义

**Files:**
- Create: `src/api/routes.py`

- [ ] **Step 1: 编写失败的测试**

```python
# tests/test_routes.py (部分测试)
"""API 路由测试。"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestFibonacciRoute:
    """测试 /fibonacci 端点。"""

    def test_fibonacci_valid_input(self):
        """测试有效的输入 n=10。"""
        from fastapi.testclient import TestClient
        from main import app
        client = TestClient(app)
        response = client.get("/fibonacci?n=10")
        assert response.status_code == 200
        assert response.json() == {"n": 10, "result": 55}

    def test_fibonacci_negative_input(self):
        """测试负数输入返回 400。"""
        from fastapi.testclient import TestClient
        from main import app
        client = TestClient(app)
        response = client.get("/fibonacci?n=-1")
        assert response.status_code == 400
```

- [ ] **Step 2: 运行测试验证失败**

```bash
pytest tests/test_routes.py::TestFibonacciRoute::test_fibonacci_valid_input -v
```

预期：FAIL（因为 main.py 还未创建）

- [ ] **Step 3: 创建路由文件**

```python
# src/api/routes.py
"""API 路由定义。"""
from fastapi import APIRouter, Query, HTTPException
from api.responses import FibonacciResponse, FibonacciSequenceResponse
from core.fibonacci import fibonacci, fibonacci_sequence


router = APIRouter()


@router.get("/fibonacci", response_model=FibonacciResponse)
def get_fibonacci(n: int = Query(..., description="斐波那契数列的索引 (n >= 0)")):
    """
    计算并返回第 n 个斐波那契数。

    Args:
        n: 斐波那契数列的索引，必须是非负整数

    Returns:
        包含 n 和结果的 JSON 响应

    Raises:
        HTTPException: 当 n 为负数时返回 400
    """
    if n < 0:
        raise HTTPException(
            status_code=400,
            detail="参数 n 必须是非负整数",
            headers={"X-Error-Code": "INVALID_PARAMETER"}
        )
    result = fibonacci(n)
    return FibonacciResponse(n=n, result=result)


@router.get("/fibonacci/sequence", response_model=FibonacciSequenceResponse)
def get_fibonacci_sequence(count: int = Query(..., description="要返回的项数 (count >= 1)")):
    """
    返回前 count 项斐波那契序列。

    Args:
        count: 要返回的项数，必须是正整数

    Returns:
        包含 count 和序列的 JSON 响应

    Raises:
        HTTPException: 当 count 小于 1 时返回 400
    """
    if count < 1:
        raise HTTPException(
            status_code=400,
            detail="参数 count 必须是正整数",
            headers={"X-Error-Code": "INVALID_PARAMETER"}
        )
    sequence = fibonacci_sequence(count)
    return FibonacciSequenceResponse(count=count, sequence=sequence)
```

- [ ] **Step 4: 提交**

```bash
git add src/api/routes.py
git commit -m "feat: 添加 API 路由定义"
```

---

### Task 4: FastAPI 应用入口

**Files:**
- Create: `src/main.py`
- Create: `src/__init__.py`

- [ ] **Step 1: 创建 src 模块初始化文件**

```python
# src/__init__.py
"""斐波那契 Web API 项目。"""
```

- [ ] **Step 2: 创建 FastAPI 应用入口**

```python
# src/main.py
"""斐波那契 Web API 主应用模块。"""
from fastapi import FastAPI
from api.routes import router as fibonacci_router
from api.responses import ErrorResponse


app = FastAPI(
    title="斐波那契 Web API",
    description="一个用于计算斐波那契数列的 Web API",
    version="1.0.0"
)

# 注册路由
app.include_router(fibonacci_router)


@app.get("/", tags=["root"])
def root():
    """根端点，返回 API 欢迎信息。"""
    return {"message": "欢迎使用斐波那契 Web API", "docs": "/docs"}


@app.get("/health", tags=["health"])
def health_check():
    """健康检查端点。"""
    return {"status": "healthy"}
```

- [ ] **Step 3: 更新测试文件以导入应用**

```python
# tests/test_routes.py (完整版)
"""API 路由测试。"""
import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import app


client = TestClient(app)


class TestFibonacciRoute:
    """测试 /fibonacci 端点。"""

    def test_fibonacci_zero(self):
        """测试 n=0 的情况。"""
        response = client.get("/fibonacci?n=0")
        assert response.status_code == 200
        assert response.json() == {"n": 0, "result": 0}

    def test_fibonacci_one(self):
        """测试 n=1 的情况。"""
        response = client.get("/fibonacci?n=1")
        assert response.status_code == 200
        assert response.json() == {"n": 1, "result": 1}

    def test_fibonacci_ten(self):
        """测试 n=10 的情况。"""
        response = client.get("/fibonacci?n=10")
        assert response.status_code == 200
        assert response.json() == {"n": 10, "result": 55}

    def test_fibonacci_negative(self):
        """测试负数输入返回 400。"""
        response = client.get("/fibonacci?n=-1")
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "非负整数" in data["detail"]

    def test_fibonacci_string_input(self):
        """测试字符串输入返回 422。"""
        response = client.get("/fibonacci?n=abc")
        assert response.status_code == 422


class TestFibonacciSequenceRoute:
    """测试 /fibonacci/sequence 端点。"""

    def test_sequence_one(self):
        """测试 count=1 的情况。"""
        response = client.get("/fibonacci/sequence?count=1")
        assert response.status_code == 200
        assert response.json() == {"count": 1, "sequence": [0]}

    def test_sequence_five(self):
        """测试 count=5 的情况。"""
        response = client.get("/fibonacci/sequence?count=5")
        assert response.status_code == 200
        assert response.json() == {"count": 5, "sequence": [0, 1, 1, 2, 3]}

    def test_sequence_ten(self):
        """测试 count=10 的情况。"""
        response = client.get("/fibonacci/sequence?count=10")
        assert response.status_code == 200
        assert response.json() == {"count": 10, "sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]}

    def test_sequence_zero(self):
        """测试 count=0 返回 400。"""
        response = client.get("/fibonacci/sequence?count=0")
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert "正整数" in data["detail"]

    def test_sequence_negative(self):
        """测试负数 count 返回 400。"""
        response = client.get("/fibonacci/sequence?count=-5")
        assert response.status_code == 400


class TestRootRoute:
    """测试根端点。"""

    def test_root(self):
        """测试根端点返回欢迎信息。"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "docs" in data

    def test_health(self):
        """测试健康检查端点。"""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
```

- [ ] **Step 4: 运行所有测试验证通过**

```bash
pytest tests/ -v
```

预期：20+ 个测试全部 PASS

- [ ] **Step 5: 提交**

```bash
git add src/main.py src/__init__.py tests/test_routes.py
git commit -m "feat: 创建 FastAPI 应用入口和完整路由测试"
```

---

### Task 5: 项目文档和验证

**Files:**
- Create: `README.md`

- [ ] **Step 1: 创建项目 README**

```markdown
# 斐波那契 Web API

一个用于计算斐波那契数列的 Web API，基于 FastAPI 构建。

## 功能特性

- 计算第 n 个斐波那契数
- 生成前 n 项斐波那契序列
- 自动生成的交互式 API 文档
- 完整的输入验证和错误处理

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## API 端点

### GET /fibonacci

计算第 n 个斐波那契数。

**请求参数:**
- `n` (query, int): 斐波那契数列的索引 (n >= 0)

**示例:**
```bash
curl "http://localhost:8000/fibonacci?n=10"
```

**响应:**
```json
{"n": 10, "result": 55}
```

### GET /fibonacci/sequence

返回前 count 项斐波那契序列。

**请求参数:**
- `count` (query, int): 要返回的项数 (count >= 1)

**示例:**
```bash
curl "http://localhost:8000/fibonacci/sequence?count=10"
```

**响应:**
```json
{"count": 10, "sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]}
```

## API 文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 运行测试

```bash
pytest tests/ -v
```

## 项目结构

```
.
├── src/
│   ├── main.py           # FastAPI 应用入口
│   ├── api/
│   │   ├── routes.py     # API 路由定义
│   │   └── responses.py  # 响应模型
│   └── core/
│       └── fibonacci.py  # 斐波那契计算逻辑
├── tests/
│   ├── test_core_fibonacci.py
│   ├── test_responses.py
│   └── test_routes.py
├── requirements.txt
└── README.md
```
```

- [ ] **Step 2: 运行完整测试套件**

```bash
pytest tests/ -v --tb=short
```

预期：所有测试 PASS

- [ ] **Step 3: 验证 API 文档可访问**

```bash
uvicorn src.main:app --port 8000 &
sleep 2
curl -s http://localhost:8000/docs | head -20
pkill -f "uvicorn src.main:app"
```

预期：返回 Swagger UI HTML 内容

- [ ] **Step 4: 提交**

```bash
git add README.md
git commit -m "docs: 添加项目 README 文档"
```

---

## 自我审查

### 1. 规格覆盖检查

| 规格要求 | 对应任务 | 状态 |
|----------|----------|------|
| GET /fibonacci 端点 | Task 3, Task 4 | ✅ |
| GET /fibonacci/sequence 端点 | Task 3, Task 4 | ✅ |
| 输入验证 (n >= 0, count >= 1) | Task 3 | ✅ |
| 结构化错误响应 | Task 2, Task 3 | ✅ |
| 核心计算逻辑 | Task 1 | ✅ |
| Pydantic 响应模型 | Task 2 | ✅ |
| 完整测试覆盖 | Task 1-4 | ✅ |
| README 文档 | Task 5 | ✅ |

### 2. 占位符扫描

- 无 TBD/TODO ✅
- 所有步骤包含实际代码 ✅
- 所有命令包含预期输出 ✅

### 3. 类型一致性检查

- `fibonacci(n: int) -> int` - 所有调用处一致 ✅
- `fibonacci_sequence(count: int) -> list[int]` - 所有调用处一致 ✅
- 响应模型名称一致 ✅

---

## 执行选项

**计划完成并保存到 `docs/superpowers/plans/2026-04-09-fibonacci-api-plan.md`。**

**两种执行选项：**

**1. 子代理驱动（推荐）** - 每个任务由独立子代理执行，任务间自动进行两轮审查（规格 + 代码质量）

**2. 内联执行** - 在当前会话中按任务顺序执行，批量执行带检查点

**选择哪种方式？**
