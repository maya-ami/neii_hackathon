- For speech recognition, install an open source framework [vosk](https://alphacephei.com/vosk/server) with the following command:
    ```shell
    sudo docker run -p 2700:2700 alphacep/kaldi-ru:latest
    ```

<<<<<<< HEAD
- Build a service that records a voice from frontend and sends it to recognition.
=======
- Build a service that records a voice from frontend and sends it to recognition. 
>>>>>>> b94eae5172ecfb52861a515dcf3abf28a3548983
    ```shell
    sudo docker build build --tag asr:1.0 .
    sudo docker run --publish 5000:5000 --name asr asr:1.0
    ```
- Usage

    ```http://0.0.0.0:5000/recognize_wav```

- Returns a recognized text.
