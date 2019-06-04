import sqlite3 as sql

def database():
    conn=sql.connect('emp_database.db')
    conn2=sql.connect('stk_database.db')

    conn.execute(' CREATE TABLE IF NOT EXISTS employes (name TEXT ,password INT, addr TEXT , city TEXT , pin TEXT)')
    conn2.execute('CREATE TABLE IF NOT EXISTS stocks(id INT , item TEXT , quantity INT)')

    conn.close()
    conn2.close()
