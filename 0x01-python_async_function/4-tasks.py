#!/usr/bin/env python3
'''execute multiple coroutines at the same time'''

import asyncio
from typing import List
module = __import__('3-tasks')
task_wait_random = module.task_wait_random

async def task_wait_n(n:int, max_delay:int) ->List[float]:
    '''execute multiple coroutines at the same time'''
    list = []
    for x in range(n):
        wait_time = await task_wait_random(max_delay)
        list.append(wait_time)
        if x > 0:
            for y in range(x):
                if (list[y] < list[y-1]):
                    tmp = list[y]
                    list[y] = list[y-1]
                    list[y-1] = tmp
    return list
