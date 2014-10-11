#!/bin/bash

cat /dev/urandom | tr -dc a-z0-9 | head -c 1000
