#!/usr/bin/python

from enum import Enum
from team import Team
class Game():

    class ReturnStatus(Enum):
        GAME_SUCCESS = 1

    def __init__(self, teams: tuple(Team, Team)) -> ReturnStatus:
        self.teams = teams
