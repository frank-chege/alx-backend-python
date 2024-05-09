#!/usr/bin/env python3
'''asynchronous generator'''
import random
import asyncio
from typing import Any

async def async_generator()->Any:
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)