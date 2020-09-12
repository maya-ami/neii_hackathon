#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:35:04 2020

@author: pinkurchin
"""

from flask import Flask, request, send_from_directory, after_this_request, jsonify, g
import websockets
import asyncio
import ast

app = Flask(__name__, static_url_path='')

async def fetch(uri, wavf):
    result = []
    async with websockets.connect(uri) as websocket:
        wf = open(wavf, "rb")
        while True:
            data = wf.read(8000)

            if len(data) == 0:
                break

            await websocket.send(data)
            result.append(await websocket.recv())

        await websocket.send('{"eof" : 1}')
        result.append(await websocket.recv())
    return result



@app.route('/recognize_wav')
def recognize_wav():
    with open("question.wav", "rb") as wf:
        wf.read()
    asyncio.set_event_loop(asyncio.SelectorEventLoop())
    result = asyncio.get_event_loop().run_until_complete(fetch('ws://localhost:2700', "question.wav"))
    print(result)
    result_dict = ast.literal_eval(result[-5])
    return result_dict['text']

if __name__ == '__main__':
    app.run(debug=True)
