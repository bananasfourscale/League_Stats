#!/usr/bin/python
import csv
from enum import Enum
from utilities import conditional_print

from year import Year
from tournament import Tournament
from tournament import registered_tournaments
from match import Match
from game import Game
from team import Team
from player import Player

# file scope list of all previously encountered game data IDs. This allows the
# ingestion of updated game data sets which will include all previously parsed
# data for that year. 
registered_game_ids = []
registered_game_id_file_name = "statistical_ranking_database/archived_games.txt"

# file scope list of all the new game IDs which were encountered this run.
# This allows multi game series to be grouped together and recognition that
# there are 12 rows of data related to one game.
newly_registred_game_ids = []

# registered player object references
registered_players = {}

# list of player IDs used as the keys to the registred player dictionary
registred_player_ids = registered_players.keys()

# registered team object references
registred_teams = {}

# list of team IDs used as the keys to the registred team dictionary
registered_team_ids = registred_teams.keys()

# integer to group all leagues which take place in the same year
current_year = None

# tournament class identifier used to group all matches in the same league
current_league = None

# match class identifier used to group all games in the same match
current_match = None

# game class identifier used to group all data rows associated with one game
current_game = None

class GameParserReturnStatus(Enum):
    GP_SUCCESS = 1
    GP_INITIALIZATION_FAILURE = 2
    GP_ARCHIVE_UPDATE_FAILURE = 3

class ColumnHeaders(Enum):
    GAME_ID = 0
    LEAGUE = 3
    YEAR = 4
    DATE = 7
    GAME_NUM = 8
    PATCH_NUM = 9
    PLAYER_ID = 10
    SIDE = 11
    LANE_POS = 12
    PLAYER_NAME = 13
    TEAM_NAME = 14
    CHAMP_PLAYED = 15
    BAN_1 = 16
    BAN_2 = 17
    BAN_3 = 18
    BAN_4 = 19
    BAN_5 = 20
    GAME_LEN = 21
    WIN_LOSS = 22
    KILLS = 23
    DEATHS = 24
    ASSIST = 25
    TEAMKILLS = 26
    TEAMDEATHS = 27
    DOUBLES = 28
    TRIPLES = 29
    QUADRAS = 30
    PENTAS = 31
    FIRST_BLOOD = 32
    FIRST_BLOOD_KILL = 33
    FIRST_BLOOD_ASSIST = 34
    FIRST_BLOOD_VICTIM = 35
    TEAM_KILLS_P_MIN = 36
    CKPM = 37
    FIRST_DRAG = 38
    TOTAL_DRAGS = 39
    OPPONET_DRAKES = 40
    ELEMENTAL_DRAKES = 41
    OPP_ELEM_DRAKES = 42
    INFERNALS = 43
    MOUNTAINS = 44
    CLOUDS = 45
    OCEANS = 46
    ELDERS = 48
    OPP_ELDERS = 49
    FIRST_HERALD = 50
    TOTAL_HERALDS = 51
    OPP_HERALDS = 52
    FIRST_BARON = 53
    TOTAL_BARONS = 54
    OPP_BARONS = 55
    FIRST_BRICK = 56
    TOTAL_TOWERS = 57
    OPP_TOWERS = 58
    FIRST_MID_TOWER = 59
    FIRST_TO_THREE_TOWERS = 60
    TOTAL_INHIBS = 61
    OPP_INHIBS = 62
    DAMAGE_TO_CHAMPS = 63
    DAMAGE_PER_MIN = 64
    DAMAGE_SHARE = 65
    DAMAGE_TAKEN_PER_MIN = 66
    DAMAGE_MITIGATED_PER_MIN = 67
    WARDS_PLACED = 68
    WARDS_PER_MIN = 69
    WARDS_KILLED = 70
    WCPM = 71
    TOTAL_GOLD = 72
    EARNED_GOLD = 73
    EARNED_GOLD_PER_MIN = 74
    EARNED_GOLD_SHARE = 75
    GOLD_SPENT = 76
    GSPD = 77
    TOTAL_CS = 78
    MINION_KILLS = 79
    MONSTER_KILLS = 80
    MONSTER_OWN_JNG = 81
    MONSTER_ENEMY_JNG = 82
    CS_PER_MIN = 83
    GOLD_AT_10 = 84
    XP_AT_10 = 85
    CS_AT_10 = 86
    OPP_GOLD_AT_10 = 87
    OPP_XP_AT_10 = 88
    OPP_CS_AT_10 = 89
    KILLS_AT_10 = 90
    ASSIST_AT_10 = 91
    DEATHS_AT_10 = 92
    OPP_KILLS_AT_10 = 93
    OPP_ASSIST_AT_10 = 94
    OPP_DEATH_AT_10 = 95
    GOLD_AT_15 = 96
    XP_AT_15 = 85
    CS_AT_16 = 86
    OPP_GOLD_AT_15 = 87
    OPP_XP_AT_15 = 88
    OPP_CS_AT_15 = 89
    KILLS_AT_15 = 90
    ASSIST_AT_15 = 91
    DEATHS_AT_15 = 92
    OPP_KILLS_AT_15 = 93
    OPP_ASSIST_AT_15 = 94
    OPP_DEATH_AT_15 = 95

