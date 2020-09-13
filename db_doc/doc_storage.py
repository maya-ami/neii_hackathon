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

class SQLDOCStorage(object):
    def __init__(self, db_name = "update_documents.db"):
        self.conn = sqlite3.connect(db_name)
    def create_sch(self):
        cursor = self.conn.cursor();
        cursor.execute("""CREATE TABLE docs
                  (name text, updt text, changes text)""")
    def delete_sch(self):
        cursor = self.conn.cursor();
        cursor.execute("""DROP TABLE docs""")
            
    def update(self, name, updt, changes):
        cursor = self.conn.cursor();
        cursor.execute("""UPDATE docs  SET name = ? , updt = ?, changes = ? WHERE name = ?""", [name, updt, changes, name])
        self.conn.commit()
            
    def write(self, name, updt, changes):
        cursor = self.conn.cursor();
        cursor.execute("""INSERT INTO docs VALUES (?, ?, ?)  """, [name, updt, changes])
        self.conn.commit()
    def read(self, name):
        cursor = self.conn.cursor();
        cursor.execute("""SELECT * FROM docs WHERE name = ? """, [name]);
        return cursor.fetchall();

    def readall(self):
        cursor = self.conn.cursor();
        cursor.execute("""SELECT * FROM docs """);
        return cursor.fetchall();
        


stor = SQLDOCStorage();
#stor.create_sch();
#stor.write('Федеральный закон "О государственной социальной помощи" от 17.07.1999 N 178-ФЗ', '11.09.2020','Изменены пункт 3.2, 4.4')
#stor.write('Федеральный закон "О дополнительных мерах государственной поддержки семей, имеющих детей" от 29.12.2006 N 256-ФЗ', '10.05.2019', 'Изменены пункт 2.2, 4.1')
#stor.write('Закон РФ "О социальной защите граждан, подвергшихся воздействию радиации вследствие катастрофы на Чернобыльской АЭС"', '01.09.2002','Изменены пункт 3.3, 4.4')
stor.update('Закон РФ "О социальной защите граждан, подвергшихся воздействию радиации вследствие катастрофы на Чернобыльской АЭС"', '01.09.2002','Изменены пункт 3.5, 4.1')
print (stor.readall())