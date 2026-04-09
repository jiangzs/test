"""交互模式测试。"""
import pytest
from unittest.mock import patch
import sys
sys.path.insert(0, 'src')


class TestInteractiveMode:
    """测试交互模式。"""

    @patch('builtins.input', side_effect=['1', '10', '3'])
    def test_interactive_calculate_and_exit(self, mock_input):
        """测试交互模式中计算并退出。"""
        from cli.interactive import run_interactive_session
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
