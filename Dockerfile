FROM ubuntu:latest
LABEL authors="ander"

ENTRYPOINT ["top", "-b"]