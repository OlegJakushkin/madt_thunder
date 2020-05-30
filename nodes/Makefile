# Makefile for the "localnode" docker image.

all:
	build-validator build-nonvalidator
.PHONY: all

build-validator:
	docker build --tag tendermint/validator validator
.PHONY: build-validator

build-nonvalidator:
	docker build --tag tendermint/nonvalidator nonvalidator
.PHONY: build-nonvalidator

