FROM ghcr.io/khainee/mlt:latest

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

CMD ["bash", "start.sh"]
