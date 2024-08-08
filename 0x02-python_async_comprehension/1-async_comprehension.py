#!/usr/bin/env python3
"""Task's 1 Module
"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension"""
    return [random_number async for random_number in async_generator()]
