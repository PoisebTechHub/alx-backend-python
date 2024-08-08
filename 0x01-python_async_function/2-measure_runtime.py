#!/usr/bin/env python3
"""Task 2's Module
"""

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns the overall execution time"""
    start_time = time.time()
    # call wait_n function n times
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    # Calculate the average time per call
    total_time = end_time - start_time
    return (total_time/n)
