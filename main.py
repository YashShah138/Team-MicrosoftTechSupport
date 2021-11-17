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

@app.route('/surfingData/')
def surfingData():
    return render_template("surfingData.html")

@app.route('/yash/')
def yash():
    return render_template("/assignments/AboutUs/yash.html")

@app.route('/akhil/')
def akhil():
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