#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):    
    """check if all the boxes can be opened"""
    keyset = {0}

    for key in boxes[0]:
        if (0 <= key < len(boxes)) and key not in keyset:
            boxes[0].extend(boxes[key])
            keyset.add(key)

    return len(keyset) == len(boxes)