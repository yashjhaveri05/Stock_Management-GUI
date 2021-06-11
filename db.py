import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)  # to connect to the database
        self.cur = self.conn.cursor()  # used to execute queries
        # to execute query and create a table with the required fields if not already made.
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY, stock text, transtype text, number text, price text)")
        self.conn.commit()
    # sets connection,cursor,sql query to create a table

    def fetch(self):  # to fetch the data
        self.cur.execute("SELECT * FROM stocks")
        rows = self.cur.fetchall()
        return rows

    def insert(self, stock, transtype, number, price):
        self.cur.execute("INSERT INTO stocks VALUES (NULL, ?, ?, ?, ?)",
                         (stock, transtype, number, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM stocks WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, stock, transtype, number, price):
        print(self.cur.fetchall())
        self.cur.execute("UPDATE stocks SET stock=?, transtype=?, number=?, price=? WHERE id=?",
                         (stock, transtype, number, price, id))
        self.conn.commit()


def __del__(self):
    self.conn.close()
