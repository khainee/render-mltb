FROM ghcr.io/khainee/mlt:rclone
RUN apt-get -qq update
RUN apt-get -qq install -y npm

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . .

CMD ["bash", "start.sh"]
