""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate

from __init__ import app



# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along
# Define variable to define type of database (sqlite), and name and location of review.db
dbURI = 'sqlite:///model/review.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text, unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, title, content, phone):
        self.name = name
        self.title = title
        self.content = content
        self.phone = phone

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "title": self.title,
            "content": self.content,
            "phone": self.phone
        }

    # CRUD update: updates users name, content, phone
    # returns self
    def update(self, name, content="", phone=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(content) > 0:
            self.content = content
        if len(phone) > 0:
            self.phone = phone
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""



def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Akhil', title='Loved Del Mar!', content='The beach was awesome! I had a super enjoyable experience with my family, and playing volleyball was super fun!', phone="8582078758")
    table = [u1]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate title, or error: {row.title}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
