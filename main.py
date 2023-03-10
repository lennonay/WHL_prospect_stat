from roster import roster
from scraper import game_scrape
from pre_processing import stats_process
from datetime import datetime
import pandas as pd

if __name__ == "__main__":

    today = datetime.today().strftime('%Y-%m-%d')

    start_game_id = 1018603 + 1
    end_game_id = 1018603 + 537

    game_info = game_scrape(start_game_id, end_game_id)

    game_info.to_csv('data/whl_game_info_{start}_to_{end}.csv'.format(start = start_game_id, end = end_game_id-1),index=False)

    #roster_df = pd.read_csv('data/roster_2023-02-05.csv')

    roster_df = roster()
    
    roster_df.to_csv('data/roster_{date}.csv'.format(date = today),index=False)

    game_info_dob = pd.merge(game_info,roster_df, on = ['player_id','first_name','last_name'], how = 'left')

    output = stats_process(game_info_dob)

    output.to_csv('data/whl_game_{start}_to_{end}.csv'.format(start = start_game_id, end = end_game_id-1),index=False)