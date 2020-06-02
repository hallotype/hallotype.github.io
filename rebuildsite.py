from os.path import basename
import os
import glob
"""
look into font folder
populate fontcss @font-faces
populate html

TODO:
- support ufo
  > compile otf on build 
"""

fontFolder = "site/fonts/"
validFontExtensions = {"otf": "opentype",
                       "ttf": "truetype", "woff2": "woff2", "woff": "woff"}


fontCss = ""
typebody = ""

AtFontFace = u"""
@font-face [
  font-family: "{fontname}";
  src: url("{path}") format("{type}");
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
    path = basename(font)
    items = os.path.splitext(path)
    fontname = items[0]
    extension = items[-1][1:]
    type = validFontExtensions[extension]
    aff = (AtFontFace.format(path=path, type=type, fontname=fontname))
    aff = aff.replace("[", "{")
    aff = aff.replace("]", "}")
    fontCss += aff
    typebody += htmlThing.format(fontname=fontname)


fontcssFile = open(fontFolder+"/fontcss.css", "w+")
fontcssFile.write(fontCss)
fontcssFile.close()

htmlFile = open("templateindex.html", "r")
htmlFileTxt = htmlFile.read()
htmlFile.close()

headerFile = open("header.html", "r")
headerFileTxt = headerFile.read()
headerFile.close()


htmlIndex = open("site/index.html", "w+")
htmlIndex.write(htmlFileTxt.format(header=headerFileTxt, typebody=typebody))
htmlIndex.close()
