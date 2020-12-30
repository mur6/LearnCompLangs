#!/usr/bin/env bash

clang++ -O3 -Wall -shared -std=c++11 \
  -fPIC \
  `python -m pybind11 --includes` \
  -undefined dynamic_lookup example.cpp \
  -o example`python3-config --extension-suffix`
