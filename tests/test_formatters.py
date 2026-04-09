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
