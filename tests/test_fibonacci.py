"""Fibonacci 函数的单元测试。"""

import pytest
from fibonacci_example import fibonacci_iterative, fibonacci_fast


class TestFibonacciIterative:
    """测试迭代版本的 fibonacci 函数。"""

    def test_fibonacci_0(self):
        """测试 fibonacci(0)。"""
        assert fibonacci_iterative(0) == 0

    def test_fibonacci_1(self):
        """测试 fibonacci(1)。"""
        assert fibonacci_iterative(1) == 1

    def test_fibonacci_2(self):
        """测试 fibonacci(2)。"""
        assert fibonacci_iterative(2) == 1

    def test_fibonacci_5(self):
        """测试 fibonacci(5)。"""
        assert fibonacci_iterative(5) == 5

    def test_fibonacci_10(self):
        """测试 fibonacci(10)。"""
        assert fibonacci_iterative(10) == 55

    def test_fibonacci_20(self):
        """测试 fibonacci(20)。"""
        assert fibonacci_iterative(20) == 6765

    def test_fibonacci_sequence(self):
        """测试前 11 个斐波那契数。"""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        result = [fibonacci_iterative(i) for i in range(11)]
        assert result == expected

    def test_fibonacci_invalid_input(self):
        """测试负数输入。"""
        with pytest.raises(ValueError):
            fibonacci_iterative(-1)


class TestFibonacciFast:
    """测试矩阵快速幂版本的 fibonacci 函数。"""

    def test_fibonacci_0(self):
        """测试 fibonacci(0)。"""
        assert fibonacci_fast(0) == 0

    def test_fibonacci_1(self):
        """测试 fibonacci(1)。"""
        assert fibonacci_fast(1) == 1

    def test_fibonacci_2(self):
        """测试 fibonacci(2)。"""
        assert fibonacci_fast(2) == 1

    def test_fibonacci_5(self):
        """测试 fibonacci(5)。"""
        assert fibonacci_fast(5) == 5

    def test_fibonacci_10(self):
        """测试 fibonacci(10)。"""
        assert fibonacci_fast(10) == 55

    def test_fibonacci_20(self):
        """测试 fibonacci(20)。"""
        assert fibonacci_fast(20) == 6765

    def test_fibonacci_sequence(self):
        """测试前 11 个斐波那契数。"""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        result = [fibonacci_fast(i) for i in range(11)]
        assert result == expected

    def test_fibonacci_invalid_input(self):
        """测试负数输入。"""
        with pytest.raises(ValueError):
            fibonacci_fast(-1)


class TestFibonacciConsistency:
    """测试两种实现的一致性。"""

    def test_both_implementations_match(self):
        """测试两种算法在 0-50 范围内结果一致。"""
        for i in range(51):
            assert fibonacci_iterative(i) == fibonacci_fast(i), f"Mismatch at {i}"


class TestFibonacciInputValidation:
    """测试输入验证。"""

    def test_boolean_true_rejected(self):
        """测试布尔值 True 被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_iterative(True)

    def test_boolean_false_rejected(self):
        """测试布尔值 False 被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_iterative(False)

    def test_float_rejected(self):
        """测试浮点数被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_iterative(10.5)

    def test_string_rejected(self):
        """测试字符串被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_iterative("10")

    def test_none_rejected(self):
        """测试 None 被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_iterative(None)

    def test_fast_boolean_true_rejected(self):
        """测试快速算法布尔值 True 被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_fast(True)

    def test_fast_boolean_false_rejected(self):
        """测试快速算法布尔值 False 被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_fast(False)

    def test_fast_float_rejected(self):
        """测试快速算法浮点数被拒绝。"""
        with pytest.raises(ValueError):
            fibonacci_fast(10.5)
