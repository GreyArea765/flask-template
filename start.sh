#!/bin/bash
app="docker.template"
docker build -t ${app} .
docker run -d -p 56734:80 \
  --name=${app} \
  -v $PWD:/app ${app}
# Uncomment this line to watch Gunicorn start up.
#docker attach ${app}