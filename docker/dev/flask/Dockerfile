FROM python:3.7-alpine

WORKDIR /flask_app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --dev --system

COPY . .

RUN pip install -e .

EXPOSE 5000
ENTRYPOINT ["./docker/dev/flask/boot.sh"]
