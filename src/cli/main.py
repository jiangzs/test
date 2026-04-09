"""斐波那契 CLI 工具主入口。"""
import typer
from cli.commands import calculate_fibonacci, calculate_sequence, interactive_mode, show_guide
from cli import __version__, __description__

# 主应用
app = typer.Typer(
    name="fibonacci",
    help="斐波那契计算器 - 教学演示工具",
    add_completion=True
)


@app.command()
def fib(
    n: int = typer.Argument(..., help="斐波那契数列的索引"),
    sequence: bool = typer.Option(False, "-s", "--sequence", help="显示序列模式"),
    interactive: bool = typer.Option(False, "-i", "--interactive", help="进入交互模式"),
    guide: bool = typer.Option(False, "-g", "--guide", help="启动新手引导"),
    version: bool = typer.Option(
        False, "-v", "--version",
        callback=lambda: typer.echo(f"fibonacci {__version__}") or typer.Exit(),
        help="显示版本号"
    )
):
    """计算第 n 个斐波那契数。"""
    if guide:
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


@app.command()
def seq(count: int = typer.Argument(..., help="要显示的项数")):
    """显示前 COUNT 项斐波那契序列。"""
    calculate_sequence(count)


@app.command()
def interact():
    """进入交互式计算模式。"""
    interactive_mode()


@app.command()
def guide_cmd():
    """启动新手引导模式。"""
    show_guide()


if __name__ == "__main__":
    app()
