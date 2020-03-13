#!/bin/sh
docker run --privileged --restart=always -it  -p 7735:7735 -v --device=/dev/spidev0.0 --name st7735s promethee/rpi.web.st7735s:latest
