from typing import List


def some(pred, _list: List[any]):
    for p in _list:
        if pred(p):
            return True
    return False


def find(pred, _list: List[any]):
    for p in _list:
        if pred(p):
            return p
    return None