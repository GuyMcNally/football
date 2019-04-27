import requests
import json
from db.postgres import connect


def create_team(team):
    query = '''INSERT INTO teams(
        id, name, code, logo
    )
    SELECT {0}, '{1}', '{2}', '{3}'
    WHERE NOT EXISTS(SELECT id FROM teams WHERE id = {0});
    '''.format(team['team_id'], team['name'], team['code'], team['logo'])
    connect(query)


def create_teams(teams):
    for team in teams:
        create_team(teams[team])


# with open('./data/pl_teams.json') as file:
#     body = json.load(file)
#     # print(body)
#     teams = body['api']['teams']
#     create_teams(teams)


def create_league(league):
    query = """INSERT INTO leagues(
        id, name, country, country_code, season, season_start, season_end, logo, flag, standings
    )
    SELECT {0}, '{1}', '{2}', '{3}','{4}', '{5}', '{6}', '{7}', '{8}', {9}
    WHERE NOT EXISTS(SELECT id FROM leagues WHERE id = {0});
    """.format(league['league_id'], league['name'], league['country'], league['country_code'], league['season'], league['season_start'], league['season_end'], league['logo'], league['flag'], league['standings'])
    connect(query)


def create_leagues(leagues):
    for league in leagues:
        create_league(leagues[league])


def get_leagues():
    response = requests.get("https://api-football-v1.p.rapidapi.com/leagues",
                            headers={
                                "X-RapidAPI-Key": "XXXX"
                            })
    body = response.json()
    print(body)
    leagues = body['api']['leagues']
    create_leagues(leagues)


def get_all_teams():
    leagues = connect('SELECT * FROM leagues;')
    for league in leagues:
        if league[2] == "England" and league[4] == "2018":
            get_team_for_league(league[0])


def create_fixtures(fixtures):
    for fixture in fixtures:
        create_fixture(fixtures[fixture])


def create_fixture(fixture):
    query = """INSERT INTO fixtures(
        id,
        event_date,
        event_timestamp,
        league,
        round,
        home_team,
        away_team,
        status,
        status_short,
        goals_home_team,
        goals_away_team,
        halftime_score,
        final_score,
        penalty, 
        elapsed
    )
    SELECT {0}, '{1}', '{2}', '{3}','{4}', '{5}', '{6}', '{7}', '{8}', {9}, '{10}', '{11}', '{12}', '{13}', '{14}'
    WHERE NOT EXISTS(SELECT id FROM fixtures WHERE id = {0});
    """.format(
        fixture['fixture_id'],
        fixture['event_date'],
        fixture['event_timestamp'],
        fixture['league_id'],
        fixture['round'],
        fixture['homeTeam_id'],
        fixture['awayTeam_id'],
        fixture['status'],
        fixture['statusShort'],
        fixture['goalsHomeTeam'],
        fixture['goalsAwayTeam'],
        fixture['halftime_score'],
        fixture['final_score'],
        fixture['penalty'],
        fixture['elapsed']
    )
    connect(query)


def get_fixture_for_league(league_id):
    response = requests.get(f'https://api-football-v1.p.rapidapi.com/fixtures/league/{league_id}',
                            headers={
                                "X-RapidAPI-Key": "XXXX"
                            })
    body = response.json()
    print(body)
    fixtures = body['api']['fixtures']
    create_fixtures(fixtures)


def get_all_fixtures():
    leagues = connect('SELECT * FROM leagues;')
    for league in leagues:
        if league[2] == "England" and league[4] == "2018":
            get_fixture_for_league(league[0])


def get_team_for_league(league_id):
    response = requests.get(f'https://api-football-v1.p.rapidapi.com/teams/league/{league_id}',
                            headers={
                                "X-RapidAPI-Key": "XXXX"
                            })
    body = response.json()
    print(body)
    teams = body['api']['teams']
    create_teams(teams)


# Use the below to populate all English Fixtures from 2018/19
# get_leagues()
# connect('SELECT * FROM leagues;')
# get_all_teams()
# connect('SELECT * FROM teams;')
# get_all_fixtures()
# connect('SELECT * FROM fixtures;')
