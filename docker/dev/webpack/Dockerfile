FROM flaskdev:latest

WORKDIR /flask_app

ENV WEBPACK_HOST=0.0.0.0
ENV WEBPACK_PROXY_TARGET=http://flask:5000

RUN apk update && \
    apk add nodejs npm yarn

RUN pip install -e .

EXPOSE 8080
ENTRYPOINT ["./docker/dev/webpack/boot.sh"]
