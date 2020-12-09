#!/usr/bin/python
from player import Player
from team import Team
from lane_assignments import LaneAssignment

if __name__ == "__main__":
    player1 = Player(player_name="Martin Nordahl Hansen", player_tag="Wunder",
        player_points_total=100)
    player2 = Player(player_name="Marcin Jankowski", player_tag="Jankos",
        player_points_total=75)
    player3 = Player(player_name="Rasmus Borregaard Winther", player_tag="Caps",
        player_points_total=125)
    player4 = Player(player_name="Luka Perkovic", player_tag="Perkz",
        player_points_total=200)
    player5 = Player(player_name="Mihael Mehle", player_tag="Mikyx",
        player_points_total=150)
    player6 = Player(player_name="Kristoffer Albao Lund Pedersen",
        player_tag="P1noy")
    team1 = Team(team_name="G2 Esports", team_tricode="G2",
        team_points_total=1000, team_points_watermark=1500,
        team_roster=[player1, player2, player3, player4, player5, player6])

    team1.__display__()

    '''
    Read the CSV File for Player and Team Base metrics on startup.
        - Read Team file first to create the base of teams which exist.
        - Then Read the Player file which will populate the previously empty
            Team class instances.
    '''