- Сервис распознавания речи [vosk](https://alphacephei.com/vosk/server)
    ```shell
    sudo docker run -p 2700:2700 alphacep/kaldi-ru:latest
    ```
    
- Cервис, принимающий голос с фронт-энда и передающий его на распознавание
    ```shell
    sudo docker build build --tag asr:1.0 .
    sudo docker run --publish 5000:5000 --name asr asr:1.0
    ```
- Пример

    ```http://0.0.0.0:5000/recognize_wav```
