FROM python:3.7-slim as base

RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends \
 python python-pip python-setuptools

WORKDIR /app

COPY app.py /app/

RUN ls -R

CMD ["python3","app.py"]
