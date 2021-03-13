To build an NLU model, we've used an open source framework [Rasa](https://github.com/RasaHQ/rasa).
- Build
    ```Shell
    docker build -t nlu1.0 .
    docker run -d -p 8888:8888 nlu1.0
    ```
- Usage
    ```
    http://localhost:8888/chat?text=у меня скоро родится второй ребенок. какие льготы положены>
    ```

- Parameters

    text - строка, распознанная [vosk](https://alphacephei.com/vosk/server)

- Returns a keyword describing the class of social benefits (maternal, retired, disabled, etc.)
