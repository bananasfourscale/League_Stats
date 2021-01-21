#!/usr/bin/python

from enum import Enum

class Match():

    class ReturnStatus(Enum):
        MATCH_SUCCESS = 1

    def __init__(self, games : list = []) -> ReturnStatus:
        self.games = games