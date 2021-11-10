import psycopg2
from config import config

class Connect_to_db():

    def connect(self):
        """ Create tables in the PostgreSQL database server """
        commands = (
                """
                CREATE TABLE current_stock (
                    Unique_Key serial PRIMARY KEY,
                    Item VARCHAR(100) NOT NULL,
                    Price REAL NOT NULL
                );
                """)

        conn = None
        try:
            params = config()

            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            cur = conn.cursor()

            for command in commands:
                cur.execute(commands)

            cur.close()

            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')


if __name__ == '__main__':
    connect()
