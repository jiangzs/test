"""CLI 命令实现模块。"""
import typer
from cli.formatters import format_result_box, format_sequence_table, format_error_message


def get_fibonacci(n: int) -> int:
    """计算第 n 个斐波那契数。"""
    if n < 0:
        raise ValueError("n 必须是非负整数")
    if n < 2:
        return n
    return get_fibonacci(n - 1) + get_fibonacci(n - 2)


def get_fibonacci_sequence(count: int) -> list[int]:
    """生成前 count 项斐波那契序列。"""
    if count < 1:
        raise ValueError("count 必须是正整数")
    return [get_fibonacci(i) for i in range(count)]


def calculate_fibonacci(n: int):
    """计算并格式化输出第 n 个斐波那契数。"""
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
    """计算并格式化输出前 count 项斐波那契序列。"""
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
    """进入交互式计算模式。"""
    from cli.interactive import run_interactive_session
    run_interactive_session()


def show_guide():
    """显示新手引导内容。"""
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
