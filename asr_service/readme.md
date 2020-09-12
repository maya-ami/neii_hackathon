## 1. Поднимаем сервис распознавания речи - vosk

sudo docker run -p 2700:2700 alphacep/kaldi-ru:latest

## 2. Запускаем наш сервис, принимающий голос с фронт-энда и передающий его на распознавание

sudo docker build build --tag asr:1.0 .
sudo docker run --publish 7777:7777 --name asr asr:1.0
