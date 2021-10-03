from enum import Enum

'''
    User Type
'''
class UserType(Enum):
    LECTURER    = 0
    TUTOR       = 1
    RESEARCHER  = 2
    STUDENT     = 3
    UNDERGRAD   = 4
    POSTGRAD    = 5
    PHD         = 6
    EXCHANGE    = 7

    ADMIN       = 8
    SUDO        = 9
    DEFAULT     = 10