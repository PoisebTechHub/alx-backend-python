#!/usr/bin/env python3
"""Task's 0 Module
"""

import asyncio
import random


from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Iterate 10 times, 1 sec wait each time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
