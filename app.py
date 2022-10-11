from unittest import result
from apihelper import check_endpoint_info
import dbhelper
from flask import Flask, request, make_response
import json


app = Flask (__name__)

@app.post('/api/hero')
def insert_a_hero():
    invalid = check_endpoint_info(request.json, ['hero_name', 'hero_bio', 'hero_image'])
    if(invalid != None):
        return make_response(json.dumps(invalid), 400)

    results = dbhelper.run_statment('CALL insert_hero(?,?,?)',
     [request.json.get('hero_name'), request.json.get('hero_bio'), request.json.get('hero_image')])
    if(type(results) == list):
        return make_response(json.dumps(results, default=str), 200)
    else:
        return make_response(json.dumps(results, default=str), 400)

app.run(debug=True)