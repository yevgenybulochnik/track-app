FROM webapp:latest as StaticAssets
RUN apk update && apk add nodejs npm yarn
RUN yarn install
RUN flask build

FROM nginx:alpine
EXPOSE 80

RUN rm /etc/nginx/conf.d/default.conf

COPY docker/prod/nginx/webapp.conf /etc/nginx/conf.d
COPY --from=StaticAssets /flask_app/app/static /webapp/static
