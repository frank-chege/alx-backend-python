#!/usr/bin/env python3
'''create tasks'''
import asyncio
from typing import Any

module = __import__('0-basic_async_syntax')
wait_random = module.wait_random

def task_wait_random(max_delay:int)->asyncio.Task:
    '''returns an asyncio task'''
    task = asyncio.create_task(wait_random(max_delay))
    return task