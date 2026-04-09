"""CLI 命令测试。"""
import pytest
from typer.testing import CliRunner
import sys
sys.path.insert(0, 'src')


@pytest.fixture
def runner():
    """创建测试运行器。"""
    from cli.main import app
    return CliRunner(), app


class TestBaseCommand:
    """测试基础计算命令。"""

    def test_fibonacci_valid(self, runner):
        """测试有效的输入。"""
        runner_instance, app = runner
        result = runner_instance.invoke(app, ["fib", "10"])
        assert result.exit_code == 0
        assert "55" in result.output

    def test_fibonacci_zero(self, runner):
        """测试 n=0 的情况。"""
        runner_instance, app = runner
        result = runner_instance.invoke(app, ["fib", "0"])
        assert result.exit_code == 0
        assert "0" in result.output

    def test_fibonacci_negative(self, runner):
        """测试负数输入返回错误。"""
        runner_instance, app = runner
        result = runner_instance.invoke(app, ["fib", "-5"])
        assert result.exit_code != 0
        assert "错误" in result.output or "error" in result.output.lower()


class TestSequenceCommand:
    """测试序列命令。"""

    def test_sequence_valid(self, runner):
        """测试有效的序列请求。"""
        runner_instance, app = runner
        result = runner_instance.invoke(app, ["seq", "5"])
        assert result.exit_code == 0
        assert "0" in result.output
        assert "3" in result.output

    def test_sequence_zero(self, runner):
        """测试 count=0 返回错误。"""
        runner_instance, app = runner
        result = runner_instance.invoke(app, ["seq", "0"])
        assert result.exit_code != 0
