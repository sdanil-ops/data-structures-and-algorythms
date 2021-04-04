#  -----------------------------------------------------------
#
#  Python linked list data structure realisation
#
#  Copyright (c) 2021. Danil Smirnov
#  Released under GNU Public License (GPL)
#  email zabanen.nu@ya.ru
#  -----------------------------------------------------------

class Node:
    def __init__(self, item=None, next_element=None):
        self.item = item
        self.next = next_element

    def __str__(self):
        return 'Node [' + str(self.item) + ']'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def contains(self, item):
        last_node = self.head
        while last_node:
            if item == last_node.item:
                return True
            last_node = last_node.next
        return False

    def add(self, item):
        self.length += 1
        if self.head is None:
            self.head = Node(item, None)
            self.tail = self.head
        elif self.tail == self.head:
            self.tail = Node(item, None)
            self.head.next = self.tail
        else:
            current = Node(item, None)
            self.tail.next = current
            self.tail = current

    def push(self, item):
        self.length += 1
        if self.head is None:
            self.tail = self.head = Node(item, None)
        else:
            self.head = Node(item, self.head)

    def insert(self, position, item):
        if self.head is None:
            self.tail = self.head = Node(item, None)
            return
        if position == 0:
            self.head = Node(item, self.head)
            return
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            if counter == position:
                current.next = Node(item, current.next)
                if current.next is None:
                    self.tail = current.next
                break
            current = current.next

    def search(self, item):
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next
        return False



    def __str__(self):
        if self.head is not None:
            current = self.head
            out = 'LinkedList [ ' + str(current.item) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.item) + ' '
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        self.__init__()
