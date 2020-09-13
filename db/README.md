- Платформа
    [Sqlite](https://www.sqlite.org/index.html)
- Запуск
    ```shell
    sudo docker build build --tag db_serv:v1 .
    sudo docker run --publish 7777:7777 --name db_serv:v1 
    ```
- Пример
    ```
    http://localhost:7777/get_answer?text=key_word
    ```
- Параметры

    key_word - ключевое слово, полученное с [nlp_service](https://github.com/maya-ami/neii_hackathon/blob/master/nlp_service)
    результат - ответ о положенных льготах и компенсациях, список  документов, необходимых для получения льготы/компенсации
