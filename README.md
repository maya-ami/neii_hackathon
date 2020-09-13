# Решение для хакатона команды НеИИ

Решение состоит из двух частей: голосовой помощник для граждан и сервис проверки обновления нормативных и законодательных актов
1. Голосовой помощник для получения гражданами информации о полагающейся им социальной помощи.

    ![](scheme.png)

    Система состоит из следующих компонентов:

    - asr_service - Сервис распознавания речи. [Подробнее](https://github.com/maya-ami/neii_hackathon/tree/master/asr_service)

    - nlp_service - Сервис обработки естественного языка. [Подробнее](https://github.com/maya-ami/neii_hackathon/tree/master/nlp_service)

    - tts_service - Сервис синтеза речи для обращения системы к пользователю. [Подробнее](https://github.com/maya-ami/neii_hackathon/tree/master/tts_service)

    - db - База данных, в которой хранится информация о мерах социальной поддержки и необходимых документах для получения соцпомощи. [Подробнее](https://github.com/maya-ami/neii_hackathon/tree/master/db)

    - клиент [Подробнее](https://github.com/maya-ami/neii_hackathon/tree/master/client)

    ![](frontend_prototype.png)

2. Сервис проверки обновления нормативных и законодательных актов.

    - law_service - Сервис сравнения документов [Подробнее](https://github.com/maya-ami/neii_hackathon/tree/master/law_service)
    - doc_db - База данных документов
    - аnnouncement_client - клиент, уведомляющий сотрудников об изменениях в документах


# Установка

Представленное решение разработано под ОС Linux.

1. Скачивание

1a. `git clone https://github.com/maya-ami/neii_hackathon`
1b. Также вы можете скачать репозиторий в виде архива и распаковать локально.

2. Установка зависимостей

pip install -r requirements.txt

*NB*: requirements.txt might be not full!

3. Установка Node.js и npm

```
sudo apt-get install nodejs
sudo apt-get install npm
```
4. Запуск микросервисов

Инструкция по установки Docker, необходимого для работы микросервисов - [здесь](https://docs.docker.com/engine/install/).
Подробная информация о создании Docker образа и его запуске представлена в README.md каждого микросервиса.

5. Запуск бекенда

`python3 main_backend.py`

6. Запуск фронтенда
```
cd client
npm install
npm run serve
```
