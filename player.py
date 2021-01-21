#!/usr/bin/python
'''
@brief: Player Class used to track player metrics and hold keys for filtering
    though the player statistical database.
'''

from enum import Enum

class Player:

    class ReturnStatus(Enum):
        PLAYER_SUCCESS = 1

    class LaneAssignment(Enum):
        TOP_LANE = 1,
        JUNGLE = 2,
        MID_LANE = 3,
        BOT_LANE = 4,
        SUPPORT = 5

    def __init__(self, player_name: str = "", player_tag: str = "",
                 player_points_total: int = 0,
                 player_role: LaneAssignment = LaneAssignment.MID_LANE,
                 player_rating: float = 0.0):
        self.player_name = player_name
        self.player_tag = player_tag
        self.player_points_total = player_points_total
        self.player_role = player_role
        self.player_rating = player_rating

    '''***************************PLAYER NAME********************************'''
    def set_player_name(self, player_name: str = "") -> ReturnStatus:
        self.player_name = player_name
        return self.ReturnStatus.PLAYER_SUCCESS

    def get_player_name(self) -> (ReturnStatus, str):
        return (self.ReturnStatus.PLAYER_SUCCESS, self.player_name)

    '''***************************PLAYER TAG*********************************'''
    def set_player_tag(self, player_tag: str = "") -> ReturnStatus:
        self.player_tag = player_tag
        return self.ReturnStatus.PLAYER_SUCCESS

    def get_player_tag(self) -> (ReturnStatus, str):
        return (self.ReturnStatus.PLAYER_SUCCESS, self.player_tag)

    '''***************************PLAYER POINT TOTAL*************************'''
    def set_player_points_total(self, player_points_total: int = 0) \
                                                                -> ReturnStatus:
        self.player_points_total = player_points_total
        return self.ReturnStatus.PLAYER_SUCCESS

    def get_player_points_total(self) -> (ReturnStatus, int):
        return (self.ReturnStatus.PLAYER_SUCCESS, self.player_points_total)

    def update_player_points(self, points_gained) -> (ReturnStatus, int):
        self.player_points_total += points_gained * 1
        return (self.ReturnStatus.PLAYER_SUCCESS, self.player_points_total)

    '''***************************PLAYER TAG*********************************'''
    def set_player_role(self, player_role: \
                            LaneAssignment = LaneAssignment.MID_LANE) \
                                                                -> ReturnStatus:
        self.player_role = player_role
        return self.ReturnStatus.PLAYER_SUCCESS

    def get_player_role(self) -> (ReturnStatus, LaneAssignment):
        return (self.ReturnStatus.PLAYER_SUCCESS, self.player_role)

    '''**************************PLAYER RATING*******************************'''
    def set_player_rating(self, rating: float = 0.0) -> ReturnStatus:
        self.player_rating = rating
        return self.ReturnStatus.PLAYER_SUCCESS

    def get_player_rating(self) -> (ReturnStatus, float):
        return (self.ReturnStatus.PLAYER_SUCCESS, self.player_rating)

    def update_player_rating(self, player_stats: dict = {}) -> ReturnStatus:
        return self.ReturnStatus.PLAYER_SUCCESS

    '''*****************************UTILITIES********************************'''
    def __display__(self):
        print("Player Name : ", self.player_name)
        print("Player Tag : ", self.player_tag)
        print("Player Ranking Points : ", self.player_points_total)
    
