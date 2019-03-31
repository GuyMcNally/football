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

#team = {"id": 999999998, "name": 'cats', "code": 'dogs', "logo": 'paw'}
#create_team(team)
connect('SELECT * FROM teams;')

