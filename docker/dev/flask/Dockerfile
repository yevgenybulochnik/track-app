FROM python:3.7-alpine

WORKDIR /flask_app

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN pip install -e .

EXPOSE 5000
ENTRYPOINT ["./docker/dev/flask/boot.sh"]
