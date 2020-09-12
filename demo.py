import requests
import ast
import subprocess
import sys
import sqlite3
sys.path.append("db")
import answer_storage2

"""
Временный скрипт для демо прототипа.
"""

db = answer_storage2.SQLStorage()

# запрос пользователь на NLP сервис
r = requests.get('http://0.0.0.0:8888/chat?text={}'.format(sys.argv[1]))
nlp_response = ast.literal_eval(r.text)

# NLU модель определила проблему пользователя - достаем ответ из БД
life_situation = db.read2(nlp_response['user_intent'])

# отправляем ответ на сервис STT
s = requests.get('http://0.0.0.0:5555/say?text={}&speed=1'.format(life_situation))

# записываем возвращаемый бинарник в wav и воспроизводим ответ пользователю
with open('answer.wav', 'wb') as f:
    for i in s:
        f.write(i)
cmd = "play answer.wav"
subprocess.call([cmd], shell=True)
