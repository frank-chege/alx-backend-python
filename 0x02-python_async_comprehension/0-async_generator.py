#!/usr/bin/env python3
'''asynchronous generator'''
import random
import asyncio

async def async_generator():
    for x in range(10):
        await asyncio.sleep(1)
        yield random.randint(0,10)