from flask import Blueprint, render_template, request
import requests

games = Blueprint('games', __name__,
                        url_prefix='/games',
                        template_folder='templates',
                        static_folder='static', static_url_path='static/games')

# ---------------------------------------

@games.route('/tic-tac-toe/')
def ticTacToe():
    return render_template("/assignments/Beaches/ticTacToe.html")

@games.route('/snake-game/')
def Snake():
    return render_template("/assignments/Beaches/Snake.html")

@games.route('/hangman-game/')
def Hangman():
    return render_template("/assignments/Beaches/Hangman.html")

@games.route('/graphing/')
def Graphing():
    return render_template("/assignments/Beaches/graphing.html")