def initailize_registered_games(verbose : bool = False) \
                                                    -> GameParserReturnStatus: 
    try:
    
        # open the archive of all previously parsed game IDs
        with open(registered_game_id_file_name, "r") as archived_game_id_file:

            # loop through all the game ids and add them to the registred list
            for game_id in archived_game_id_file:
                conditional_print(verbose, str(game_id))
                registered_game_ids.append(game_id.strip('\n'))
    except Exception as e:
        conditional_print(verbose, str(e))
        return GameParserReturnStatus.GP_INITIALIZATION_FAILURE

    conditional_print(verbose, registered_game_ids)  
    return GameParserReturnStatus.GP_SUCCESS

def update_registred_games(verbose : bool = False, game_id : str = "") \
                                                    -> GameParserReturnStatus:

    try :
        # open the registred games list

        with open(registered_game_id_file_name, "a") as archived_game_id_file:
            conditional_print(verbose, game_id)
            archived_game_id_file.write(game_id)
            archived_game_id_file.write("\n")
            registered_game_ids.append(game_id)
    except Exception as e:
        conditional_print(verbose, str(e))
        return GameParserReturnStatus.GP_ARCHIVE_UPDATE_FAILURE
    return GameParserReturnStatus.GP_SUCCESS

def parse_game_csv(verbose : bool = False, file_name : str = "") \
                                                    -> GameParserReturnStatus:
    # function scope error indicator
    return_status = None

    # boolean used to indicate if the current row being read is the header
    header_row = True

    try:
        
        # open the game data collection file
        conditional_print(verbose, "Attempting to parse" + file_name)
        with open(file_name, newline='') as game_data_file:
            game_parser = csv.reader(game_data_file, delimiter = ',')

            # loop through the lines of file
            for game_section in game_parser:

                # if this is hte header row, then ignore
                if header_row is True:
                    conditional_print(verbose, "Header Row")
                    header_row = False

                # otherwise pull out the data
                else:
                    
                    conditional_print(verbose, "Data Row")

                    # check the game ID to know if we should parse this set of
                    # data or just skip to the next game
                    game_id = game_section[ColumnHeaders.GAME_ID.value]

                    # check if the game has already been parsed in a previous
                    # version of the file. If so add it now and parse the data
                    if registered_game_ids.count(game_id) == 0:
                        
                        # start by updating the list of parsed games
                        conditional_print(verbose, "New ID " + str(game_id))
                        update_registred_games(verbose, game_id)
                        newly_registred_game_ids.append(game_id)

                        # if the player name is not registred, make a new object
                        # to to store reference information
                        if registred_player_ids.count(
                            game_section[ColumnHeaders.PLAYER_NAME.value]) == 0:

                            # Create a new player object, immediately adding it
                            # to the list of referenced players
                            registered_players[
                                game_section[ColumnHeaders.PLAYER_NAME.value]] =\
                                Player(
                                    player_tag=game_section[
                                        ColumnHeaders.PLAYER_NAME.value],

                                    # The first line of each game data set is
                                    # the top laner
                                    player_role=Player.LaneAssignment.TOP_LANE,
                                )

                        # if the team name is not registered, make a new object
                        # to score the reference information
                        if registered_team_ids.count(
                            game_section[ColumnHeaders.TEAM_NAME.value]) == 0:

                            # create a new Team object immediately adding it to
                            # the list of referenced teams
                            registred_teams[
                                game_section[ColumnHeaders.TEAM_NAME.value]] =\
                                Team(
                                    team_name=game_section[
                                        ColumnHeaders.TEAM_NAME.value],
                                    team_roster=[registered_players[
                                        game_section[
                                            ColumnHeaders.PLAYER_NAME.value]]]                                    
                                )

                        # construct a new game object referencing this new data
                        current_game = Game()

                        # contruct a new player if not registred


                    # otherwise the game is already in the registred list,
                    # which should mean that the data within has already been
                    # taken into acount for team/player ratings
                    else:
                        conditional_print(verbose, "Old ID " + str(game_id))

                        # check the list of games that were just registered this
                        # run. If this game is in that list, then we need to
                        # collect all the rows which correspond to one game
                        if newly_registred_game_ids.count(game_id) > 0:
                            
                            # add new teams if these teams have not been
                            # registerered already. A 100 or 200 in the player
                            # id section indicates Team data
                            if game_section[ColumnHeaders.PLAYER_ID.value] \
                                == 100:
                                pass

                            # add new players to the teams if they have not
                            # been registred. 1-10 in the player id section
                            # indicates Player data
                            if game_section[ColumnHeaders.PLAYER_ID.value] < 10:
                                pass

                        # otherwise this is data that has already been fully
                        # handled on a previous run, so just skill the row
                        else:
                            continue

    except Exception as e:
        print("Failed to parse ", file_name)
        raise e

