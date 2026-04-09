# 斐波那契 CLI 工具实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 实现一个基于 Typer 的命令行工具，提供基础计算、序列显示和交互模式三个功能。

**Architecture:** 采用模块化设计：CLI 入口 (main.py) 定义应用，命令模块 (commands.py) 处理各子命令，交互模块 (interactive.py) 处理交互模式，核心逻辑复用现有 fibonacci.py。

**Tech Stack:** Typer, Rich, pytest, Python 3.8+

---

## 文件结构

| 文件 | 类型 | 说明 |
|------|------|------|
| `requirements-cli.txt` | Create | CLI 工具依赖 |
| `src/cli/__init__.py` | Create | CLI 模块初始化 |
| `src/cli/main.py` | Create | Typer 主入口 |
| `src/cli/commands.py` | Create | 命令定义 |
| `src/cli/interactive.py` | Create | 交互模式逻辑 |
| `src/cli/formatters.py` | Create | 输出格式化 |
| `tests/test_cli.py` | Create | CLI 命令测试 |
| `tests/test_interactive.py` | Create | 交互模式测试 |

---

### Task 1: 项目依赖和模块结构

**Files:**
- Create: `requirements-cli.txt`
- Create: `src/cli/__init__.py`

- [ ] **Step 1: 创建 CLI 依赖文件**

```txt
# requirements-cli.txt
# 斐波那契 CLI 工具依赖
typer==0.9.0
rich==13.7.0
# 开发和测试
pytest==8.3.4
pytest-cov==4.1.0
```

- [ ] **Step 2: 创建 CLI 模块初始化文件**

```python
# src/cli/__init__.py
"""斐波那契 CLI 工具模块。"""

__version__ = "1.0.0"
__description__ = "斐波那契计算器 - 教学演示工具"
```

- [ ] **Step 3: 安装依赖并验证模块可导入**

```bash
pip install -r requirements-cli.txt
python -c "import sys; sys.path.insert(0, 'src'); from cli import __version__; print(__version__)"
```

预期输出：`1.0.0`

- [ ] **Step 4: 提交**

```bash
git add requirements-cli.txt src/cli/__init__.py
git commit -m "feat: 添加 CLI 模块结构和依赖"
```

---

### Task 2: 输出格式化模块

**Files:**
- Create: `src/cli/formatters.py`
- Test: `tests/test_formatters.py`

- [ ] **Step 1: 编写失败的测试**

```python
# tests/test_formatters.py
"""输出格式化器测试。"""
import pytest
import sys
sys.path.insert(0, 'src')


class TestResultBoxFormatter:
    """测试结果框格式化。"""

    def test_single_result(self):
        """测试单个结果的格式化输出。"""
        from cli.formatters import format_result_box
        output = format_result_box(10, 55)
        assert "55" in output
        assert "10" in output

    def test_result_box_contains_emoji(self):
        """测试结果框包含计算图标。"""
        from cli.formatters import format_result_box
        output = format_result_box(5, 5)
        assert "📊" in output or "╔" in output


class TestSequenceTableFormatter:
    """测试序列表格格式化。"""

    def test_sequence_table(self):
        """测试序列表格输出。"""
        from cli.formatters import format_sequence_table
        output = format_sequence_table([0, 1, 1, 2, 3])
        assert "0" in output
        assert "3" in output
```

- [ ] **Step 2: 运行测试验证失败**

```bash
pytest tests/test_formatters.py -v
```

预期：FAIL（模块不存在）

- [ ] **Step 3: 编写最小实现**

