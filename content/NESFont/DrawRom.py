"""
Plot binary data, especially old game ROMs like NES games.
You have to have your own rom files. I dont support piracy.

Thom Janssen, HalloType, 2020
thom@hallotype.nl

MIT License
"""

import os
import sys
from drawBot import *

def drawROM(rom=None, pxl=10, rows=16):
    if rom == None:
        # dummy ROM
        rows=2
        data = b'\x3C\x7E\x62\x62\x7E\x62\x62\x00\x83\x9D\x9D\x83\x9D\x9D\x83\xFF\xC3\x9D\x9F\x9F\x9F\x9D\xC3\xFF\x7C\x62\x62\x62\x62\x62\x7C\x00'
        numOfSprites = 4

    else:
        romfile = open(rom, 'rb')
        data = romfile.read()
        romfile.close()

        numOfSprites = ceil(os.stat(rom).st_size/8)
    
    print("Number of sprites:",numOfSprites)


    cols = numOfSprites / rows

    newPage(cols*pxl*8, rows*pxl*8)
    fill(.95,.95,.95)
    rect(0,0,cols*pxl*8, rows*pxl*8)

    y = rows*pxl*8-pxl
    lineCount=0

    for i in range(numOfSprites):
        for b in data[i*8:(i+1)*8]:
    
            c = ("{0:b}".format(b).zfill(8))
            for x,bit in enumerate(c):
                if bit == "1":
                    fill(0)
                    rect(x*pxl,y,pxl,pxl)
            y-=pxl
            lineCount +=1
            if (lineCount/8)%rows == 0:
                y = rows*pxl*8-pxl
                translate(8*pxl)


    # saveImage("YourRom.png") 

drawROM()
