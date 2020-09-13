#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 18:30:42 2020

@author: pinkurchin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 20:59:59 2020

@author: pinkurchin
"""

from flask import Flask, request, send_from_directory, after_this_request, jsonify, g
import sqlite3;

DATABASE = 'update_documents.db'

app = Flask(__name__, static_url_path='')


def tuple_to_dict(tup):
    result = {'doc_updt' : tup[0]};
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

@app.route('/get_doc_updt')
def get_answer():
    text = request.args.get('doc_name')
    
    #Обращение к БД
    cursor = get_db().cursor();
    cursor.execute("""SELECT updt FROM docs WHERE name =  ?  """, [text]);
    answers = cursor.fetchall();
    #keywords = m.get_keywords(text)
    result = [];
    for a in answers:
        result.append(tuple_to_dict(a))
    return jsonify({'answer' : result})

@app.route('/set_doc_uinfo')
def get_answer():
    name = request.args.get('doc_name')
    updt = request.args.get('doc_updt')
    changes = request.args.get('doc_changes')
    
    cursor = get_db().cursor();
    cursor.execute("""UPDATE docs  SET name = ? , updt = ?, changes = ? WHERE name = ?""", [name, updt, changes, name])
    get_db().commit()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6547)