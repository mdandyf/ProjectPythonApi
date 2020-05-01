import flask
from flask import request, jsonify
import json

from modules.db_operation import db_startup, db_query_run
from modules.customer import fetchall_customer_detail, fetch_customer_by_filter
from modules.employee import fetchall_employee_detail
from modules.artist import fetchall_artist_detail

# getting flask and put into the app for running API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# all API controller sections
@app.route('/', methods=['GET'])
def home() :
    return "This is REST using python"

@app.route('/customers/details',  methods=['GET'])
def fetch_customers():
    result = fetchall_customer_detail()
    return jsonify(result)

@app.route('/customers/filter',  methods=['GET'])
def fetch_customers_filter():
    # Getting data from query parameters
    query_parameters = request.args
    state = query_parameters.get('state')
    country = query_parameters.get('country')

    try:
        # when data successfully found, return json
        result = fetch_customer_by_filter(state, country)
        return jsonify(result)
    except:
        # when data has not found, return html
        return page_not_found(404)

@app.route('/artists/details',  methods=['GET'])
def fetch_artists():
    result = fetchall_artist_detail()
    return jsonify(result)

@app.route('/employees/details',  methods=['GET'])
def fetch_employees():
    result = fetchall_employee_detail()
    return jsonify(result)

# all API error handler sections 
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()