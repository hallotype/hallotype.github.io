from os.path import basename
import os
import glob
"""
look into BASE64 folder
populate fontcss @font-faces
populate html

TODO:
- support ufo
  > compile otf on build 
"""

fontFolder = "compiledFonts/BASE64/"
validFontExtensions = {"otf": "opentype",
                       "ttf": "truetype",
                       "woff2": "woff2",
                       "woff": "woff",
                       "b64": "base64"}


fontCss = ""
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
    print(font)
    path = basename(font)
    items = os.path.splitext(path)
    fontname = items[0]
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
    print('test')


fontcssFile = open("site/css/fontcss.css", "w+")
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
