#!/usr/bin/env python3
""" Module documentation """
import asyncio
import random
from typing import List
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> List:
    """doc func"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return end - start
