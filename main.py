from __init__ import app
from flask import render_template, request
from flask import request, redirect
import requests

from crud.app_crud import app_crud
app.register_blueprint(app_crud)

# app.routes

@app.route('/')
def index():
    url = "https://tides.p.rapidapi.com/tides"
    querystring = {"longitude":"-2.097","latitude":"44.414","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "c1ebf686e7mshe4ed4400d544e06p107f7fjsn1235b397e8bd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render_template("/index.html", output=response.json())

@app.route('/reviews/')
def reviews():
    return render_template("/assignments/reviews.html")

@app.route('/surfingData/')
def surfingData():
    return render_template("/assignments/surfingData.html")

@app.route('/beachlocation1/')
def BeachLocation1():
    return render_template("/assignments/BeachLocation1.html")

@app.route('/beachlocation2/')
def BeachLocation2():
    return render_template("/assignments/BeachLocation2.html")

def selectBestBeach(form):
    return "DelMar is the best beach for you"

@app.route('/favoritebeach1/', methods=["GET", "POST"])
def FavoriteBeachSurvey():
    feedback = "Beach Not Identified"
    SolanaBeach = 0
    DelMar = 0
    if request.method == "POST":
        if (request.form.get("surfing") != None):
            SolanaBeach += 1
        if (request.form.get("volleyball") != None):
            DelMar += 1
        if (request.form.get("dog") != None):
            DelMar += 1
        if (request.form.get("crowd") != None):
            SolanaBeach += 1
        if (request.form.get("picnic") != None):
            DelMar += 1
        if (DelMar == 0 and SolanaBeach == 0):
            feedback = "Pick at least one preference"
        elif (DelMar > SolanaBeach):
            feedback = "Del Mar beach is best for you"
        elif (SolanaBeach > DelMar):
            feedback = "Solana Beach is best for you"
        elif (SolanaBeach == DelMar):
            feedback = "Solana and Del Mar beach are good for you"

    return render_template("/assignments/Survey.html", beach = feedback)

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

    url = "https://sportscore1.p.rapidapi.com/tennis-rankings/wta"
    querystring = {"page":"1"}
    headers = {
        'x-rapidapi-host': "sportscore1.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    responseTwo = requests.request("GET", url, headers=headers, params=querystring)
    WTAdata = responseTwo.json()

    url = "https://sportscore1.p.rapidapi.com/tennis-rankings/atp"
    querystring = {"page":"1"}
    headers = {
    'x-rapidapi-host': "sportscore1.p.rapidapi.com",
    'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    return render_template("/assignments/AboutUs/akhil.html", data=data, WTAdata=WTAdata)


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


    import requests

    url = "https://nhl-stats-and-live-data.p.rapidapi.com/standings"

    querystring = {"date":"2018-01-09","season":"20032004"}

    headers = {
        'x-rapidapi-host': "nhl-stats-and-live-data.p.rapidapi.com",
        'x-rapidapi-key': "39c4bf8c2emsh30b02ab6dc01dd9p13f427jsn690a650cf2ec"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    var = response.json()
    return render_template("/assignments/AboutUs/jay.html", var=var)

@app.route('/password/')
def Password():
    return render_template("/assignments/password.html")

# run page lol
if __name__ == "__main__":
    app.run(debug=True)
