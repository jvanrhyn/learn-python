from datetime import datetime

from flask import Flask, jsonify, render_template, request

from . import app
from . import data

@app.route("/api/v1/books/all", methods=["GET"])
def get_books_all():
    return jsonify(data.books), 200

@app.route("/api/v1/books/<id>", methods=["GET"])
def get_books_by_id(id):
    if 'id' == None:
        return "Error: No id field provided. Please specify an id.", 500

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in data.books:
        if book['id'] == int(id):
            results.append(book)
    
    if results == []:
        return jsonify(f'Could not find a book with id {id}'), 404

    return jsonify(results), 200    
