#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:27:41 2020

@author: pinkurchin
"""

# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import sqlite3;

class SQLStorage(object):
    def __init__(self, db_name = "documents_v2.db"):
        self.conn = sqlite3.connect(db_name)

    def write2(self,  key_words,  summary):
        if not self.conn is None:
            cursor = self.conn.cursor();
            cursor.execute("""INSERT INTO answers VALUES (?, ?)  """, [ key_words,  summary])
            self.conn.commit();
            return True;
        else:
            return False;
    def read2(self, key_words):
        cursor = self.conn.cursor();
        key_words = '%' + key_words + '%'
        cursor.execute("""SELECT answer FROM answers WHERE keyword LIKE ? """, [key_words]);
        return cursor.fetchall();




# stor = SQLStorage();
# print(stor.read2('matcapital'))
# print(stor.read2('retired_transport'))
