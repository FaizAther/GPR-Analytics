from enum import Enum

'''
    Event Type
'''
class EventType(Enum):
    LECTURE         = 0
    TUTORIAL        = 1
    PRACTICAL       = 2

    ASSIGNMENT      = 3
    PROJECT         = 4
    EXAM            = 5

    CONSULTATION    = 6
    GUEST           = 7
    DEFAULT         = 8
