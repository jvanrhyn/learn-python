from datetime import datetime

from flask import Flask, jsonify, render_template, request

from . import app

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/api/v1/books/all", methods=["GET"])
def get_books_all():
    return jsonify(books), 200

@app.route("/api/v1/books/<id>", methods=["GET"])
def get_books_by_id(id):
    if 'id' == None:
        return "Error: No id field provided. Please specify an id.", 500

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == int(id):
            results.append(book)
    
    if results == []:
        return jsonify(f'Could not find a book with id {id}'), 404

    return jsonify(results), 200    
