- Framework used:
    [Sqlite](https://www.sqlite.org/index.html)
- Build
    ```shell
    sudo docker build build --tag db_serv:v1 .
    sudo docker run --publish 7777:7777 --name db_serv:v1
    ```
- Usage
    ```
    http://localhost:7777/get_answer?text=key_word
    ```
- Parameters

    key_word - an answer of the [nlp_service](https://github.com/maya-ami/neii_hackathon/blob/master/nlp_service).

- Returns info on statutory benefits and the documents a person needs to provide to claim the benefits.
