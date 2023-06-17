import psycopg2
from os import environ


class Postgres:
    connection = None

    @staticmethod
    def connect():
        if (Postgres.connection is not None):
            print("Already Connected!")
            return

        try:

            print('Connecting to the PostgreSQL database...')
            Postgres.connection = psycopg2.connect(
                host=environ.get("DATABASE_HOST"),
                database=environ.get("DATABASE_NAME"),
                user=environ.get("DATABASE_USER"),
                password=environ.get("DATABASE_PASSWORD")
            )

            cur = Postgres.connection.cursor()

            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            db_version = cur.fetchone()
            print(db_version)

            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if Postgres.connection is not None:
                return Postgres.connection
