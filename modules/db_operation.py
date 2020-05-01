
import sqlite3

def db_startup():

    # looking into relative path from current path, then connect to database
    dbPath = 'data_source/chinook.db'

    # connect to database
    db = sqlite3.connect(dbPath)

    db.row_factory = dict_factory
    return db.cursor()

def db_query_run(query, filters):
    # looking into relative path from current path, then connect to database
    dbPath = 'data_source/chinook.db'

    # connect to database
    db = sqlite3.connect(dbPath)

    db.row_factory = dict_factory
    cur = db.cursor()

    result = ''

    if not filters :
        result = cur.execute(query).fetchall()
    else :
        result = cur.execute(query, filter).fetchall()

    db.close()

    return result
    

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d