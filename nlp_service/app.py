from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
import tensorflow.compat.v1 as tf
tf.logging.set_verbosity(tf.logging.ERROR)
import asyncio
import subprocess
from subprocess import Popen, PIPE
import os, sys
import warnings
warnings.filterwarnings('ignore')

from flask import Flask, request, send_from_directory, after_this_request
import subprocess, os, urllib, hashlib, re
from shlex import quote

app = Flask(__name__)
agent = Agent.load("./models/20200912-152114.tar.gz")

@app.route("/chat")
def chat():
    text = request.args.get('text')
    msg = asyncio.run(agent.parse_message_using_nlu_interpreter(text))
    dic = {}
    dic['user_intent'] = msg['intent']['name']
    for i in range(len(msg['entities'])):
        dic[msg['entities'][0]['entity']] = msg['entities'][0]['value']
    dic['bot_reposnse'] = asyncio.run(agent.handle_text(text))[0]['text']
    resb = str(dic)
    return resb


if __name__ == "__main__":
    app.run("0.0.0.0",debug=True, threaded=True)
