#!/usr/bin/python

from enum import Enum

class Tournament():

    class ReturnStatus(Enum):
        TOURNAMENT_SUCCESS = 1

    def __init__(self, games : list = []) :
        self.games = games
