import sqlite3
import json


class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        if exc_val:
            raise

    def sql_query(self, sql_request: str):
        print("Database current state: \n")
        print(self.conn.cursor().execute('SELECT * FROM USERS').fetchall())
        self.conn.execute(f'''{sql_request}''')
        with open("json_data.txt", "w+") as file:
            json.dump(conn.cursor().execute(f'{sql_request}').fetchall(), file)
            print("JSON format" + json.dumps(conn.cursor().execute(f'''{sql_request}''').fetchall()))

    def select(self, sql_request: str):
        self.sql_query(sql_request)

    def execute(self, sql_request: str):
        self.sql_query(sql_request)

    def delete(self, sql_request: str):
        self.sql_query(sql_request)

    def create_database(self, sql_request: str):
        self.sql_query(sql_request)

    def show_databases(self, sql_request: str):
        self.sql_query(sql_request)

    def drop_databases(self, sql_request: str):
        self.sql_query(sql_request)

    def show_tables(self, sql_request: str):
        self.sql_query(sql_request)

    def update(self, sql_request: str):
        self.sql_query(sql_request)

    def join(self, sql_request: str):
        self.sql_query(sql_request)

    def poslat_za_pivom(self, sql_request: str):
        self.sql_query(sql_request)

    def vinesti_musor(self, sql_request: str):
        self.sql_query(sql_request)

    def pogulyat_s_sobakoi(self, sql_request: str):
        self.sql_query(sql_request)

    def zabrat_detei_is_shkoli(self, sql_request: str):
        self.sql_query(sql_request)

    def shodit_v_magazin(self, sql_request: str):
        self.sql_query(sql_request)


if __name__ == '__main__':
    db = 'test_db.db'
    query = input("Input your sql query")

    with DataConn(db) as conn:
        que = DataConn(db)
        que.sql_query(sql_request='SELECT * FROM USERS WHERE AGE>25')
