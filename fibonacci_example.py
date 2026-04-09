def fibonacci_iterative(n):
    """
    使用迭代法计算第 n 个斐波那契数。

    斐波那契数列：0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    其中 F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) (n >= 2)

    参数:
        n (int): 要计算的斐波那契数的位置，必须是非负整数

    返回:
        int: 第 n 个斐波那契数

    示例:
        >>> fibonacci_iterative(0)
        0
        >>> fibonacci_iterative(1)
        1
        >>> fibonacci_iterative(5)
        5
        >>> fibonacci_iterative(10)
        55

    注意:
        使用迭代算法，时间复杂度 O(n)，空间复杂度 O(1)
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 默认使用迭代算法
fibonacci = fibonacci_iterative


if __name__ == "__main__":
    # 示例：计算第 10 个斐波那契数
    number = 10
    result = fibonacci(number)
    print(f"The {number}th Fibonacci number is: {result}")

    # 运行 doctest 测试
    import doctest
    doctest.testmod(verbose=True)