from db.postgres import connect

# connect()

def create_team(team):
    query = '''INSERT INTO teams(
        id, name, code, logo
    )
    SELECT {0}, '{1}', '{2}', '{3}'
    WHERE NOT EXISTS(SELECT id FROM teams WHERE id = {0});
    '''.format(team['id'],team['name'], team['code'], team['logo'])
    connect(query)

def create_teams(teams):
    for team in teams:
        create_team(team)

#team = {"id": 999999998, "name": 'cats', "code": 'dogs', "logo": 'paw'}
#create_team(team)
connect('SELECT * FROM teams;')


def create_league(league):
    query = '''INSERT INTO leagues(
        id, name, country, country_code, season, season_start, season_end, logo, flag, standings
    )
    SELECT {0}, '{1}', '{2}', '{3}','{4}', '{5}', '{6}', '{7}', '{8}', {9}
    WHERE NOT EXISTS(SELECT id FROM leagues WHERE id = {0});
    '''.format(league['id'],league['name'], league['country'], league['country_code'], league['season'], league['season_start'], league['season_end'], league['logo'], league['flag'], league['standings'])
    connect(query)


# league = {"id" : 1234, "name": "Botswana Super League" ,"country" : "Botswana", "country_code" : "9999", "season" : "2010/11", "season_start" : "2018-08-22", "season_end" : "2019-03-01", "logo" : "Tree", "flag" : "NA", "standings" : False}
    
# create_league(league)

connect('SELECT * FROM leagues;')

def create_leagues(leagues):
    for league in leagues:
        create_league(league)
