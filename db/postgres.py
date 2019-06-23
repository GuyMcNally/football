import psycopg2
from .config import config


def connect(query):
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database... ')
        connection = psycopg2.connect(**params)
        connection.autocommit = True

        # create a cursor
        cursor = connection.cursor()

        # execute a statement
        print('QUERY:')
        print(query)
        cursor.execute(query)
        # display the PostgreSQL database server version
        result = cursor.fetchall()
        print(result)
        return result
     # close the communication with the PostgreSQL
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


def connect_with_names(query):
    """ Connect to the PostgreSQL database server """
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database... ')
        connection = psycopg2.connect(**params)
        connection.autocommit = True

        # create a cursor
        cursor = connection.cursor()

        # execute a statement
        print('QUERY:')
        # print(query)
        cursor.execute(query)
        column_names = [desc[0] for desc in cursor.description]
        # print(curs.description)
        # display the PostgreSQL database server version
        results = cursor.fetchall()
        # print(results)
        formatted_results = []

        for result in results:
            result_dict = {}
            for index, column in enumerate(column_names):
                result_dict[column] = result[index]
            formatted_results.append(result_dict)

        # print(formatted_results)
        return formatted_results
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