```python
# src/cli/formatters.py
"""CLI 输出格式化模块。"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box


def format_result_box(n: int, result: int) -> str:
    """
    格式化单个斐波那契数的结果输出。

    Args:
        n: 斐波那契数列的索引
        result: 计算结果

    Returns:
        格式化的字符串输出
    """
    console = Console()

    content = f"[bold]索引 (n):[/bold]     {n}\n[bold]结果：[/bold]        {result}"
    panel = Panel(
        content,
        title="📊 斐波那契计算结果",
        box=box.DOUBLE_EDGE,
        border_style="blue"
    )

    # 捕获输出为字符串
    from io import StringIO
    output = StringIO()
    console.file = output
    console.print(panel)
    return output.getvalue()


def format_sequence_table(sequence: list[int]) -> str:
    """
    格式化斐波那契序列的表格输出。

    Args:
        sequence: 斐波那契数列列表

    Returns:
        格式化的表格字符串
    """
    console = Console()

    table = Table(
        title=f"📋 斐波那契序列 (前{len(sequence)}项)",
        box=box.DOUBLE_EDGE,
        border_style="green"
    )

    table.add_column("索引", justify="center", style="cyan")
    table.add_column("值", style="yellow")

    for i, value in enumerate(sequence):
        table.add_row(str(i), str(value))

    from io import StringIO
    output = StringIO()
    console.file = output
    console.print(table)
    return output.getvalue()


def format_error_message(message: str, hint: str = None) -> str:
    """
    格式化错误消息输出。

    Args:
        message: 错误消息
        hint: 可选的提示消息

    Returns:
        格式化的错误字符串
    """
    console = Console()

    from io import StringIO
    output = StringIO()
    console.file = output

    console.print(f"❌ 错误：{message}", style="red bold")
    if hint:
        console.print(f"💡 提示：{hint}", style="yellow")

    return output.getvalue()


def format_guide_intro() -> str:
    """
    格式化新手引导的欢迎消息。

    Returns:
        格式化的欢迎字符串
    """
    console = Console()

    content = """[bold blue]👋 欢迎来到斐波那契计算器！[/bold blue]

这是一个交互式学习工具，帮助你理解斐波那契数列。

[bold]斐波那契数列是：[/bold] 0, 1, 1, 2, 3, 5, 8, 13...
每个数字是前两个数字的和。"""

    panel = Panel(
        content,
        title="🎓 新手引导",
        border_style="cyan"
    )

    from io import StringIO
    output = StringIO()
    console.file = output
    console.print(panel)
    return output.getvalue()
```

- [ ] **Step 4: 运行测试验证通过**

```bash
pytest tests/test_formatters.py -v
```

预期：4 个测试全部 PASS

- [ ] **Step 5: 提交**

```bash
git add src/cli/formatters.py tests/test_formatters.py
git commit -m "feat: 添加 CLI 输出格式化器和测试"
```

---

### Task 3: CLI 主入口和命令定义

**Files:**
- Create: `src/cli/main.py`
- Create: `src/cli/commands.py`
- Test: `tests/test_cli.py` (部分)

- [ ] **Step 1: 编写失败的测试**

```python
# tests/test_cli.py (第一部分)
"""CLI 命令测试。"""
import pytest
from typer.testing import CliRunner
import sys
sys.path.insert(0, 'src')


@pytest.fixture
def runner():
    """创建测试运行器。"""
    from cli.main import app
    return CliRunner()


class TestBaseCommand:
    """测试基础计算命令。"""

    def test_fibonacci_valid(self, runner):
        """测试有效的输入。"""
        result = runner.invoke(app, ["10"])
        assert result.exit_code == 0
        assert "55" in result.output

    def test_fibonacci_zero(self, runner):
        """测试 n=0 的情况。"""
        result = runner.invoke(app, ["0"])
        assert result.exit_code == 0
        assert "0" in result.output

    def test_fibonacci_negative(self, runner):
        """测试负数输入返回错误。"""
        result = runner.invoke(app, ["-5"])
        assert result.exit_code != 0
        assert "错误" in result.output or "error" in result.output.lower()


class TestSequenceCommand:
    """测试序列命令。"""

    def test_sequence_valid(self, runner):
        """测试有效的序列请求。"""
        result = runner.invoke(app, ["sequence", "5"])
        assert result.exit_code == 0
        # 验证包含前 5 项
        assert "0" in result.output
        assert "3" in result.output

    def test_sequence_zero(self, runner):
        """测试 count=0 返回错误。"""
        result = runner.invoke(app, ["sequence", "0"])
        assert result.exit_code != 0
```

- [ ] **Step 2: 运行测试验证失败**

