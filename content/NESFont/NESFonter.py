"""
Make a font from binary data, such as NES games!
https://hallotype.github.io/nesfonts.html

Thom Janssen, HalloType, 2020
thom@hallotype.nl
License MIT 

@thomhendrik
"""

# run in RoboFont

from drawBot import BezierPath
from math import floor
from glyphNameFormatter import GlyphName

rom = "path/to/Super Mario Bros..nes"
glyphOrder = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ @@@-×@!" # @=ignore


pixelSize = 100
HEX = "9010"


with open(rom, 'rb') as romFile:
    fnt = romFile.read()

# Make a new font
nf = NewFont("NES")

# convert the hex value to decimal
start = int(HEX, 16)

amount = len(glyphOrder)*2 # x2 because of the empty sprites inbetween

for i in range(amount):
    if i%2!=0:continue # skip those empty inbetweens
    
    # we draw pixels upwards on a rows and than decrement the row.
    y = pixelSize*7 
    
    name = GlyphName(ord(glyphOrder[floor(i/2)])).getName()
    if name == "at" : continue

    # ng = new glyph
    ng = nf.newGlyph(name)
    ng.autoUnicodes() # add unicode
    ng.width = pixelSize*8
    
    for b in fnt[start+(i*8):start+((i+1)*8)]: # fetch a byte
        c = ("{0:b}".format(b).zfill(8))       # int to binary
        for x,bit in enumerate(c):             # loop the bits
            if bit == "1": # <-- make it "0" to make a cameo font
                path = BezierPath()
                path.rect(x*pixelSize,y,pixelSize,pixelSize)
                
                # draw the path in the glyph
                pen = ng.getPen()
                path.drawToPen(pen)
                
            # we dont draw white pixels...
        
        y-=pixelSize # decrement row

        
    