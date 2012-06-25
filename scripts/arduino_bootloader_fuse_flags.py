#!/usr/bin/python

import os
import sys
import re

ARDUINO_HOME = "/usr/share/arduino/"
ARDUINO_CONF = ARDUINO_HOME + "hardware/arduino/boards.txt"
ARDUINO_BOOT = ARDUINO_HOME + "hardware/arduino/bootloaders/"

def getBoardPrefs(boardName):
    ptnBoard = re.compile(r'^(.*)\.name=(.*)')
    prefs = {}
    for line in open(ARDUINO_CONF):
        line = line.strip()
        if line.startswith(boardName + '.'):
            k, v = line.split('=')
            k = k[len(boardName) + 1:]
            prefs[k] = v

    if not prefs:
        print("%s not found!"%boardName)
        print("you may edit %s to add a new board."%ARDUINO_CONF)

    return prefs

def avrdudeFlags(boardPrefs):
    flags = []
    flags.append("-p%s"%boardPrefs["build.mcu"])
    flags.append("-e")
    if "bootloader.unlock_bits" in boardPrefs.keys():
        flags.append("-Ulock:w:%s:m"%boardPrefs["bootloader.unlock_bits"])
    if "bootloader.extended_fuses" in boardPrefs.keys():
        flags.append("-Uefuse:w:%s:m"%boardPrefs["bootloader.extended_fuses"])
    flags.append("-Uhfuse:w:%s:m"%boardPrefs["bootloader.high_fuses"])
    flags.append("-Ulfuse:w:%s:m"%boardPrefs["bootloader.low_fuses"])

    bootloaderPath = os.path.join(ARDUINO_BOOT,
                                  boardPrefs["bootloader.path"],
                                  boardPrefs["bootloader.file"])
    flags.append("-Uflash:w:%s:i"%bootloaderPath)

    if "bootloader.lock_bits" in boardPrefs.keys():
        flags.append("-Ulock:w:%s:m"%boardPrefs["bootloader.lock_bits"])

    return " ".join(flags)



if __name__ == "__main__":
    boardPrefs = getBoardPrefs(sys.argv[1])
    #print boardPrefs
    print avrdudeFlags(boardPrefs)
