import os
import datetime
from functools import wraps

from task2 import logger

@logger('gen.log')
def flat_generator(list_of_lists):
    for list_ in list_of_lists:
        for item in list_:
            yield item

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
        ]

flat_generator(list_of_lists_1)