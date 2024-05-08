#!/usr/bin/env python3
import asyncio
module = __import__('0-basic_async_syntax')
wait_random = module.wait_random
'''execute multiple coroutines at the same time'''

async def wait_n(n, max_delay):
    '''execute multiple coroutines at the same time'''
    list = []
    for x in range(n):
        wait_time = await wait_random(max_delay)
        list.append(wait_time)
    return list