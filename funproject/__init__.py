"""
FunProject
--------
This application designed for Python Packaging Tutorial.

Python is fun.

How to run it:
    funproject formal # going to help you
    funproject informal # going to help you
"""

__author__ = 'Bahram Aghaei'
__email__ = "aghaee.bahram@gmail.com"
__version__ = '0.1.0'

from .core import formal_greeting, informal_greeting

__all__ = [
        'formal_greeting', 'informal_greeting',
        ]
