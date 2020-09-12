FROM python:3.7-slim as base

RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends \
 python python-pip python-setuptools

RUN pip install rasa==1.6.1
RUN pip uninstall -y tensorflow
RUN pip install tensorflow==1.15.0
RUN pip show tensorflow

WORKDIR /app

COPY app.py /app/

COPY ./models /app/models/

RUN ls -R

CMD ["python3","app.py"]
