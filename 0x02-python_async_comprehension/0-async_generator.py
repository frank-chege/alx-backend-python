#!/usr/bin/env python3
'''asynchronous generator'''
import random
import asyncio
from typing import AsyncGenerator

async def async_generator()->AsyncGenerator[float, None]:
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0,10)