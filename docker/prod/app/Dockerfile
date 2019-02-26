FROM python:3.7-alpine

WORKDIR /flask_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY tests tests
COPY wp_config wp_config
COPY flask-base.py setup.py setup.cfg package.json config.py tsconfig.json ./
COPY docker/prod/app/boot.sh boot.sh

RUN pip install -e .

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
