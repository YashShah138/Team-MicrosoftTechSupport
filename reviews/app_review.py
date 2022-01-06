"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests
from reviewmodel import Review


# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_reviews = Blueprint('reviews', __name__,
                     url_prefix='/reviews',
                     template_folder='templates/assignments/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_reviews)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def reviews_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Review.query.all()]


def reviews_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Review.query.filter((Review.name.ilike(term)) | (Review.title.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def reviews_by_id(userid):
    """finds User in table matching userid """
    return Review.query.filter_by(userID=userid).first()


# User extraction from SQL
def reviews_by_title(title):
    """finds User in table matching email """
    return Review.query.filter_by(title=title).first()


""" app route section """


# Default URL
@app_reviews.route('/')
def reviews():
    """obtains all Users from table and loads Admin Form"""
    return render_template("reviews.html", table=reviews_all())


# CRUD create/add
@app_reviews.route('/create-review/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Review(
            request.form.get("name"),
            request.form.get("title"),
            request.form.get("content"),
        )
        po.create()
    return redirect(url_for('reviews.reviews'))


# CRUD read
@app_reviews.route('/read-reviews/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = reviews_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("reviews.html", table=table)


# CRUD update
@app_reviews.route('/update-reviews/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = reviews_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('reviews.reviews'))


# CRUD delete
@app_reviews.route('/delete-reviews/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = reviews_by_id(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('reviews.reviews'))

""" API routes section """

class ReviewsAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, title, content):
            po = Review(name, title, content)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {name} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return reviews_all()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return reviews_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, title, name):
            po = reviews_by_title(title)
            if po is None:
                return {'message': f"{title} is not found"}, 210
            po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, name, title, content):
            po = reviews_by_title(title)
            if po is None:
                return {'message': f"{title} is not found"}, 210
            po.update(name, title, content)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = reviews_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:email>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:email>/<string:name>/<string:password>/<string:phone>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/reviews'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create-reviews/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create-reviees/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read-reviews/', "get"],
        ['/read-reviews/ilike/John', "get"],
        ['/read-reviews/ilike/com', "get"],
        ['/update-reviews/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update-reviews/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete-reviews/4', "delete"],
        ['/delete-reviews/5', "delete"],
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for user in reviews_all():
        print(user)


"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()
