#from wsgiref import headers

#import querystring as querystring
from flask import Flask, render_template, request
import requests

# creates whatever a Flask instance is
from requests import get

app = Flask(__name__)

# app.routes
@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/aboutus/')
def aboutus():
    return render_template("/assignments/aboutus.html")


@app.route('/surfingData/')
def surfingData():
    url = "https://tides.p.rapidapi.com/tides"
    querystring = {"longitude":"-2.097","latitude":"44.414","interval":"60","duration":"1440"}
    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "80e73128e0mshda8c95123266391p176951jsnbc06ff234f92"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render_template("/assignments/surfingData.html")


@app.route('/yash/')
def yash():
    url = "https://yourf1.p.rapidapi.com/drivers"

    headers = {
    'x-rapidapi-host': "yourf1.p.rapidapi.com",
    'x-rapidapi-key': "80e73128e0mshda8c95123266391p176951jsnbc06ff234f92"
}

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render_template("/assignments/AboutUs/yash.html", data=data)


@app.route('/akhil/')
def akhil():
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
