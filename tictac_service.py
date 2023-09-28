from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from tictactoe_2 import TicTacToe2
import json
from player_controller import PlayerController
from game_match_controller import GameMatchController
from lobby_controller import LobbyController


app = Flask(__name__)
CORS(app)

p_controller = PlayerController()
g_controller = GameMatchController(p_controller)
l_controller = LobbyController(p_controller, g_controller)


@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res


@app.post("/signin/")
def signin():
    data = request.json
    response = p_controller.signin(data.get('email'), data.get('password'), data.get('nick_name'))
    if type(response) is str:
        return jsonify({'error': response})
    return jsonify(response.to_dict())


@app.post("/login/")
def login():
    data = request.json
    response = p_controller.login(data.get('email'), data.get('password'))
    if type(response) is str:
        return jsonify({'error': response})
    return jsonify(response.to_dict())


@app.get("/list-online-players")
def list_online_players():
    return jsonify(p_controller.get_all_online_players())


@app.get("/list-all-lobbies")
def list_all_lobbies():
    return jsonify(l_controller.get_all_lobbies())


@app.post("/create-lobby/")
def create_lobby():
    data = request.json
    return jsonify(l_controller.create_lobby(data.get('email')))


@app.post("/add-player-to-lobby")
def add_player_to_lobby():
    data = request.json
    return jsonify(l_controller.add_player_to_lobby(data['email'], data['lobby_id']))


@app.get("/update-matrix/<value>")
def update_matrix(value):
    game_id, x, y, in_x, in_y = value.split('-')
    game_match_dict = g_controller.play(game_id, x, y, in_x, in_y)
    return jsonify(game_match_dict)


@app.get("/start-game/<lobby_id>")
def start_game(lobby_id):
    l_controller.start_game(lobby_id)
    return json.dumps()


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
