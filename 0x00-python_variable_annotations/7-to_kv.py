#!/usr/bin/env python3
from typing import Union, Tuple
'''annotating tuples'''
def to_kv(k: str, v: Union[int, float])->Tuple[str, float]:
    return (k, (v**v))