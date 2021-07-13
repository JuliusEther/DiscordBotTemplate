#!/bin/sh

pushd $(dirname $0)

mkdir -p logs
python src/main.py

popd