from flask import Blueprint, render_template, request
import requests

games = Blueprint('games', __name__,
                  url_prefix='/games',
                  template_folder='templates',
                  static_folder='static', static_url_path='static/games')