from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/read_top_hashtags_with_influencers")
def read_top_hashtags_with_influencers():
    data = [{"name": "#lebanon", "data": [{"name": "jamil_sayed", "value": 1000}, {"name": "riad", "value": 3}]},
            {"name": "#لبنان", "data": [{"name": "dima", "value": 50}, {"name": "ali.zien", "value": 5}]}]

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

