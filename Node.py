class Node:

    def __init__(self):
        self.__value = None
        self.__next = None
        self.__prev = None
        self.__index = None

    def set_value(self, value):
        self.__value = value

    def set_next(self, next_node):
        self.__next = next_node

    def set_prev(self, prev_node):
        self.__prev = prev_node

    def set_index(self, index):
        self.__index = index

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_index(self):
        return self.__index
