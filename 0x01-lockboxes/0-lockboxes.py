#!/usr/bin/python3
"""method for opening all locked boxes"""


def canUnlockAll(boxes):
    '''method to unlock the boxes'''
    opened = set([0])
    keys = boxes[0][:]

    while keys:
        key = keys.pop()
        if key not in opened and key < len(boxes):
            opened.add(key)
            keys.extend(boxes[key])
    return len(opened) == len(boxes)
