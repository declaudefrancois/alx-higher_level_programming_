#!/usr/bin/python3
"""
    Locked class module.
"""


class LockedClass:
    """
        Locked class.
        Prevents the user from dynamically
        creating new instance attributes,
        except if the new instance attribute
        is called first_name.

        Attributes:
            first_name (string): first name.
    """

    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        """
            Initialize a new instance.

            Args:
                first_name (string): first name.
        """
        self.first_name = first_name
