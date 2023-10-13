#!/usr/bin/env python3
"""
    Task 2
    Measuring Runtime
    function: measure_time
    Args: n - int
        : max_delay - int
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        returns: the total execution time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
