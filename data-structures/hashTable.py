#  -----------------------------------------------------------
#
#  Python hash table data structure realisation
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

def _hash(data: str, key: int)-> int:
    result = 0
    for pos in range(len(data)):
        result += ord(data[pos]) * pos
    return result % key


def _rehash(hash_: int, key: int)-> int:
    return (hash_ + 1) % key


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def get(self, key: int):
        return self.data[key]

    def add(self, data: str):
        hash_ = _hash(data, self.size)
        while self.data[hash_] is not None:
            hash_ = _rehash(hash_, self.size)
        self.data[hash_] = data

    def delete(self, key: int):
        self.data[key] = None
