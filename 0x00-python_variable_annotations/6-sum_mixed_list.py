#!/usr/bin/env python3
'''annotating lists with mixed types'''
from typing import List
def sum_mixed_list(mxd_lst: List[int, float])->float:
    '''annotating lists with mixed types'''
    return sum(mxd_lst)