from app import app
from flask import render_template, request
from flask import request, redirect
import requests

from xBP_routes.about_pages import about_pages
from xBP_routes.games import games


from crudy.app_crud import app_crud
from crudy.app_crud_api import app_crud_api

app.register_blueprint(games)
app.register_blueprint(about_pages)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)



# app.routes

@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/reviews/')
def reviews():
    return render_template("/assignments/reviews.html")

@app.route('/wordle/', methods=['GET', 'POST'])
def Wordle():
    if request.form:
        guess = request.form.get("Guess")
        print(guess)
        if len(guess) == 5:
            return render_template("/assignments/wordle.html", guess=guess)
    return render_template("/assignments/wordle.html")

@app.route('/jaypbl/')
def jaypbl():
    return render_template("/assignments/Beaches/jaypbl.html")


# ---------------- BEACHES --------------------

@app.route('/solana-beach/')
def SolanaBeach():

    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.272469","latitude":"32.989262","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/SolanaBeach.html", tides=tides)


@app.route('/del-mar-beach/')
def DelMarBeach():

    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.872269","latitude":"33.603588","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/DelMarBeach.html", tides=tides)


@app.route('/blacks-beach/')
def BlacksBeach():

    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.253716","latitude":"32.898354","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/BlacksBeach.html", tides=tides)


@app.route('/pacific-beach/')
def PacificBeach():

    url = "https://tides.p.rapidapi.com/tides"

    querystring = {"longitude":"-117.236748","latitude":"32.782021","interval":"60","duration":"1440"}

    headers = {
        'x-rapidapi-host': "tides.p.rapidapi.com",
        'x-rapidapi-key': "af654d789amshce4b35d071f3bd2p1c0cc8jsn8db3aa6a8acc"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    tides = response.json()

    return render_template("/assignments/Beaches/PacificBeach.html", tides=tides)


@app.route('/beachlocation3/')
def BeachLocation3():
    return render_template("/assignments/Beaches/BeachLocation3.html", image_list=[
        "https://www.californiabeaches.com/wp-content/uploads/2014/09/BigS-Overlooking-Blacks-Beach-San-Diego-CA-Large-e1512026583176.jpg",
        "https://theshoallajolla.com/latest/wp-content/uploads/2019/02/shutterstock_767106478.jpg",
        "https://d14fqx6aetz9ka.cloudfront.net/wp-content/uploads/2018/05/03094852/11.jpg"
                                                                                  ])


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


@app.route('/beach-guessing/', methods=["GET", "POST"])
def BeachGuessing():

    return render_template("/assignments/Beach Guessing.html")


# run page lol
if __name__ == "__main__":
    app.run(debug=True)
