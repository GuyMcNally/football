
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from scipy.stats import poisson, skellam
from db.postgres import connect_with_names

# connecting to the db
fixtures = connect_with_names('select * from fixtures;')

for fixture in fixtures:
    round_number = fixture['round'][-2:]
    if round_number != 'ls' and round_number != 'al':
        int_version = int(round_number)
        fixture['round'] = int_version
    else:
        fixture['round'] = 0


# converting database list to df
fixtures_df = pd.DataFrame(fixtures)

# reducing the database size
fixtures_reduced = fixtures_df[['id', 'event_date', 'league', 'round',
                                'home_team', 'away_team', 'goals_home_team', 'goals_away_team']]
fixtures_reduced_renamed = fixtures_reduced.rename(
    columns={'goals_home_team': 'HomeGoals', 'goals_away_team': 'AwayGoals'})

fixtures_reduced_renamed['event_date'] = pd.to_datetime(
    fixtures_reduced_renamed['event_date'])

# print(fixtures_reduced_renamed.head())
