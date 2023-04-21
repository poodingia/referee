from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
game_info = {
    "room_id": "xxx",
    "match_id": "xxx",
    "status": "None",
    "size": "3",
    "board": [["X"], ["O"], ["X"], [" "], [" "], [" "], [" "], [" "], [" "]],
    "time1": "100",
    "time2": "100",
    "team1_id": None,
    "team2_id": None,
    "turn": "xx1",
    "score1": "0",
    "score2": "0"
}


@app.route('/init', methods=['POST'])
@cross_origin()
def get_data():
    data  = request.data
    info = json.loads(data.decode('utf-8'))
    if game_info["team1_id"] is None:
        game_info["team1_id"] = info["team_id"]
    else:
        game_info["team2_id"] = info["team_id"]
        game_info["turn"] = info["team_id"]
    return {
        "room_id": "xxx",
        "match_id": "xx1",
        "init": True, 
        }


@app.route('/', methods=['POST'])
@cross_origin()
def render_board():
    # Code này để đổi lượt chơi nhưng đang cho một đội chơi liên tục
    # if game_info["turn"] == game_info["team1_id"]:
    #     game_info["turn"] = game_info["team2_id"]
    # elif game_info["turn"] == game_info["team2_id"]:
    #     game_info["turn"] = game_info["team1_id"]
    response = make_response(jsonify(game_info))
    print(game_info)
    return response


@app.route('/move', methods=['POST'])
@cross_origin()
def handle_move():
    data = request.data
    game_info.update(json.loads(data.decode('utf-8')))
    print(game_info)
    return 'ok'
