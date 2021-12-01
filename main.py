# imports
from flask import Flask, render_template, request
import requests

# creates whatever a Flask instance is
from requests import get

app = Flask(__name__)

# app.routes
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutus/')
def aboutus():
    return render_template("/assignments/aboutus.html")


@app.route('/surfingData/')
def surfingData():
    return render_template("surfingData.html")


@app.route('/yash/')
def yash():
    return render_template("/assignments/AboutUs/Yash.html")


@app.route('/akhil/')
def akhil():

    import requests
    url = "https://sportscore1.p.rapidapi.com/tennis-rankings/atp"
    querystring = {"page":"1"}
    headers = {
    'x-rapidapi-host': "sportscore1.p.rapidapi.com",
    'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    return render_template("/assignments/AboutUs/akhil.html", data=data)


@app.route('/valen/')
def valen():
    import requests

    url = "https://nfl-team-stats.p.rapidapi.com/v1/nfl-stats/teams/win-stats/2021"

    headers = {
    'x-rapidapi-host': "nfl-team-stats.p.rapidapi.com",
    'x-rapidapi-key': "dabdc2fe99mshcfa1ae8827f4f16p1f550djsn5f1b6441c796"
    }
    response = requests.request("GET", url, headers=headers)
    chargers=response.json()


    print(response.text)
    return render_template("/assignments/AboutUs/valen.html", chargers=chargers)


@app.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    if request.form:
        pokemon = request.form.get("input")
        PokemonAPI = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
        PokemonImage = (PokemonAPI.json()["sprites"]["front_default"])
        return render_template("/assignments/AboutUs/avinh.html", PokemonImage=PokemonImage)
    return render_template("/assignments/AboutUs/avinh.html")


@app.route('/jay/')
def jay():
    return render_template("/assignments/AboutUs/jay.html")


# run page lol
if __name__ == "__main__":
    app.run(debug=True)