```bash
pytest tests/test_cli.py::TestBaseCommand::test_fibonacci_valid -v
```

预期：FAIL（模块不存在）

- [ ] **Step 3: 创建主入口文件**

```python
# src/cli/main.py
"""斐波那契 CLI 工具主入口。"""
import typer
from cli.commands import calculate_fibonacci, calculate_sequence, interactive_mode
from cli import __version__, __description__

# 创建 Typer 应用
app = typer.Typer(
    name="fibonacci",
    help="斐波那契计算器 - 教学演示工具",
    add_completion=True
)


@app.command(invoke_without_command=True)
def main(
    n: int = typer.Argument(None, help="斐波那契数列的索引"),
    sequence: bool = typer.Option(False, "-s", "--sequence", help="显示序列模式"),
    interactive: bool = typer.Option(False, "-i", "--interactive", help="进入交互模式"),
    guide: bool = typer.Option(False, "-g", "--guide", help="启动新手引导"),
    version: bool = typer.Option(
        False, "-v", "--version",
        callback=lambda: typer.echo(f"fibonacci {__version__}") and typer.Exit(),
        help="显示版本号"
    )
):
    """
    斐波那契计算器 - 计算第 n 个斐波那契数或显示序列。

    示例:
        fibonacci 10           # 计算第 10 个斐波那契数
        fibonacci sequence 5   # 显示前 5 项
        fibonacci -i           # 进入交互模式
        fibonacci --guide      # 启动新手引导
    """
    if guide:
        from cli.commands import show_guide
        show_guide()
        return

    if interactive:
        interactive_mode()
        return

    if n is not None:
        if sequence:
            calculate_sequence(n)
        else:
            calculate_fibonacci(n)
    else:
        # 无参数时显示帮助
        typer.echo(typer.style("使用 fibonacci --help 查看用法", fg=typer.colors.YELLOW))


@app.command()
def seq(
    count: int = typer.Argument(..., help="要显示的项数"),
):
    """显示前 COUNT 项斐波那契序列。"""
    calculate_sequence(count)


@app.command()
def interact():
    """进入交互式计算模式。"""
    interactive_mode()


@app.command()
def guide():
    """启动新手引导模式。"""
    from cli.commands import show_guide
    show_guide()


if __name__ == "__main__":
    app()
```

- [ ] **Step 4: 创建命令定义文件**

