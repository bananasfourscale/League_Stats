#!/usr/bin/python

from enum import Enum

class Year():
    
    class ReturnStatus(Enum):
        YEAR_SUCCESS = 1

    def __init__(self, tournaments : list = [], year_str : str = '2020',
                 year_int : int = 2020):
        self.tournaments = tournaments
        self.year_str = year_str
        self.year_int = year_int