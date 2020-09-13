Сервис синтеза речи использует проект [RHVoice](https://github.com/Olga-Yakovleva/RHVoice)
- Запуск
    ```shell
    docker build -t tts1.0 .
    docker run -d -p 5555:5555 tts1.0 
    ```
- Пример
    ```
    http://localhost:5555/say?text=Привет&speed=1
    ```
- Параметры 
    - text - текст для синтеза
    - voice - имя голоса RHVoice
    - speed - скорость воспроизведения Wav файла
