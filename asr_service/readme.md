- For speech recognition, install an open source framework [vosk](https://alphacephei.com/vosk/server) with the following command:
    ```shell
    sudo docker run -p 2700:2700 alphacep/kaldi-ru:latest
    ```

- Build a service that records a voice from frontend and sends it to recognition. 
    ```shell
    sudo docker build build --tag asr:1.0 .
    sudo docker run --publish 5000:5000 --name asr asr:1.0
    ```
- Usage

    ```http://0.0.0.0:5000/recognize_wav```
