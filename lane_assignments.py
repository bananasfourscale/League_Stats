#!/usr/bin/python
'''
@brief: Enumeration representing the 5 nomative roles in the game
'''

from enum import Enum

class LaneAssignment(Enum):
        TOP_LANE = 1,
        JUNGLE = 2,
        MID_LANE = 3,
        BOT_LANE = 4,
        SUPPORT = 5