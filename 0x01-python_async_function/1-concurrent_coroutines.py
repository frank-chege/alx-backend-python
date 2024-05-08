#!/usr/bin/env python3
'''execute multiple coroutines at the same time'''

import asyncio
from typing import List
module = __import__('0-basic_async_syntax')
wait_random = module.wait_random

async def wait_n(n:int, max_delay:int) ->List[float]:
    '''execute multiple coroutines at the same time'''
    list = []
    for x in range(n):
        wait_time = await wait_random(max_delay)
        list.append(wait_time)
        if x > 0:
            for y in range(x):
                if (list[y] < list[y-1]):
                    tmp = list[y]
                    list[y] = list[y-1]
                    list[y-1] = tmp
    return list
