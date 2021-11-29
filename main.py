# imports
from flask import Flask, render_template, request

# creates whatever a Flask instance is
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

    print(response.text)


    return render_template("/assignments/AboutUs/akhil.html")


@app.route('/valen/')
def valen():
    return render_template("/assignments/AboutUs/valen.html")


@app.route('/avinh/')
def avinh():
    return render_template("/assignments/AboutUs/avinh.html")


@app.route('/jay/')
def jay():
    return render_template("/assignments/AboutUs/jay.html")


# run page lol
if __name__ == "__main__":
    app.run(debug=True)
