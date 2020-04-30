import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home() :
    return "This is REST using python"

@app.route('/customers/details',  methods=['GET'])
def getCustDetais():
    db = sqlite3.connect('chinook.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    all_details = cur.execute('SELECT * FROM customers;').fetchall()

    return jsonify(all_details)

@app.route('/customers/filter',  methods=['GET'])
def getCustFilter():
    db = sqlite3.connect('chinook.db')
    db.row_factory = dict_factory
    cur = db.cursor()

    query_parameters = request.args
    state = query_parameters.get('state')
    country = query_parameters.get('country')

    query = 'SELECT * FROM customers WHERE'
    to_filter = []

    if state:
        query += ' State=? AND'
        to_filter.append(state)
    if country:
        query += ' Country=? AND'
        to_filter.append(country)  
    if not (state or country):
        return page_not_found(404)

    query = query[:-3] + ';'

    result = cur.execute(query, to_filter).fetchall()

    return jsonify(result)

@app.route('/artists/details',  methods=['GET'])
def getArtistDetais():
    db = sqlite3.connect('chinook.db')
    db.row_factory = dict_factory
    cur = db.cursor()
    all_details = cur.execute('SELECT * FROM artists;').fetchall()

    return jsonify(all_details)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


app.run()