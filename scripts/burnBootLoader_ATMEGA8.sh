#!/bin/bash

# may run this script with sudo
# this script burn bootloader for ATMEGA8 using NT-ISP(stk200), pararell programmer.
# following binay path is point contents from ubuntu package arduino.

BINARY=/usr/share/arduino/hardware/arduino/bootloaders/atmega8/ATmegaBOOT.hex
HFUSE=0xCA
LFUSE=0xDF

AVRDUDE_OPTS="-cstk200 -pm8 -P/dev/parport0"
#AVRDUDE_OPTS="-cstk500 -pm8 -P/dev/ttyUSB0"

avrdude $AVRDUDE_OPTS -e -u -Ulock:w:0x3f:m -Uefuse:w:0x00:m -Uhfuse:w:$HFUSE:m -Ulfuse:w:$LFUSE:m
avrdude $AVRDUDE_OPTS -Uflash:w:$BINARY:i -Ulock:w:0x0f:m
