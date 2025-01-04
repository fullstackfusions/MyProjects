from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Create a Flask app
app = Flask(__name__)

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy object
db = SQLAlchemy(app)

# Create a Marshmallow object
ma = Marshmallow(app)

# Create a class for the book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create a class for the book schema
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author_id')

# Create an instance of the book schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Create a class for the author model
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name

# Create a class for the author schema
class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

# Create an instance of the author schema
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

# Create the database tables
db.create_all()

# Define an endpoint function for creating a new book
@app.route('/book', methods=['POST'])
def add_book():
    # Get the title and author_id from the request data
    title = request.json['title']
    author_id = request.json['author_id']

    # Get the author object from the database
    author = Author.query.get(author_id)

    # Create a new book object
    new_book = Book(title, author)

    # Add the book to the database
    db.session.add(new_book)
    db.session.commit()

    # Return the book as JSON
    return book_schema.jsonify(new_book)

# Define an endpoint function for getting all books
@app.route('/book', methods=['GET'])
def get_books():
    # Get all books from the database
    all_books = Book.query.all()

    # Serialize the books as JSON
    result = books_schema.dump(all_books)

    # Return the books as JSON
    return jsonify(result)

# Define an endpoint function for getting a book by id
@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    # Get the book from the database
    book = Book.query.get(id)

    # Return the book as JSON
    return book_schema.jsonify(book)

# Define an endpoint function for updating a book by id
@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
    # Get the book from the database
    book = Book.query.get(id)

    # Get the title and author_id from the request data
    title = request.json['title']
    author_id = request.json['author_id']

    # Get the author object from the database
    author = Author.query.get(author_id)

    # Update the book attributes
    book.title = title
    book.author = author

    # Commit the changes to the database
    db.session.commit()

    # Return the book as JSON
    return book_schema.jsonify(book)

# Define an endpoint function for deleting a book by id
@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    # Get the book from the database
    book = Book.query.get(id)

    # Delete the book from the database
    db.session.delete(book)
    db.session.commit()

    # Return a success message as JSON
    return jsonify({'message': 'Book deleted successfully'})

# Define an endpoint function for creating a new author
@app.route('/author', methods=['POST'])
def add_author():
    # Get the name from the request data
    name = request.json['name']

    # Create a new author object
    new_author = Author(name)

    # Add the author to the database
    db.session.add(new_author)
    db.session.commit()

    # Return the author as JSON
    return author_schema.jsonify(new_author)

# Define an endpoint function for getting all authors
@app.route('/author', methods=['GET'])
def get_authors():
    # Get all authors from the database
    all_authors = Author.query.all()

    # Serialize the authors as JSON
    result = authors_schema.dump(all_authors)

    # Return the authors as JSON
    return jsonify(result)

# Define an endpoint function for getting an author by id
@app.route('/author/<id>', methods=['GET'])
def get_author(id):
    # Get the author from the database
    author = Author.query.get(id)

    # Return the author as JSON
    return author_schema.jsonify(author)

# Define an endpoint function for updating an author by id
@app.route('/author/<id>', methods=['PUT'])
def update_author(id):
    # Get the author from the database
    author = Author.query.get(id)

    # Get the name from the request data
    name = request.json['name']

    # Update the author name
    author.name = name

    # Commit the changes to the database
    db.session.commit()

    # Return the author as JSON
    return author_schema.jsonify(author)

# Define an endpoint function for deleting an author by id
@app.route('/author/<id>', methods=['DELETE'])
def delete_author(id):
    # Get the author from the database
    author = Author.query.get(id)

    # Delete the author from the database
    db.session.delete(author)
    db.session.commit()

    # Return a success message as JSON
    return jsonify({'message': 'Author deleted successfully'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
