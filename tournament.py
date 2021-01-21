#!/usr/bin/python

from enum import Enum
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

    def __init__(self, matches : list = [], tournament_name : str = 'LEC',
                 tournament_level : TournamentLevel = \
                     TournamentLevel.AMATURE_LEAGUE,
                 base_points : int = 100, start_date : datetime = None,
                 end_date : datetime = None, event_stages : list = [],
                 participant_count_per_stage : list = []):
        self.matches = matches
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

registered_tournaments = {
    'BIG' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'BRCC' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'CBLOL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'CK' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'CU' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'DC' : {
        # TODO is demacia this level?
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'EM' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'KeSPA' : {
        # TODO is Kespa this level?
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LCK' : {
        'level' : Tournament.TournamentLevel.MAJOR_LEAGUE,
        'points' : 500,
    },
    'LCL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LCS' : {
        'level' : Tournament.TournamentLevel.MAJOR_LEAGUE,
        'points' : 500,
    },
    'LCS.A' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LDL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LEC' : {
        'level' : Tournament.TournamentLevel.MAJOR_LEAGUE,
        'points' : 500,
    },
    'LFL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LJL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LLA' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'LPL' : {
        'level' : Tournament.TournamentLevel.MAJOR_LEAGUE,
        'points' : 500,
    },
    'MSI' : {
        'level' : Tournament.TournamentLevel.WORLD_CHAMPIONSHIP,
        'points' : 1000,
    },
    'MSC' : {
        'level' : Tournament.TournamentLevel.MAJOR_LEAGUE,
        'points' : 500,
    },
    'NASG' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'NEST' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'NLC' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'OCS' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'OPL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'PCS' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'RCL' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'TCL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'TRA' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'UKLC' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'UL' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'UPL' : {
        'level' : Tournament.TournamentLevel.AMATURE_LEAGUE,
        'points' : 100,
    },
    'VCS' : {
        'level' : Tournament.TournamentLevel.MINOR_LEAGUE,
        'points' : 250,
    },
    'WCS' : {
        'level' : Tournament.TournamentLevel.MID_SEASON_INTERNATIONAL,
        'points' : 250,
    },
}


if __name__ == "__main__":
    pass
