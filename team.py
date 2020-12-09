#!/usr/bin/python
'''
@brief: Team Class used to track team metrics and contains references to player
    classes representing each player on the team.
'''
from player import Player
from enum import Enum
from game import Game

class Team:

    class ReturnStatus(Enum):
        TEAM_SUCCESS = 1
        TEAM_PLAYER_NOT_IN_ROSTER_GROUP = 2
        TEAM_ROSTER_GROUP_FULL = 3
        TEAM_ROSTER_GROUP_EMPTY = 4

    def __init__(self, team_name: str = "", team_tricode: str = "",
                 team_points_total: int = 0,
                 team_points_watermark: int = 0,
                 team_core: list = [], team_roster: list = [],
                 team_roster_active: list = [], team_roster_former: list = []):
        self.team_name = team_name
        self.team_tricode = team_tricode
        self.team_points_total = team_points_total
        self.team_points_watermark = team_points_watermark
        self.team_core = team_core
        self.team_roster = team_roster
        self.team_roster_active = team_roster_active
        self.team_roster_former = team_roster_former

    '''***************************TEAM NAME**********************************'''
    def set_team_name(self, team_name: str = "") -> ReturnStatus:
        self.team_name = team_name
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_name(self) -> (ReturnStatus, str):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_name)

    '''***************************TEAM TRICODE*******************************'''
    def set_team_tricode(self, team_tricode: str = "") -> ReturnStatus:
        self.team_tricode = team_tricode
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_tricode(self) -> (ReturnStatus, str):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_tricode)
    
    '''***********************TEAM POINTS TOTAL******************************'''
    def set_team_points_total(self, team_points_total: int = 0) -> ReturnStatus:
        self.team_points_total = team_points_total
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_points_total(self) -> (ReturnStatus, int):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_points_total)

    '''************************TEAM POINTS WATERMARK*************************'''
    def set_team_points_watermark(self, team_points_watermark: int = 0) \
        -> ReturnStatus:
        self.team_points_watermark = team_points_watermark
        return self.ReturnStatus.TEAM_SUCCESS
    
    def get_team_points_watermark(self) -> (ReturnStatus, int):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_points_watermark)

    '''***************************TEAM CORE**********************************'''
    def set_team_core(self, team_core: list = []) -> ReturnStatus:
        self.team_core = team_core
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_core(self) -> (ReturnStatus, list):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_core)

    def add_player_to_core(self, player: Player) -> ReturnStatus:

        # check that the core is not already full (3 players)
        if len(self.team_core) == 3:
            return self.ReturnStatus.TEAM_ROSTER_GROUP_FULL

        self.team_core.append(player)
        #TODO update core stats
        return self.ReturnStatus.TEAM_SUCCESS
    
    def remove_player_from_core(self, player: Player) -> ReturnStatus:
        
        # check to see if the roster is empty
        if len(self.team_core) == 0:
            return self.ReturnStatus.TEAM_ROSTER_GROUP_EMPTY
        
        # check if the selected player is in the core
        if self.team_core.count(player) <= 0:
            return self.ReturnStatus.TEAM_PLAYER_NOT_IN_ROSTER_GROUP

        # player reference found in core, now remove
        self.team_core.remove(player)
        #TODO upate core stats
        return self.ReturnStatus.TEAM_SUCCESS

    '''***************************TEAM ROSTER********************************'''
    def set_team_roster(self, team_roster: list = []) -> ReturnStatus:
        self.team_roster = team_roster
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_roster(self) -> (ReturnStatus, list):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_roster)

    def add_player_to_roster(self, player: Player) -> ReturnStatus:
        self.team_roster.append(player)
        #TODO Update all team based averages
        return self.ReturnStatus.TEAM_SUCCESS
    
    def remove_player_from_roster(self, player: Player) -> ReturnStatus:
        
        # check to see if the roster is empty
        if len(self.team_roster) == 0:
            return self.ReturnStatus.TEAM_ROSTER_GROUP_EMPTY

        # check for the player in all roster sets
        if self.team_roster.count(player) <= 0:
            return self.ReturnStatus.TEAM_PLAYER_NOT_IN_ROSTER_GROUP
        else:
            self.team_roster.remove(player)
        self.remove_player_from_core(player)
        self.remove_player_from_roster_active(player)
        #TODO update all team stats
        return self.ReturnStatus.TEAM_SUCCESS

    '''*********************TEAM ROSTER ACTIVE*******************************'''
    def set_team_roster_active(self, team_roster_active: list = []) \
        -> ReturnStatus:
        self.team_roster_active = team_roster_active
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_roster_active(self) -> (ReturnStatus, list):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_roster_active)

    def add_player_to_roster_active(self, player: Player) -> ReturnStatus:

        # check to see if the roster is full (5 players)
        if len(self.team_roster_active) == 5:
            return self.ReturnStatus.TEAM_ROSTER_GROUP_FULL
        self.team_roster.append(player)
        #TODO update active roster stats
        return self.ReturnStatus.TEAM_SUCCESS

    def remove_player_from_roster_active(self, player: Player) -> ReturnStatus:
        
        # check to see if the roster is empty
        if len(self.team_roster) == 0:
            return self.ReturnStatus.TEAM_ROSTER_GROUP_EMPTY
        self.team_roster_active.remove(player)
        #TODO update active roster stats
        return self.ReturnStatus.TEAM_SUCCESS

    '''*************************TEAM ROSTER FORMER***************************'''
    def set_team_roster_former(self, team_roster_former: list = []) \
        -> ReturnStatus:
        self.team_roster_former = team_roster_former
        return self.ReturnStatus.TEAM_SUCCESS

    def get_team_roster_former(self, team_roster_former: list = []) \
        -> (ReturnStatus, list):
        return (self.ReturnStatus.TEAM_SUCCESS, self.team_roster_former)

    '''*****************************UTILITIES********************************'''
    def update_game_stats(self, game: Game = None) -> (ReturnStatus, float):
        return (self.ReturnStatus.TEAM_SUCCESS, 0.0)

    def __display__(self):
        print("Team Name : ", self.team_name)
        print("Team Points : ", self.team_points_total)
        print("Roster : ")
        for player in self.team_roster:
            player.__display__()
