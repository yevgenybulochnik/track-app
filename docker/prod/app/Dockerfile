FROM python:3.7-alpine

WORKDIR /flask_app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --dev --system

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
