#!/usr/bin/python
import csv
from enum import Enum
from utilities import conditional_print

registered_game_ids = []
registered_game_id_file_name = "statistical_ranking_database/archived_games.txt"

class GameParserReturnStatus(Enum):
    GP_SUCCESS = 1
    GP_INITIALIZATION_FAILURE = 2
    GP_ARCHIVE_UPDATE_FAILURE = 3

def initailize_registered_games(verbose : bool = False) \
                                                    -> GameParserReturnStatus:
    
    try:
    
        # open the archive of all previously parsed game IDs
        with open(registered_game_id_file_name, "r") as archived_game_id_file:

            # loop through all the game ids and add them to the registred list
            for game_id in archived_game_id_file:
                conditional_print(verbose, str(game_id))
                registered_game_ids.append(game_id)
    except Exception as e:
        conditional_print(verbose, str(e))
        return GameParserReturnStatus.GP_INITIALIZATION_FAILURE  
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
    print("Attempting to parse ", file_name)
    header_row = True
    try:

        # open the game data collection file
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
                    if verbose :
                        conditional_print(verbose, "Data Row")

                    # game ID parsing
                    game_id = game_section[0]
                    conditional_print(verbose, str(game_id))

                    # check if the game has already been parsed in a previous
                    # version of the file. If so add it now and parse the data
                    if registered_game_ids.count(game_id) == 0:
                        
                        conditional_print(verbose, "New ID")
                        update_registred_games(verbose, game_id)

                    # otherwise the game is already in the registred list,
                    # which should mean that the data within has already been
                    # taken into acount for team/player ratings
                    else:
                        conditional_print(verbose, "Old ID")
                        pass

    except Exception as e:
        print("Failed to parse ", file_name)
        raise e

if __name__ == "__main__":
    print("Parsing Test File")
    test_file_name = \
        "game_data/2021_LoL_esports_match_data_from_OraclesElixir_20210111.csv"
    parse_game_csv(True, test_file_name)

