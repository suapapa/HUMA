#!/bin/bash

ARDUINO_BOARD="diecimila"

# Programmer specific flags
#AVRDUDE_OPTS="-cstk200 -pm8 -P/dev/parport0"
AVRDUDE_OPTS="-cstk500 -P/dev/ttyUSB0"

AVRDUDE="avrdude"
$AVRDUDE $AVRDUDE_OPTS `./arduino_bootloader_fuse_flags.py $ARDUINO_BOARD`
