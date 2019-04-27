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


def get_team_for_league(league_id):
    response = requests.get(f'https://api-football-v1.p.rapidapi.com/teams/league/{league_id}',
                            headers={
                                "X-RapidAPI-Key": "XXXX"
                            })
    body = response.json()
    print(body)
    teams = body['api']['teams']
    create_teams(teams)


# get_all_teams()
# connect('SELECT COUNT(*) FROM teams;')
