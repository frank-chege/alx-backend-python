#!/usr/bin/env python3
'''duck typing annotation'''
from typing import Iterable, Sequence, List
def element_length(lst: Iterable[Sequence])->List[tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]