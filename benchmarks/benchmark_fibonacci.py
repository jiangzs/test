"""
Fibonacci 算法性能基准测试。

比较迭代算法 O(n) 和矩阵快速幂算法 O(log n) 的性能差异。
"""

import os
import sys
import timeit

# 添加父目录到路径以导入 fibonacci_example
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from fibonacci_example import fibonacci_iterative, fibonacci_fast


def benchmark_function(func, n, number=10000):
    """
    测量函数执行时间。

    参数:
        func: 要测试的函数
        n: 传递给函数的参数
        number: 重复执行次数

    返回:
        每次执行的平均时间（毫秒）
    """
    # 重新导入要测试的具体函数
    if func.__name__ == 'fibonacci_iterative':
        setup = "from fibonacci_example import fibonacci_iterative as func"
    else:
        setup = "from fibonacci_example import fibonacci_fast as func"

    time_taken = timeit.timeit(
        stmt=f'func({n})',
        setup=setup,
        number=number
    )
    return (time_taken / number) * 1000  # 转换为毫秒


def run_benchmarks():
    """运行所有基准测试。"""
    test_values = [10, 20, 30, 50, 100]

    print("=" * 60)
    print("Fibonacci 算法性能对比")
    print("=" * 60)
    print(f"{'n':<10} {'迭代算法 (ms)':<20} {'快速算法 (ms)':<20} {'提升倍数':<15}")
    print("-" * 60)

    for n in test_values:
        iterative_time = benchmark_function(fibonacci_iterative, n)
        fast_time = benchmark_function(fibonacci_fast, n)
        speedup = iterative_time / fast_time if fast_time > 0 else float('inf')
        print(f"{n:<10} {iterative_time:<20.4f} {fast_time:<20.4f} {speedup:<15.2f}x")

    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
