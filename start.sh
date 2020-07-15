#!/bin/bash
app="kapi"
docker build -t ${app} .
docker run -d -p 5001:5001 \
  --name=${app} 