```python
# src/cli/commands.py
"""CLI 命令实现模块。"""
import typer
from cli.formatters import format_result_box, format_sequence_table, format_error_message
from io import StringIO
import sys


def get_fibonacci(n: int) -> int:
    """
    计算第 n 个斐波那契数。

    Args:
        n: 斐波那契数列的索引 (n >= 0)

    Returns:
        第 n 个斐波那契数
    """
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n < 2:
        return n
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


def get_fibonacci_sequence(count: int) -> list[int]:
    """
    生成前 count 项斐波那契序列。

    Args:
        count: 要生成的项数 (count >= 1)

    Returns:
        包含前 count 项斐波那契数的列表
    """
    if count < 1:
        raise ValueError("count 必须是正整数")
    return [get_fibonacci(i) for i in range(count)]


def calculate_fibonacci(n: int):
    """
    计算并格式化输出第 n 个斐波那契数。

    Args:
        n: 斐波那契数列的索引
    """
    try:
        if n < 0:
            typer.echo(format_error_message(
                "索引 n 必须是非负整数",
                "斐波那契数列从 0 开始，如 fibonacci 0, fibonacci 1, ..."
            ), err=True)
            raise typer.Exit(code=1)

        result = get_fibonacci(n)
        typer.echo(format_result_box(n, result))

    except ValueError as e:
        typer.echo(format_error_message(str(e)), err=True)
        raise typer.Exit(code=1)


def calculate_sequence(count: int):
    """
    计算并格式化输出前 count 项斐波那契序列。

    Args:
        count: 要显示的项数
    """
    try:
        if count < 1:
            typer.echo(format_error_message(
                "序列计数必须是正整数",
                "请指定至少 1 项，如 fibonacci sequence 1"
            ), err=True)
            raise typer.Exit(code=1)

        sequence = get_fibonacci_sequence(count)
        typer.echo(format_sequence_table(sequence))

    except ValueError as e:
        typer.echo(format_error_message(str(e)), err=True)
        raise typer.Exit(code=1)


def interactive_mode():
    """
    进入交互式计算模式。
    """
    from rich.prompt import Prompt
    from cli.formatters import format_guide_intro

    console = typer.Console()
    console.print(format_guide_intro())

    while True:
        typer.echo("\n[bold]你想：[/bold]")
        typer.echo("  1. 计算一个具体的斐波那契数")
        typer.echo("  2. 查看数列的前几项")
        typer.echo("  3. 退出")

        choice = Prompt.ask("请选择", choices=["1", "2", "3"], default="1")

        if choice == "1":
            n_str = Prompt.ask("请输入 n 的值")
            try:
                n = int(n_str)
                calculate_fibonacci(n)
            except ValueError:
                typer.echo(format_error_message("请输入有效的整数"))
        elif choice == "2":
            count_str = Prompt.ask("请输入要显示的项数")
            try:
                count = int(count_str)
                calculate_sequence(count)
            except ValueError:
                typer.echo(format_error_message("请输入有效的整数"))
        elif choice == "3":
            typer.echo("👋 再见！")
            break


def show_guide():
    """
    显示新手引导内容。
    """
    from cli.formatters import format_guide_intro
    from rich.prompt import Prompt

    console = typer.Console()
    console.print(format_guide_intro())

    typer.echo("\n[bold]让我们开始吧！你想：[/bold]")
    typer.echo("  1. 计算一个具体的斐波那契数")
    typer.echo("  2. 查看数列的前几项")
    typer.echo("  3. 了解更多关于斐波那契的知识")

    choice = Prompt.ask("请选择", choices=["1", "2", "3"], default="1")

    if choice == "1":
        n_str = Prompt.ask("请输入 n 的值")
        try:
            n = int(n_str)
            calculate_fibonacci(n)
        except ValueError:
            typer.echo(format_error_message("请输入有效的整数"))
    elif choice == "2":
        count_str = Prompt.ask("请输入要显示的项数")
        try:
            count = int(count_str)
            calculate_sequence(count)
        except ValueError:
            typer.echo(format_error_message("请输入有效的整数"))
    elif choice == "3":
        typer.echo("\n[bold]关于斐波那契数列：[/bold]")
        typer.echo("斐波那契数列由意大利数学家莱昂纳多·斐波那契发现。")
        typer.echo("它在自然界中广泛存在，如花瓣数量、螺旋形状等。")
        typer.echo("相邻两项的比值趋近于黄金比例 φ ≈ 1.618...")
```

- [ ] **Step 5: 运行测试验证通过**

```bash
pytest tests/test_cli.py::TestBaseCommand -v
```

预期：3 个测试全部 PASS

- [ ] **Step 6: 提交**

```bash
git add src/cli/main.py src/cli/commands.py tests/test_cli.py
git commit -m "feat: 添加 CLI 主入口和命令实现"
```

---

### Task 4: 交互模式完整实现

**Files:**
- Create: `src/cli/interactive.py`
- Test: `tests/test_interactive.py`

- [ ] **Step 1: 编写失败的测试**

```python
# tests/test_interactive.py
"""交互模式测试。"""
import pytest
from unittest.mock import patch
from io import StringIO
import sys
sys.path.insert(0, 'src')


class TestInteractiveMode:
    """测试交互模式。"""

    @patch('builtins.input', side_effect=['1', '10', '3'])
    def test_interactive_calculate_and_exit(self, mock_input):
        """测试交互模式中计算并退出。"""
        from cli.interactive import run_interactive_session
        # 验证不抛出异常
        try:
            run_interactive_session()
        except Exception as e:
            pytest.fail(f"交互模式抛出异常：{e}")

    @patch('builtins.input', side_effect=['2', '5', '3'])
    def test_interactive_sequence(self, mock_input):
        """测试交互模式中显示序列。"""
        from cli.interactive import run_interactive_session
        try:
            run_interactive_session()
        except Exception as e:
            pytest.fail(f"交互模式抛出异常：{e}")
```

