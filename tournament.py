#!/usr/bin/python

from enum import Enum
from registered_tournaments import registered_tournaments
from datetime import datetime

class Tournament():

    class ReturnStatus(Enum):
        TOURNAMENT_SUCCESS = 1

    class TournamentLevel(Enum):
        AMATURE_LEAGUE = 1
        MINOR_LEAGUE = 2
        MAJOR_LEAGUE = 3
        MID_SEASON_INTERNATIONAL = 4
        WORLD_CHAMPIONSHIP = 5

    def __init__(self, games : list = [], tournament_name : str = 'LEC',
                 tournament_level : TournamentLevel = \
                     TournamentLevel.AMATURE_LEAGUE,
                 base_points : int = 100, start_date : datetime = None,
                 end_date : datetime = None, event_stages : list = [],
                 participant_count_per_stage : list = []):
        self.games = games
        self.tournament_name = tournament_name
        self.torunament_level = tournament_level
        self.base_points = base_points
        self.start_date = start_date
        self.end_date = end_date
        self.event_stages  = event_stages
        self.participant_count_per_stage = participant_count_per_stage

    def __display__(self):
        print("Tournament Name : ", self.tournament_name)
        print("Start Date : ", self.start_date)
        print("End Date : ", self.end_date)
if __name__ == "__main__":
    
