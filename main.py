from app import app
from flask import render_template, request
from flask import request, redirect

from xBP_routes.about_pages import about_pages
from xBP_routes.games import games
from xBP_routes.beaches import beaches

from crudy.app_crud import app_crud
from crudy.app_crud_api import app_crud_api

app.register_blueprint(games)
app.register_blueprint(about_pages)
app.register_blueprint(beaches)

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)



@app.route('/')
def index():
    return render_template("/index.html")

# ----------------------------------------------------

@app.route('/reviews/')
def reviews():
    return render_template("/assignments/reviews.html")

# ----------------------------------------------------

@app.route('/wordle/', methods=['GET', 'POST'])
def Wordle():
    if request.form:
        guess = request.form.get("Guess")
        print(guess)
        if len(guess) == 5:
            return render_template("/assignments/wordle.html", guess=guess)
    return render_template("/assignments/wordle.html")

# ----------------------------------------------------

@app.route('/jaypbl/')
def jaypbl():
    return render_template("/assignments/Beaches/jaypbl.html")

# ---------------- Beach Survey and Game --------------------

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
