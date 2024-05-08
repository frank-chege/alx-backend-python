#!/usr/bin/env python3
import time
import asyncio
'''measure the runtime'''
module = __import__('1-concurrent_coroutines')
wait_n = module.wait_n

def measure_time(n:int, max_delay:int) ->float:
    '''measure the runtime'''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    runtime = end_time - start_time
    return runtime / n