FROM python:3.7-slim as base

RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends \
 python python-pip python-setuptools

WORKDIR /app
COPY requirements.txt requirements.txt
COPY app.py /app/

COPY update_documents.db /app/

RUN pip install -r requirements.txt

CMD ["python3","app.py"]
