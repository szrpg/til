#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
training:
  https://docs.python.org/ja/3.8/library/typing.html
'''

def greeting(name: str) -> str:
    '''型チェッカー
    '''
    return 'Hello ' + name

print(greeting('world'))
try:
    print(greeting(123))
except TypeError as te:
    print('print(greeting(123))')
    print(f'TypeError: {te}')

def greeting(name: str) -> str:
    '''戻り値が合っていないと型チェッカーが働かない
    '''
    #return 'Hello ' + name
    return 123

print(greeting('world'))
print(greeting(0))


# https://docs.python.org/ja/3.8/library/typing.html#type-aliases

from typing import List
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2., [1., -4.2, 5.4])
print(new_vector)

from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcat_message(message: str, servers: Sequence[Server]) -> None:
    pass



