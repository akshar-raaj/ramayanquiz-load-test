import time
import sys
import psycopg2
import os


times = int(sys.argv[1])


def _create_connection():
    connection_string = os.environ['CONNECTION_STRING']
    try:
        connection = psycopg2.connect(connection_string)
    except psycopg2.OperationalError:
        return None
    return connection

def perform(times):
    connections = []
    st = time.time()
    for _ in range(times):
        connection = _create_connection()
        if connection is None:
            print("Probably unable to create connection")
            sys.exit(0)
        connections.append(connection)
        time.sleep(.1)
    end = time.time()
    print(f'Took {end-st} seconds to repeat {times} times.')


if __name__ == '__main__':
    perform(times)
