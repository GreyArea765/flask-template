#!/bin/bash
app="docker.template"
docker build -t ${app} .
docker run -d -p 56734:80 \
  --name=${app} \
  -v $PWD:/app ${app}
docker attach ${app}