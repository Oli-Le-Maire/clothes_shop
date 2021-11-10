import psycopg2
from config import config
from connect import Connect_to_db

class Stock():

    def create_table(self):
        Connect_to_db().connect()

    def row_to_add_in_stock(self, item, price):
        row_to_add = (item, price)
        self.insert_stock(row_to_add)

    def insert_stock(self, row_to_add):
        """ insert new clothes into the table as a row"""
        sql = """INSERT INTO current_stock (
            item, price
        )
        VALUES ((%s), (%s))
        RETURNING item;"""

        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (row_to_add))
            id = cur.fetchone()[0]
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()


    def remove_chosen_item_from_stock(self, item):
        """ take away clothes from the table as a row"""
        sql = """DELETE FROM current_stock WHERE item = item
            RETURNING item;;"""

        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (item))
            id = cur.fetchone()[0]
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

    def check_current_stock(self, inserted_item):
        """ return clothes from the table as a row"""
        sql = """SELECT * FROM current_stock WHERE item = (%s);"""

        conn = None

        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql, (inserted_item, ))
            queried_item = cur.fetchone()
            conn.commit()
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

        return self.checked_item(queried_item)

    def checked_item(self, queried_item):
        if queried_item == None:
            return (queried_item, False)
        else:
            return (queried_item, True)
