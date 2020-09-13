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
    def create_sch(self):
        cursor = self.conn.cursor();
        cursor.execute("""CREATE TABLE answers
                  (keyword text,  answer text)""")
    def delete_sch(self):
        cursor = self.conn.cursor();
        cursor.execute("""DROP TABLE answers""")
    def create_sch_address(self):
        cursor = self.conn.cursor();
        cursor.execute("""CREATE TABLE address
                  (city text, ad text)""")
    def delete_sch_address(self):
        cursor = self.conn.cursor();
        cursor.execute("""DROP TABLE address""")

    def write(self, name, key_words, doc_list, organizations, summary, comment):
        if not self.conn is None:
            cursor = self.conn.cursor();
            cursor.execute("""INSERT INTO main_table VALUES (?, ?, ?, ?, ?, ?)  """, [name, key_words, doc_list, organizations, summary, comment])
            self.conn.commit();
            return True;
        else:
            return False;
    def write2(self,  key_words,  summary):
        if not self.conn is None:
            cursor = self.conn.cursor();
            cursor.execute("""INSERT INTO answers VALUES (?,  ?)  """, [ key_words, summary])
            self.conn.commit();
            return True;
        else:
            return False;
    def write3(self,  city, address):
        if not self.conn is None:
            cursor = self.conn.cursor();
            cursor.execute("""INSERT INTO address VALUES (?, ?)  """, [ city, address])
            self.conn.commit();
            return True;
        else:
            return False;
    def read(self, key_words):
        cursor = self.conn.cursor();
        key_words = '%' + key_words + '%'
        cursor.execute("""SELECT * FROM main_table WHERE key_words LIKE ? """, [key_words]);
        return cursor.fetchall();
    def read2(self, key_words):
        cursor = self.conn.cursor();
        key_words = '%' + key_words + '%'
        cursor.execute("""SELECT * FROM answers WHERE keyword LIKE ? """, [key_words]);
        return cursor.fetchall();
    def read3(self, city):
        cursor = self.conn.cursor();
        city = '%' + city + '%'
        cursor.execute("""SELECT * FROM address WHERE city LIKE ? """, [city]);
        return cursor.fetchall();
    def readall(self):
        cursor = self.conn.cursor();
        cursor.execute("""SELECT * FROM main_table """);
        return cursor.fetchall();



stor = SQLStorage();
#print (stor.read3('Сызрань'))
#print('/n')
#print(stor.read2('matcapital'))
#stor.delete_sch();
#stor.create_sch();
'''stor.create_sch_address();
stor.write3('Самара', 'город Самара, улица Революционная, 44')
stor.write3('Новокуйбышевск', 'город Новокуйбышевск, улица Ленинградская, 9А')
stor.write3('Тольятти', 'город Тольятти, улица Октябрьская, 59')
stor.write3('Сызрань', 'город Сызрань,  улица К. Маркса, 19')
stor.write3('Чапаевск', 'город Чапаевскь, улица Рабочая, 11 А')
stor.write3('Нефтегорск', 'город Нефтегорск, проспект Победы, 7')
stor.write3('Чапаевск', 'город Отрадный, улица Комсомольская, д.5')'''
print(stor.read2('matcapital'))
print('/n')
print(stor.read2('retired_transport'))
print('/n')
print(stor.read2('disabled_transport'))
print('/n')
print(stor.read2('birth'))
print('/n')
print(stor.read2('child_monthly'))
print('/n')
print(stor.read2('veteran_compensation'))
print('/n')
print(stor.read2('veteran_monthly'))
print('/n')
print(stor.read2('disabled_compensation'))

'''stor.write2('matcapital', ' Вам полагается материнский капитал. Необходимы следующие документы: заявление на получение сертификата на маткапитал;\
 паспорт гражданина Российской Федерации;\
 свидетельства о рождении всех детей; для усыновленных — свидетельства об усыновлении.')

stor.write2('birth', ' Вам полагается единовременное  пособие 17 479,73 руб. Необходимы следующие документы: заявление о назначении пособия;\
справка о рождении ребенка;\
справка с места работы второго родителя о том, что он не получает данное пособие;\
свидетельство о расторжении брака, если родители разведены.')

stor.write2('retired_transport', ' Вам положена ежемесячная денежная компенсация расходов на общественный транспорт. Необходимы следующие документы: заявление на предоставления ЕДВ на оплату проезда в общественном транспорте\
Паспорт (или иной документ, удостоверяющий личность)')

stor.write2('disabled_transport','Вам положены льготы на проезд в общественном транспорте.Необходимые доккументы: заявление;Паспорт;\
Документы, подтверждающие право на льготы. Не нужны, если вы предпенсионер;\
Фотография 3 × 4 см, если есть. ')

stor.write2('child_monthly', 'Вам полагается ежемесячное пособие на ребенка. Необходимы следующие документы: заявление по форме; паспорт; свидетельство о рождении ребенка')

stor.write2('veteran_compensation',   'Вам как ветерану положена ежемесячная денежная компенсация расходов на оплату жилого помещения и коммунальных услуг. Необходиы следующие документы: заявление; паспорт; удостоверение ветерана; Справка о составе семьи ;\
Свидетельство о заключении/расторжении  брака; \ Справка о платежах за жилое помещение и коммунальные услуги; Счета-квитанции; \
СНИЛС заявителя и членов его семьи; Банковские реквизиты' )

stor.write2('veteran_monthly', ' Вам полагаются ежемесячные выплаты. Необходимы следующие документы: заявление; паспорт ;ветеранское удостоверения')

stor.write2('disabled_compensation', 'Вам положена ежемесячная денежная компенсация расходов на оплату жилого помещения и коммунальных услуг ')'''

#stor.write('Doc2', 'Инвалидность, ребенок-инвалид', 'Паспорт. свидетельство о рождении, удостоверение инвалида', 'МФЦ', 'Пусто', 'Пусто');
#stor.write('Doc2', 'Инвалидность, ветеран', 'Паспорт, ветеранское, удостоверение инвалида', 'МФЦ', 'Пусто', 'Пусто');
#print(stor.read('Инвалидность'));
#print(stor.readall());
