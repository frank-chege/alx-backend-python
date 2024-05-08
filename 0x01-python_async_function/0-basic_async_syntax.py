#!/usr/bin/env python3
'''using random library'''
import asyncio
import random
async def  wait_random(max_delay:int =10) ->float:
    '''returns the wait time'''
    wait_time = random.uniform(0, max_delay)
    return wait_time
