from flask import Blueprint, render_template, request
import requests

beaches = Blueprint('beaches', __name__,
                  url_prefix='/beaches',
                  template_folder='templates',
                  static_folder='static', static_url_path='static/beaches')

@beaches.route('/solana-beach/')
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

@beaches.route('/del-mar-beach/')
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

@beaches.route('/blacks-beach/')
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

@beaches.route('/pacific-beach/')
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

@beaches.route('/beachlocation3/')
def BeachLocation3():
    return render_template("/assignments/Beaches/BeachLocation3.html", image_list=[
        "https://www.californiabeaches.com/wp-content/uploads/2014/09/BigS-Overlooking-Blacks-Beach-San-Diego-CA-Large-e1512026583176.jpg",
        "https://theshoallajolla.com/latest/wp-content/uploads/2019/02/shutterstock_767106478.jpg",
        "https://d14fqx6aetz9ka.cloudfront.net/wp-content/uploads/2018/05/03094852/11.jpg"
    ])

