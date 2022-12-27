#!/usr/bin/python3

"""Singly linked list module"""


class Node:
    """Represents a node of a singly linked list.

    Attributes:
        __data (int): The data of the node.
        __next_node(Node): The next node after the current one.
    """

    def __init__(self, value, next_node=None):
        self.data = value
        self.next_node = next_node

    @property
    def data(self):
        """data property getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data property setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node porperty getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node=None):
        """next_node property setter"""
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """Instantiates an empty SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """Allows to uses a node as a string. e.g: to print int."""
        text = ""
        tmp = self.__head
        while tmp is not None:
            text += "{:d}".format(tmp.data)
            text += "" if tmp.next_node is None else "\n"
            tmp = tmp.next_node
        return (text)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted
        position in the list (increasing order)

        Args:
            value (int): The data value of the new node.
        """
        node = Node(value)
        if self.__head is None:
            self.__head = node
            return

        if value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return

        tmp = self.__head
        while tmp.next_node is not None and value > tmp.next_node.data:
            tmp = tmp.next_node

        tmp1 = tmp.next_node
        tmp.next_node = node
        node.next_node = tmp1
