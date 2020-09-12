#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:59:59 2020

@author: pinkurchin
"""

from flask import Flask, request, send_from_directory, after_this_request, jsonify, g
import sqlite3;

DATABASE = 'documents.db'

app = Flask(__name__, static_url_path='')


def tuple_to_dict(tup):
    result = {'Doc list' : tup[2], 'Orgs' : tup[3], 'Summary' : tup[4] };
    return result;

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db=getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/get_answer')
def get_answer():
    text = request.args.get('text')
    
    #Обращение к модели
    key_words = text
    
    #Обращение к БД
    cursor = get_db().cursor();
    key_words = '%' + key_words + '%'
    cursor.execute("""SELECT * FROM main_table WHERE key_words LIKE ? """, [key_words]);
    answers = cursor.fetchall();
    #keywords = m.get_keywords(text)
    result = [];
    for a in answers:
        result.append(tuple_to_dict(a))
    return jsonify({'answer' : result})


if __name__ == '__main__':
    app.run(debug=True)
