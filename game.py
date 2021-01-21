#!/usr/bin/python

from enum import Enum
from team import Team

class Game():

    class ReturnStatus(Enum):
        GAME_SUCCESS = 1

    def __init__(self, game_id : str = "", teams : tuple = (None, None),
                 game_data : list = []) -> ReturnStatus:
        self.game_id = game_id
        self.teams = teams
        self.game_data = game_data
