from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response
import json



HOST = 'localhost'

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
game_info = {
         "match_id": "xxx",
        "status": "None",
        "size" : "3", 
        "board": [[ "X"], ["O"], ["X" ], [" "], [" "], [" "], [" "], [" "], [" "]],
        "time1": "100", 
        "time2": "100", 
    "team1_id": "xx1", 
    "team2_id": "xx2",	
    "turn": "xx1", 
    "score1": "0",
    "score2": "0"
    }

@app.route('/init')
@cross_origin()
def get_data():
    return {
    "room_id":"xxx",
    "init": True}

@app.route('/', methods=['POST'])
@cross_origin()
def render_board():
    response = make_response(jsonify(game_info))
    print(response)
    return response

@app.route('/move', methods=['POST'])
@cross_origin()
def handle_move():
    data = request.data
    game_info.update(json.loads(data.decode('utf-8')))
    print(game_info)
    return 'ok'

if __name__ == '_main_':
    app.run(host="0.0.0.0")
