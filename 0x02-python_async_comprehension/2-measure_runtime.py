#!/usr/bin/env python3
'''run coroutines concurrently'''
import asyncio
import time
from typing import 

module = __import__('1-async_comprehension')
async_comprehension = module.async_comprehension

async def measure_runtime()->float:
    '''concurrency'''
    tasks= []
    for x in range(4):
        tasks.append(async_comprehension())
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    runtime = end_time - start_time
    return runtime