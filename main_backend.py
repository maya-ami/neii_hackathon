import requests
import ast
import subprocess
import sys
import sqlite3
sys.path.append("db")
import answer_storage2
from cont_asr import listen

from flask import Flask

"""
Бекенд, связывающий 3 микросервиса (ASR, NLP, STT)
"""

app = Flask(__name__)

@app.route('/assist')
def assist():
    # ! пока бинарник имитирует прочитанный wav файлик!
    # ! В проде вместо этого будет блоб с фронтенда!
    with open("example_from_front.wav", "rb") as f:
        to_recognize = f.read()

    # Записываем полученный с фронтенда бинарник в wav файл
    with open("./asr_service/question.wav", "wb") as f:
        f.write(to_recognize)

    # Отправляем wav файл на ASR сервис
    q = requests.get("http://0.0.0.0:5000/recognize_wav")
    print(q.text)

    # запрос пользователь на NLP сервис
    r = requests.get('http://0.0.0.0:8888/chat?text={}'.format(q.text))
    nlp_response = ast.literal_eval(r.text)

    # NLU модель определила проблему пользователя - достаем инфо из БД
    db = answer_storage2.SQLStorage()
    life_situation = db.read2(nlp_response['user_intent'])
    print(life_situation)

    # отправляем инфо на сервис синтеза речи (STT)
    s = requests.get('http://0.0.0.0:5555/say?text={}'.format(life_situation))

    # возвращаем сгенерированный голосовой ответ на фронтенд
    return s.content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999, debug=True)
