#!/usr/bin/env python3
"""
    Task 2. 
    function: measure_runtime
    Args: no arguments
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
        this function executes async_comprehension four times in parallel
        and measures runtime        
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension(),
                            async_comprehension(),
                            async_comprehension(),
                            async_comprehension()))
        
    return (time.time() - start_time)
