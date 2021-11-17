FROM python:3.8-alpine

ADD requirements.pip /src/requirements.pip
RUN pip3 install -r /src/requirements.pip

WORKDIR /app
ADD main.py /app/main.py

CMD ["hypercorn", "-b", "0.0.0.0:8000", "main:app"]
