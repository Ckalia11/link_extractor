#!/bin/bash
GIT_COMMIT=$(git log -1 --format=%h)
docker build -t ckalia/linkextractor-api:$GIT_COMMIT ./api
docker build -t ckalia/linkextractor-web:$GIT_COMMIT ./web
docker push ckalia/linkextractor-api:$GIT_COMMIT
docker push ckalia/linkextractor-web:$GIT_COMMIT
docker rmi ckalia/linkextractor-api:$GIT_COMMIT
docker rmi ckalia/linkextractor-web:$GIT_COMMIT