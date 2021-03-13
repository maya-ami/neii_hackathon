For text-to-speech synthesis, use an open source framework [RHVoice](https://github.com/Olga-Yakovleva/RHVoice)
- Build
    ```shell
    docker build -t tts1.0 .
    docker run -d -p 5555:5555 tts1.0
    ```
- Usage
    ```
    http://localhost:5555/say?text=Привет&speed=1
    ```
- Parameters
    - text
    - voice - available voices: Elena, Anna, Irina, Alexander.
    - speed

- Returns a wav file and plays it.
