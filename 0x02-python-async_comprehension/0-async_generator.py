#!/usr/bin/env python3
"""
    Task 0. 
    function: async_generator
    Args: no arguments
"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """This function loops 10 times, each time asynchronously
    waits 1 second, then yields a random number between 0 and 10"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.random() * 10)
