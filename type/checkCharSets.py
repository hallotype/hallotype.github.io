import glob
import os
from fontTools.ttLib import TTFont


def checkCharSets():
    charsets = {}
    for font in glob.glob("fonts/**.*tf"):
        ftf = TTFont(font)
        fontname = os.path.basename(font)[:-4]
        glyphs = ftf['cmap'].buildReversed()
        if "a" not in glyphs:
            charsets[fontname] = ['noLowercase']
        if "A" not in glyphs:
            if fontname in charsets:
                charsets[fontname].append("noUppercase")
            else:
                charsets[fontname] = ['noUppercase']
    return charsets
