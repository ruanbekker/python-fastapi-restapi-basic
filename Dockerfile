FROM python:3.8-alpine

RUN adduser -D app
WORKDIR /home/app

ADD requirements.pip /src/requirements.pip
RUN pip3 install -r /src/requirements.pip

ADD main.py /home/app/main.py
RUN chown -R app:app /home/app

USER app

CMD ["hypercorn", "-b", "0.0.0.0:8000", "main:app"]
