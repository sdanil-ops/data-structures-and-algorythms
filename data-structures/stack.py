#  -----------------------------------------------------------
#
#  Python stack data structure realisation
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------


class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []
        self.max_items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if self.top():
            if item < self.top():
                self.min_items.append(item)
            if item > self.top():
                self.max_items.append(item)
            self.items.append(item)
        else:
            self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]

    def get_min(self):
        if len(self.min_items) == 0:
            return None
        return self.min_items[len(self.min_items) - 1]

    def get_max(self):
        if len(self.max_items) == 0:
            return None
        return self.max_items[len(self.max_items) - 1]

