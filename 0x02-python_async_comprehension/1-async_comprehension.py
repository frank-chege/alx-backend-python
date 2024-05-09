#!/usr/bin/env python3
'''using async comprehension'''

module = __import__('0-async_generator')
async_generator = module.async_generator

async def async_comprehension():
    '''using async comprehension'''
    return [random async for random in async_generator()]