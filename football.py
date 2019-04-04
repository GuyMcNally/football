import requests
from db.postgres import connect

# connect()


def create_team(team):
    query = '''INSERT INTO teams(
        id, name, logo,
    )
    SELECT {0}, '{1}', '{2}'
    WHERE NOT EXISTS(SELECT id FROM teams WHERE id = {0});
    '''.format(team['team_id'], team['name'], team['logo'])
    connect(query)

# I've dropped code as there is no code in API. https://api-football-v1.p.rapidapi.com/teams/league/ 
# In fact I've had to use a league ID to get it to work, for ex 20 gives you this seasons premier league teams
# what I then tried to do was default the code to 2 but as I'm not so bright I couldn't figure it out. 
#team['code']

def create_teams(teams):
    for team in teams:
        create_team(teams[team])


# team = {"id": 999999998, "name": 'cats', "code": 'dogs', "logo": 'paw'}
# create_team(team)
# connect('SELECT * FROM teams;')


def create_league(league):
    query = """INSERT INTO leagues(
        id, name, country, country_code, season, season_start, season_end, logo, flag, standings
    )
    SELECT {0}, '{1}', '{2}', '{3}','{4}', '{5}', '{6}', '{7}', '{8}', {9}
    WHERE NOT EXISTS(SELECT id FROM leagues WHERE id = {0});
    """.format(league['league_id'], league['name'], league['country'], league['country_code'], league['season'], league['season_start'], league['season_end'], league['logo'], league['flag'], league['standings'])
    connect(query)


# league = {
#     "league_id": "112",
#     "name": " Super Lig",
#     "country": "Turkey",
#     "country_code": "TR",
#     "season": "2017",
#     "season_start": "2017-08-11",
#     "season_end": "2018-05-19",
#     "logo": "https://www.api-football.com/public/leagues/112.png",
#     "flag": "https://www.api-football.com/public/flags/tr.svg",
#     "standings": True
# }

# create_league(league)

def create_leagues(leagues):
    for league in leagues:
        create_league(leagues[league])


def get_leagues():
    response = requests.get("https://api-football-v1.p.rapidapi.com/leagues",  headers={
        "X-RapidAPI-Key": "xx"
    })
    body = response.json()
    print(body)
    leagues = body['api']['leagues']
    create_leagues(leagues)


#get_leagues()
#connect('SELECT * FROM leagues;')

def get_teams():
    response = requests.get("https://api-football-v1.p.rapidapi.com/teams/league/2",  headers={
        "X-RapidAPI-Key": "xx"
    })
    body = response.json()
    print(body)
    teams = body['api']['teams']
    create_teams(teams)

get_teams()
connect('SELECT * FROM teams;')
