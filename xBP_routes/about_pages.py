from flask import Blueprint, render_template, request
import requests

about_pages = Blueprint('About', __name__,
                     url_prefix='/about',
                     template_folder='templates',
                     static_folder='static', static_url_path='static/about')

# ----------------------------------------

@about_pages.route("/akhil/", methods=['GET','POST'])
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


@about_pages.route('/yash/')
def yash():
    url = "https://yourf1.p.rapidapi.com/drivers"

    headers = {
        'x-rapidapi-host': "yourf1.p.rapidapi.com",
        'x-rapidapi-key': "80e73128e0mshda8c95123266391p176951jsnbc06ff234f92"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render_template("/assignments/AboutUs/yash.html", data=data)


@about_pages.route('/valen/')
def valen():

    url = "https://nfl-team-stats.p.rapidapi.com/v1/nfl-stats/teams/win-stats/2021"

    headers = {
        'x-rapidapi-host': "nfl-team-stats.p.rapidapi.com",
        'x-rapidapi-key': "dabdc2fe99mshcfa1ae8827f4f16p1f550djsn5f1b6441c796"
    }
    response = requests.request("GET", url, headers=headers)
    chargers=response.json()


    print(response.text)
    return render_template("/assignments/AboutUs/valen.html", chargers=chargers)


@about_pages.route('/avinh/', methods=['GET', 'POST'])
def avinh():
    if request.form:
        pokemon = request.form.get("input")
        PokemonAPI = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon)
        PokemonImage = (PokemonAPI.json()["sprites"]["front_default"])
        return render_template("/assignments/AboutUs/avinh.html", PokemonImage=PokemonImage)
    return render_template("/assignments/AboutUs/avinh.html")


@about_pages.route('/jay/')
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
