import psycopg2
from .config import config
 
def connect():
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
 
        # create a cursor
        cursor = connection.cursor()
        
 # execute a statement
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cursor.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    connect()