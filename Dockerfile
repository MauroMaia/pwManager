#FROM python:3.6-alpine
FROM python:3.9-buster
MAINTAINER Mauro Filipe Maia <dev@maurofilipemaia.dev>
ENV PS1="\[\e[0;33m\]|> pwmanager <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /src
COPY . /src
RUN pip install --no-cache-dir -r requirements.txt \
    && python setup.py install
WORKDIR /
ENTRYPOINT ["pwmanager"]
