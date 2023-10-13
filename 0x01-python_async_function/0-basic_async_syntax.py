#!/usr/bin/env python3
'''Task 0's module.
    Write an asynchronous coroutine that takes in an integer argument and
    waits for a randome delay between 0 and max_delay
    function wait_random
    args: max_delay int default_value = 10

'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        waits for a random delay
    """
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
