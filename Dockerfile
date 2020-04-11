FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --yes apt-utils
RUN apt-get update && apt-get install --yes iputils-ping iproute2
RUN apt-get update && apt-get install --yes software-properties-common python3
RUN apt-get update && apt-get install --yes wget golang
#RUN wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
#RUN tar -xzf go1.14.2.linux-amd64.tar.gz
#RUN export PATH=/go/bin

COPY . .

RUN go build hello.go
RUN ./hello

