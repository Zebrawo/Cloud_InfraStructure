FROM mongo:latest

COPY mongod.conf /etc/mongod.conf

RUN sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf
