FROM nginx:alpine
EXPOSE 80

RUN rm /etc/nginx/conf.d/default.conf

COPY docker/nginx/webapp.conf /etc/nginx/conf.d
