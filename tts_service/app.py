#!/usr/bin/env python
from flask import Flask, request, send_from_directory, after_this_request
import subprocess, os, urllib, hashlib, re
from shlex import quote

app = Flask(__name__, static_url_path='')
data_path = "/opt/data"


@app.route('/say')
def say():
    text = request.args.get('text')
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    file_name = m.hexdigest()
    file_path = data_path + "/" + file_name
    voice = request.args.get('voice')
    speed = request.args.get('speed')
    voice = "-p anna" if voice is None else "-p %s" % (voice)
    speed = "1" if speed is None else "%s" % (speed)
    cmd = "echo %s | RHVoice-test %s -o %s.wav && sox %s.wav %s.wav tempo %s" % (quote(text), voice, file_path, file_path, file_path+'_speed', speed)
    subprocess.call([cmd], shell=True)
    @after_this_request
    def remove_file(response):
        os.remove("%s.wav" % (file_path+"_speed"))
        return response
    # return send_from_directory(data_path, "%s.wav" % (file_name+"_speed"))
    with open("%s.wav" % (file_path+"_speed"), "rb") as f:
        data = f.read()

    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)
