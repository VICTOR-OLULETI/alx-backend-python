#!/usr/bin/env python3
"""
    Task 1.
    function: async_generator
    Args: no arguments
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This coroutine will collect 10 random numbers using an async
    comprehensing over async generator"""
    return [i async for i in async_generator()]
