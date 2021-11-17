# imports
from flask import Flask, render_template

# creates whatever a Flask instance is
app = Flask(__name__)

# app.routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aboutus/')
def aboutus():
    return render_template("/assignments/aboutus.html")

# run page lol
if __name__ == "__main__":
    app.run(debug=True)