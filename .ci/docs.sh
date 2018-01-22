#!/usr/bin/env bash

set -ex

make build
virtualenv env
source env/bin/activate
pip install -r requirements.txt
make docs
cp -r docs/build/. /home/kiwi/docs/avahi-client
