"""交互模式专用模块。"""
import typer
from rich.prompt import Prompt
from rich.console import Console
from cli.commands import calculate_fibonacci, calculate_sequence
from cli.formatters import format_guide_intro, format_error_message


def run_interactive_session():
    """运行完整的交互式计算会话。"""
    console = Console()
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
        calculate_fibonacci(n)
    except ValueError:
        typer.echo(format_error_message("请输入有效的整数"))
    except typer.Exit:
        pass


def _handle_sequence():
    """处理序列显示。"""
    count_str = Prompt.ask("请输入要显示的项数")
    try:
        count = int(count_str)
        calculate_sequence(count)
    except ValueError:
        typer.echo(format_error_message("请输入有效的整数"))
    except typer.Exit:
        pass


def _handle_exit():
    """处理退出。"""
    typer.echo("👋 再见！")
