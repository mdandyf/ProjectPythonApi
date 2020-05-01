from modules.db_operation import db_startup, db_query_run

def fetchall_customer_detail():
    return db_query_run('SELECT * FROM customers;', [])

def fetch_customer_by_filter(state, country):
     cur = db_startup()

     query = 'SELECT * FROM customers WHERE'
     to_filter = []

     if state:
         query += ' State=? AND'
         to_filter.append(state)
     if country:
         query += ' Country=? AND'
         to_filter.append(country)  
     if not (state or country):
         raise Exception('Not Found')

     query = query[:-3] + ';'

     return cur.execute(query, to_filter).fetchall()