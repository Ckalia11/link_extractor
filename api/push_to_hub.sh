#!/bin/bash
GIT_COMMIT=$(git log -1 --format=%h)
docker build -t ckalia/linkextractor:$GIT_COMMIT .
docker push ckalia/linkextractor:$GIT_COMMIT