from requests_toolbelt import MultipartEncoder
import requests
import json
import ast
import subprocess
import sys
import sqlite3
sys.path.append("db")
import answer_storage2
from flask import Flask, jsonify, Response, request
from flask_cors import CORS, cross_origin

"""
Бекенд, связывающий 3 микросервиса (ASR, NLP, STT), с JS фронтендом.
Приложение использует два метода:
    - sound активируется при голосовом обращении к чат-боту.
    - text активируется при отправки текстового сообщения в форму чат-бота.
"""

app = Flask(__name__)
cors = CORS(app)


def chunked_reader(f, chunksize=2 ** 20):  # 1Mb chunks
    while True:
        chunk = f.read(chunksize)
        if not chunk:
            return
        yield chunk

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/sound', methods=['POST'])
@cross_origin(supports_credentials=True)
def sound():
    # Записываем полученный с фронтенда бинарник в wav файл
    to_recognize = request.files['file'].read()
    with open("./asr_service/question.wav", "wb") as f:
        f.write(to_recognize)

    # # Отправляем wav файл на ASR сервис
    q = requests.get("http://0.0.0.0:5000/recognize_wav")
    print(q.text)

    # # запрос пользователь на NLP сервис
    r = requests.get('http://0.0.0.0:8888/chat?text={}'.format(q.text))
    nlp_response = ast.literal_eval(r.text)

    # # NLU модель определила проблему пользователя - достаем инфо из БД
    db = answer_storage2.SQLStorage()
    life_situation = db.read2(nlp_response['user_intent'])
    print(life_situation[0][0])

    # # отправляем инфо на сервис синтеза речи (STT)
    s = requests.get('http://0.0.0.0:5555/say?text={}'.format(life_situation))

    # # возвращаем сгенерированный голосовой ответ на фронтенд
    # return {s.content}
    # пока не получилось передавать файл синтеза речи в виде бинарника через браузер,
    # сохраним и воспроизведем файл синтеза речи
    with open('answer.wav', 'wb') as f:
        for i in s:
            f.write(i)
    cmd = "play answer.wav"
    subprocess.call([cmd], shell=True)


    dict1 = [{"text": q.text, "isBot": False}, {"text": life_situation[0][0], "isBot": True}]
    m = MultipartEncoder(fields={ 'messages': json.dumps(dict1), 'files': ("sound.wav", s.content, 'audio/wav') })
    return (m.to_string(), {'Content-Type': m.content_type})



@app.route('/text', methods=['POST'])
def text():
    text = request.form["text"]
    r = requests.get('http://0.0.0.0:8888/chat?text={}'.format(text))
    nlp_response = ast.literal_eval(r.text)

    # # NLU модель определила проблему пользователя - достаем инфо из БД
    db = answer_storage2.SQLStorage()
    life_situation = db.read2(nlp_response['user_intent'])
    print(life_situation)

    # # отправляем инфо на сервис синтеза речи (STT)
    s = requests.get('http://0.0.0.0:5555/say?text={}'.format(life_situation))

    # # возвращаем сгенерированный голосовой ответ на фронтенд
    # return {s.content}
    # пока не получилось передавать файл синтеза речи в виде бинарника через браузер,
    # сохраним и воспроизведем файл синтеза речи
    # with open('answer.wav', 'wb') as f:
    #     for i in s:
    #         f.write(i)
    # cmd = "play answer.wav"
    # subprocess.call([cmd], shell=True)

    print(s.content)


    dict1 = [{"text": life_situation[0][0], "isBot": True}]
    m = MultipartEncoder(fields={ 'messages': json.dumps(dict1), 'files': ("sound.wav", s.content, 'audio/wav') })
    return (m.to_string(), {'Content-Type': m.content_type})

if __name__ == "__main__":
    app.run(host='localhost', port=8083, debug=True)
