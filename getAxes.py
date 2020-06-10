import glob
import os
from fontTools.ttLib import TTFont


def getAxes():
    fonts = {}
    for ttf in glob.glob("fonts/**.ttf"):
        ftf = TTFont(ttf)
        fontname = os.path.basename(ttf)[:-4]
        axes = []
        # print(fontname)
        if 'fvar' in ftf.keys():
            axes = []
            for axis in ftf['fvar'].axes:
                a = {}
                a['tag'] = axis.axisTag
                a['min'] = axis.minValue
                a['def'] = axis.defaultValue
                a['max'] = axis.maxValue
                axes.append(a)
        if axes:
            fonts[fontname] = axes
    # d = open("axes", "w+")
    # d.write(str(fonts))
    # d.close()
    return fonts
