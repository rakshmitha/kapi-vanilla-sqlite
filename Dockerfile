FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN pip install flask

COPY . /app

WORKDIR /app

RUN apk update \
    && apk add bash nano
RUN pip install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]