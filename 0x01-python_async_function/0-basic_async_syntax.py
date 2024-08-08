#!/usr/bin/env python3
"""Task 0's Module
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Returns the waited time at randon number of seconds"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
