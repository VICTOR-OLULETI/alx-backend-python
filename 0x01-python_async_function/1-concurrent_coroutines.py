#!/usr/bin/env python3
'''Task 1's module.
    Async routine wait_n
    Args: n int
    imports: wait_random from 0-basic_async_syntax
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n returns the list of all delays (float values)"""
    delay = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(delay)
