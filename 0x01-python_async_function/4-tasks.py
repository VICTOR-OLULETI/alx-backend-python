#!/usr/bin/env python3
'''Task 4's module.
    Async function task_wait_n
    Args: n int
    imports: wait_random from 0-basic_async_syntax
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n returns the list of all delays (float values)"""
    delay = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
        )
    return sorted(delay)