- [ ] **Step 2: 运行测试验证失败**

```bash
pytest tests/test_interactive.py::TestInteractiveMode::test_interactive_calculate_and_exit -v
```

预期：FAIL（模块不存在）

- [ ] **Step 3: 创建交互模式模块**

```python
# src/cli/interactive.py
"""交互模式专用模块。"""
import typer
from rich.prompt import Prompt
from rich.console import Console
from cli.commands import calculate_fibonacci, calculate_sequence, get_fibonacci, get_fibonacci_sequence
from cli.formatters import format_guide_intro, format_error_message


def run_interactive_session():
    """
    运行完整的交互式计算会话。

    提供菜单驱动的界面，用户可以：
    1. 计算单个斐波那契数
    2. 显示斐波那契序列
    3. 退出
    """
    console = Console()

    # 显示欢迎消息
    console.print(format_guide_intro())

    while True:
        _show_menu()
        choice = Prompt.ask("请选择", choices=["1", "2", "3"], default="1")

        if choice == "1":
            _handle_calculate()
        elif choice == "2":
            _handle_sequence()
        elif choice == "3":
            _handle_exit()
            break


def _show_menu():
    """显示主菜单。"""
    typer.echo("\n[bold]你想：[/bold]")
    typer.echo("  1. 计算一个具体的斐波那契数")
    typer.echo("  2. 查看数列的前几项")
    typer.echo("  3. 退出")


def _handle_calculate():
    """处理单个斐波那契数计算。"""
    n_str = Prompt.ask("请输入 n 的值")
    try:
        n = int(n_str)
        from cli.commands import calculate_fibonacci as calc
        calc(n)
    except ValueError:
        typer.echo(format_error_message("请输入有效的整数"))
    except typer.Exit:
        pass  # calculate_fibonacci 可能抛出 Exit


def _handle_sequence():
    """处理序列显示。"""
    count_str = Prompt.ask("请输入要显示的项数")
    try:
        count = int(count_str)
        from cli.commands import calculate_sequence as calc_seq
        calc_seq(count)
    except ValueError:
        typer.echo(format_error_message("请输入有效的整数"))
    except typer.Exit:
        pass


def _handle_exit():
    """处理退出。"""
    typer.echo("👋 再见！")
```

- [ ] **Step 4: 更新 commands.py 使用 interactive.py**

```python
# 在 src/cli/commands.py 中更新 interactive_mode 函数
def interactive_mode():
    """进入交互式计算模式。"""
    from cli.interactive import run_interactive_session
    run_interactive_session()
```

- [ ] **Step 5: 运行测试验证通过**

```bash
pytest tests/test_interactive.py -v
```

预期：2 个测试全部 PASS

- [ ] **Step 6: 提交**

```bash
git add src/cli/interactive.py tests/test_interactive.py
git commit -m "feat: 添加交互模式完整实现"
```

---

### Task 5: 项目文档和入口脚本

**Files:**
- Create: `README-CLI.md`
- Create: `bin/fibonacci`

- [ ] **Step 1: 创建 CLI README**

```markdown
# 斐波那契 CLI 工具

一个用于计算斐波那契数列的命令行工具，专为教学演示设计。

## 功能特性

- 📊 计算第 n 个斐波那契数
- 📋 显示前 n 项斐波那契序列（表格格式）
- 🎓 交互式学习模式
- 👶 新手引导模式
- ❌ 友好的错误提示

## 安装

```bash
# 安装依赖
pip install -r requirements-cli.txt
```

## 使用方法

### 基础计算

```bash
# 计算第 10 个斐波那契数
python -m cli.main 10

