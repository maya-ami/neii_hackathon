- Запуск
    ```Shell
    docker build -t nlu1.0
    docker run -d -p 8888:8888 nlu1.0
    ```
- Пример
    ```
    http://localhost:8888/chat?text=у меня скоро родится второй ребенок. какие льготы положены>
    ```

- Параметры
    text - строка, распознанная [vosk](https://alphacephei.com/vosk/server)
    результат - ключевое слово для поиска в БД
