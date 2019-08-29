FROM dyne/devuan:ascii

RUN apt-get -y update --fix-missing
#RUN apt-get -y install ...

WORKDIR /app
COPY src /app