# 或者使用模块方式
python src/cli/main.py 10
```

### 序列显示

```bash
# 显示前 5 项序列
python -m cli.main sequence 5
python src/cli/main.py seq 5
```

### 交互模式

```bash
# 进入交互模式
python -m cli.main -i
python src/cli/main.py interact
```

### 新手引导

```bash
# 启动新手引导
python -m cli.main --guide
python src/cli/main.py guide
```

### 帮助信息

```bash
python -m cli.main --help
```

## 输出示例

### 基础计算

```
$ python -m cli.main 10
╔════════════════════════════════════╗
║  📊 斐波那契计算结果                ║
╠════════════════════════════════════╣
║  索引 (n):     10                  ║
║  结果：        55                  ║
╚════════════════════════════════════╝
```

### 序列显示

```
$ python -m cli.main seq 5
╔═══════════════════════════════════════════════════╗
║  📋 斐波那契序列 (前 5 项)                          ║
╠═══════╦═══════════════════════════════════════════╣
║  索引 ║  值                                       ║
╠═══════╬═══════════════════════════════════════════╣
║   0   ║  0                                        ║
║   1   ║  1                                        ║
║   2   ║  1                                        ║
║   3   ║  2                                        ║
║   4   ║  3                                        ║
╚═══════╩═══════════════════════════════════════════╝
```

### 错误提示

```
$ python -m cli.main -5
❌ 错误：索引 n 必须是非负整数
💡 提示：斐波那契数列从 0 开始，如 fibonacci 0, fibonacci 1, ...
```

## 运行测试

```bash
pytest tests/test_cli.py -v
pytest tests/test_interactive.py -v
pytest tests/test_formatters.py -v
```

## 项目结构

```
src/cli/
├── __init__.py      # 模块初始化
├── main.py          # Typer 主入口
├── commands.py      # 命令实现
├── interactive.py   # 交互模式
└── formatters.py    # 输出格式化
tests/
├── test_cli.py
├── test_interactive.py
└── test_formatters.py
```
```

- [ ] **Step 2: 创建可执行入口脚本**

```python
# bin/fibonacci
#!/usr/bin/env python3
"""斐波那契 CLI 工具可执行入口。"""
import sys
import os

# 添加 src 目录到 Python 路径
script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(script_dir, '..', 'src')
sys.path.insert(0, src_dir)

from cli.main import app

if __name__ == "__main__":
    app()
```

- [ ] **Step 3: 使脚本可执行**

```bash
chmod +x bin/fibonacci
```

- [ ] **Step 4: 测试安装和运行**

```bash
# 测试本地运行
python -m cli.main 10
python -m cli.main seq 5
python -m cli.main --help
```

- [ ] **Step 5: 运行完整测试套件**

```bash
pytest tests/ -v --tb=short
```

预期：所有测试 PASS (10+ 个测试)

- [ ] **Step 6: 提交**

```bash
git add README-CLI.md bin/fibonacci
git commit -m "docs: 添加 CLI 文档和可执行入口"
```

---

## 自我审查

### 1. 规格覆盖检查

| 规格要求 | 对应任务 | 状态 |
|----------|----------|------|
| 基础计算命令 | Task 3 | ✅ |
| 序列显示命令 | Task 3 | ✅ |
| 交互模式 | Task 4 | ✅ |
| 表格/美化输出 | Task 2 | ✅ |
| 新手引导 | Task 3 (commands.py) | ✅ |
| 错误提示友好 | Task 2, Task 3 | ✅ |
| Typer 框架 | Task 3 | ✅ |
| Rich 美化 | Task 2 | ✅ |
| 完整测试覆盖 | Task 1-4 | ✅ |
| README 文档 | Task 5 | ✅ |

### 2. 占位符扫描

- 无 TBD/TODO ✅
- 所有步骤包含实际代码 ✅
- 所有命令包含预期输出 ✅

### 3. 类型一致性检查

- `get_fibonacci(n: int) -> int` - 所有调用处一致 ✅
- `get_fibonacci_sequence(count: int) -> list[int]` - 一致 ✅
- 格式化函数签名一致 ✅

---

## 执行选项

**计划完成并保存到 `docs/superpowers/plans/2026-04-09-fibonacci-cli-plan.md`。**

**两种执行选项：**

**1. 子代理驱动（推荐）** - 每个任务由独立子代理执行，任务间自动进行两轮审查（规格 + 代码质量），快速迭代

**2. 内联执行** - 在当前会话中按任务顺序执行，批量执行带检查点

**选择哪种方式开始实现？**
