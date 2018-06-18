#!/usr/bin/env python3
# Author: GreatBahram
from random import choice

def informal_greeting():
    """
    Randomly return an informal greeting
    """

    greeting_messages = [
            "Hey, Hey man!",
            "How’s it going?",
            "What’s up?",
            "What’s going on?",
            "How’s life?",
            ]

    return choice(greeting_messages)

def formal_greeting():
    """
    Randomly return a formal greeting
    """

    greeting_messages = [
            "Good morning",
            "It’s nice to meet you",
            "How have you been?",
            "Pleased to meet you",
            "How have you been?",
            ]

    return choice(greeting_messages)
