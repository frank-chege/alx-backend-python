#!/usr/bin/env python3
'''annotate a callable'''
from typing import Callable
def make_multiplier(multiplier: float) ->Callable[[float], float]:
    '''create a function that multiplies a float by the multiplier'''
    def func(x: float)->float:
        '''multiplies x by multiplier'''
        return x * multiplier
    return func
