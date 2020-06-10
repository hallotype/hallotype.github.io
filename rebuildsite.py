from os.path import basename
import os
import glob

from getAxes import getAxes

# process the fonts
os.system("sh processFonts.sh")
fontsAxes = getAxes()

# print(fontsAxes)

"""
look into BASE64 folder
populate fontcss @font-faces
populate html

"""

fontFolder = "compiledFonts/BASE64/"
validFontExtensions = {"otf": "opentype",
                       "ttf": "truetype",
                       "woff2": "woff2",
                       "woff": "woff",
                       "b64": "base64"}

fontcsses = ""
templateCss = '<link rel="stylesheet" href="css/%s.css" />\n'
typebody = ""

AtFontFace = u"""
@font-face [
  font-family: "{fontname}";
  src:url(data:font/woff2;base64,{b64});
] 
.{fontname} [
  font-family: "{fontname}";
]
"""

htmlThing = """
<p contenteditable="true" class="{fontname}">OHamburgefonstiv</p>
"""

for font in glob.glob(fontFolder+"**"):
    if font.split(".")[-1] not in validFontExtensions:
        continue
    # print(font)
    fontCss = ""

    path = basename(font)
    items = os.path.splitext(path)
    fontname = items[0]
    #print("fontname", fontname)

    extension = items[-1][1:]
    file = open(font, 'r')
    b64 = file.read()
    file.close()
    # type = validFontExtensions[extension]
    aff = (AtFontFace.format(fontname=fontname, b64=b64))
    aff = aff.replace("[", "{")
    aff = aff.replace("]", "}")
    fontCss += aff
    typebody += htmlThing.format(fontname=fontname)
    if fontname in fontsAxes:
        for ax in fontsAxes[fontname]:
            typebody += "<input type='range' class='ax' min='%s' max='%s' value='%s'>%s" % (
                ax['min'], ax['max'], ax['def'], ax['tag'])
        typebody += "<div class='clear'></div>"

    fontcssFile = open("css/%s.css" % fontname, "w+")
    fontcssFile.write(fontCss)
    fontcssFile.close()

    fontcsses += templateCss % fontname

htmlFile = open("templateindex.html", "r")
htmlFileTxt = htmlFile.read()
htmlFile.close()

headerFile = open("header.html", "r")
headerFileTxt = headerFile.read()
headerFile.close()

print(typebody)

htmlIndex = open("index.html", "w+")
htmlIndex.write(htmlFileTxt.format(fontcsses=fontcsses,
                                   header=headerFileTxt,
                                   typebody=typebody,)
                )
htmlIndex.close()
