from modules.db_operation import db_startup, db_query_run

def fetchall_artist_detail():
    return db_query_run('SELECT * FROM artists;', [])