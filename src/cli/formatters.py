"""CLI 输出格式化模块。"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box


def format_result_box(n: int, result: int) -> str:
    """
    格式化单个斐波那契数的结果输出。
    """
    console = Console()
    content = f"[bold]索引 (n):[/bold]     {n}\n[bold]结果：[/bold]        {result}"
    panel = Panel(
        content,
        title="📊 斐波那契计算结果",
        box=box.DOUBLE_EDGE,
        border_style="blue"
    )
    from io import StringIO
    output = StringIO()
    console.file = output
    console.print(panel)
    return output.getvalue()


def format_sequence_table(sequence: list[int]) -> str:
    """
    格式化斐波那契序列的表格输出。
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
    """格式化错误消息输出。"""
    console = Console()
    from io import StringIO
    output = StringIO()
    console.file = output
    console.print(f"❌ 错误：{message}", style="red bold")
    if hint:
        console.print(f"💡 提示：{hint}", style="yellow")
    return output.getvalue()


def format_guide_intro() -> str:
    """格式化新手引导的欢迎消息。"""
    console = Console()
    content = """[bold blue]👋 欢迎来到斐波那契计算器！[/bold blue]

这是一个交互式学习工具，帮助你理解斐波那契数列。

[bold] 斐波那契数列是：[/bold] 0, 1, 1, 2, 3, 5, 8, 13...
每个数字是前两个数字的和。"""
    panel = Panel(content, title="🎓 新手引导", border_style="cyan")
    from io import StringIO
    output = StringIO()
    console.file = output
    console.print(panel)
    return output.getvalue()
