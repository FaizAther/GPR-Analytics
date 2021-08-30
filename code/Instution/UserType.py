from enum import Enum
'''
    User Type
'''
class UserType(Enum):
    LECTURER    = 0
    TUTOR       = 1
    RESEARCHER  = 2   
    UNDERGRAD   = 3
    POSTGRAD    = 4
    PHD         = 5
    EXCHANGE    = 6
    DEFAULT     = 7