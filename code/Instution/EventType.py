from enum import Enum

'''
    Event Type
'''
class EventType(Enum):
    LECTURE         = 0
    TUTORIAL        = 1
    PRACTICAL       = 2
    CONSULTATION    = 3
    GUEST           = 4
    EXAM            = 5
    DEFAULT         = 6
