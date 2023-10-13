#!/usr/bin/env python3
"""
    Task 3
    function: task_wait_random
    Args: max_delay - int
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function takes in an integer max_delay and returns a
    asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
