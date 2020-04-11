FROM ubuntu:16.04
RUN apt-get update && apt-get install --yes iputils-ping iproute2
RUN apt-get update && apt-get install --yes software-properties-common python3
RUN apt-get update && apt-get install --yes wget golang

RUN apt-get update && apt-get install --yes git

RUN apt-get update && apt-get install --yes unzip

RUN wget https://github.com/tendermint/tendermint/releases/download/v0.32.6/tendermint_v0.32.6_linux_amd64.zip
RUN unzip tendermint_v0.32.6_linux_amd64.zip -d /usr/bin/
#ENV PATH=.
RUN tendermint version

