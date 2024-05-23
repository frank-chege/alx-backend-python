#!/usr/bin/env python3
'''annotating lists with mixed types'''
from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]])->float:
    '''annotating lists with mixed types'''
    return sum(mxd_lst)