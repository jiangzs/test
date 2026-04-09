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
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 默认使用迭代算法
fibonacci = fibonacci_iterative


def _matrix_multiply(a, b):
    """
    2x2 矩阵乘法。

    参数:
        a: 2x2 矩阵 [[a11, a12], [a21, a22]]
        b: 2x2 矩阵 [[b11, b12], [b21, b22]]

    返回:
        2x2 矩阵，a 和 b 的乘积
    """
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]


def _matrix_power(matrix, n):
    """
    计算矩阵的 n 次幂（快速幂算法）。

    参数:
        matrix: 2x2 矩阵
        n: 幂次，非负整数

    返回:
        matrix 的 n 次幂
    """
    # 单位矩阵
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = _matrix_multiply(result, matrix)
        matrix = _matrix_multiply(matrix, matrix)
        n //= 2
    return result


def fibonacci_fast(n):
    """
    使用矩阵快速幂算法计算第 n 个斐波那契数。

    基于恒等式：[[1,1],[1,0]]^n = [[F(n+1), F(n)], [F(n), F(n-1)]]

    参数:
        n (int): 要计算的斐波那契数的位置，必须是非负整数

    返回:
        int: 第 n 个斐波那契数

    示例:
        >>> fibonacci_fast(0)
        0
        >>> fibonacci_fast(1)
        1
        >>> fibonacci_fast(5)
        5
        >>> fibonacci_fast(10)
        55

    注意:
        使用矩阵快速幂算法，时间复杂度 O(log n)，空间复杂度 O(1)
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0

    # 基础矩阵 [[1, 1], [1, 0]]
    base = [[1, 1], [1, 0]]
    result = _matrix_power(base, n)
    return result[0][1]


# 默认使用快速算法
fibonacci = fibonacci_fast


if __name__ == "__main__":
    # 示例：计算第 10 个斐波那契数
    number = 10
    result = fibonacci(number)
    print(f"The {number}th Fibonacci number is: {result}")

    # 运行 doctest 测试
    import doctest
    doctest.testmod(verbose=True)