def update_year(game_data : list = []) -> Year.ReturnStatus:

    # if the current year is none, then we are at the top of a data set and
    # there is no current year being tracked. Make one                                                
    if current_year is None:
        current_year = Year(year_str=game_data[ColumnHeaders.GAME_ID.value],
            year_int=int(game_data[ColumnHeaders.GAME_ID.value]))
        return Year.ReturnStatus.YEAR_SUCCESS

    # if the year given is equal to the current year check stages
    if game_data[ColumnHeaders.GAME_ID.value] == current_year.year_str:

        # TODO find a way to build in stages of a tournament
        return Year.ReturnStatus.YEAR_SUCCESS

    # otherwise, we are at the end of the data set for the previous year.
    # Record all required year end data gathered.
    else:
        pass

def update_league(game_data : list = []) -> Tournament.ReturnStatus:

    # if the current league is none, then we are at the top of a data set and
    # there is no current league being tracked. Make one
    if current_league is None:
        current_league = Tournament(
            tournament_name=game_data[ColumnHeaders.GAME_ID.value],
            tournament_level=registered_tournaments[
                game_data[ColumnHeaders.GAME_ID.value]]['level'],
            base_points=registered_tournaments[
                game_data[ColumnHeaders.GAME_ID.value]]['points'],
            start_date=game_data[ColumnHeaders.DATE.value],
        )
        return Tournament.ReturnStatus.TOURNAMENT_SUCCESS

    # if the current league does not match the previous league, set end date
    if current_league.tournament_name == game_data[ColumnHeaders.LEAGUE.value]:
        current_league.end_date=game_data[ColumnHeaders.DATE.value]
        current_year.tournaments.append(current_league)

    # other wise update the current tournament
    else:

        # TODO update tournament with any relavent game data
        pass
    return Tournament.ReturnStatus.TOURNAMENT_SUCCESS

def update_match(game_data : list = []) -> Match.ReturnStatus:
    if current_match is None:
        current_match = Match()
        return Match.ReturnStatus.MATCH_SUCCESS

    
    return Match.ReturnStatus.MATCH_SUCCESS

if __name__ == "__main__":
    print("Parsing Test File")
    initailize_registered_games(False)
    test_file_name = \
        "game_data/2021_LoL_esports_match_data_from_OraclesElixir_20210111.csv"
    parse_game_csv(True, test_file_name)

