FROM golang
RUN apt-get update && apt-get install --yes iputils-ping iproute2
RUN apt-get update && apt-get install --yes software-properties-common python3 wget git unzip

RUN wget https://github.com/tendermint/tendermint/releases/download/v0.32.6/tendermint_v0.32.6_linux_amd64.zip
RUN unzip tendermint_v0.32.6_linux_amd64.zip -d /usr/bin/
#ENV PATH=.
RUN tendermint version
RUN go version

RUN go get -v github.com/spf13/viper
RUN go get -v github.com/dgraph-io/badger

COPY . . 
RUN go run hello.go
