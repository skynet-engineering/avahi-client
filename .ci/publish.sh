#!/usr/bin/env bash

set -ex

PYPI_ROOT=/home/kiwi/pypi
PACKAGE=avahi-client

make build
mkdir -p ${PYPI_ROOT}/${PACKAGE}
cp dist/* ${PYPI_ROOT}/${PACKAGE}
