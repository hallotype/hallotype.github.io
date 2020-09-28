import sys
import os
import glob

from os.path import basename

from getAxes import getAxes
from checkCharSets import checkCharSets

pw = open("fonts/preferredWords.py", "r")
pwContent = pw.read()
preferredWords = eval(pwContent)
pw.close()
# print(preferredWords)


# process the fonts
os.system("sh processFonts.sh")
fontsAxes = getAxes()
charSets = checkCharSets()
print(charSets)


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
thefonts = ""
lineview = ""
gridview = ""

AtFontFace = u"""
@font-face [
  font-family: "{fontname}";
  src:url(data:font/woff2;base64,{b64});
]
.{fontname} [
  font-family: "{fontname}";
]
"""

lineViewTemplate = """
<p contenteditable="true" class="lineView">%s</p>
"""
gridViewTemplate = """
<p contenteditable="true" class="gridView invisible">%s</p>
"""


slidersScript = ""
slidersScript_all = ""
sliderTemplate = """
const {fontname}Sliders = document.querySelector("#sliders-{fontname}");
{fontname}Sliders.oninput = {fontname}Changer;
function {fontname}Changer(e) [
  let fontElements = document.querySelectorAll("div.{fontname}");
  fontElements.forEach(function (fontElement) [
    fontElement.style.cssText =
      "font-variation-settings:" +
"""

for font in glob.glob(fontFolder+"**"):
    if font.split(".")[-1] not in validFontExtensions:
        continue
    fontCss = ""

    path = basename(font)
    items = os.path.splitext(path)
    fontname = items[0]
    # print("fontname", fontname)
    extension = items[-1][1:]

    file = open(font, 'r')
    b64 = file.read()
    file.close()

    # type = validFontExtensions[extension]
    aff = (AtFontFace.format(fontname=fontname, b64=b64))
    aff = aff.replace("[", "{").replace("]", "}")
    fontCss += aff

    extraClasses = ""
    if fontname in charSets:
        extraClasses = " "
        for extraClass in charSets[fontname]:
            extraClasses += extraClass

    fontItem = "<div class='fontItem lineView {fontname}{extraClasses}'>".format(
        fontname=fontname, extraClasses=extraClasses)

    lineContent = "OHamburgefonstiv"
    gridContent = "A"

    if fontname in preferredWords:
        if 'line' in preferredWords[fontname]:
            lineContent = preferredWords[fontname]['line']
        if 'grid' in preferredWords[fontname]:
            gridContent = preferredWords[fontname]['grid']

    fontItem += lineViewTemplate % lineContent
    fontItem += gridViewTemplate % gridContent
    varSup = ""
    slidersScript = ""
    if fontname in fontsAxes:
        varSup = "<div class='varSup' style='text-transform: capitalize;' id='sliders-" + fontname + "'>"
        slidersScript = sliderTemplate.format(fontname=fontname)
        slidersScript = slidersScript.replace("[", "{").replace("]", "}")
        for i, ax in enumerate(fontsAxes[fontname]):

            varSup += """<input type='range' class='ax' min='{min}' max='{max}' value='{default}' name='{fontname}{tag}' id='{fontname}{tag}'><label for='{fontname}{tag}'>{name}</label><br>""".format(
                min=ax['min'],
                max=ax['max'],
                default=ax['def'],
                fontname=fontname,
                tag=ax['tag'],
                name=ax['name']

            )

            if i == 0:
                slidersScript += '''"'{tag}' " + document.querySelector("#{fontname}{tag}").value\n'''.format(
                    tag=ax['tag'], fontname=fontname)
            else:
                slidersScript += '''+",'{tag}' " + document.querySelector("#{fontname}{tag}").value\n'''.format(
                    tag=ax['tag'], fontname=fontname)
        slidersScript += "  });}"
        varSup += "</div>"
        fontItem += varSup
    fontItem += "</div>"
    thefonts += fontItem

    fontcssFile = open("css/%s.css" % fontname, "w+")
    fontcssFile.write(fontCss)
    fontcssFile.close()

    fontcsses += templateCss % fontname

    slidersScript_all += slidersScript

    vu = open('varUnits/%s.html' % fontname, "w+")
    c = "<link rel='stylesheet' href='type/css/%s.css'/>\n" % fontname
    c += "<div class='{fontname}{extraClasses}' id='varUnit'>\n".format(
        fontname=fontname, extraClasses=extraClasses)
    c += lineViewTemplate % lineContent
    c += varSup
    c += "\n<script>%s</script>\n" % slidersScript
    c += "</div>\n"
    vu.write(c)
    vu.close()

htmlFile = open("templateindex.html", "r")
htmlFileTxt = htmlFile.read()
htmlFile.close()

headerFile = open("header.html", "r")
headerFileTxt = headerFile.read()
headerFile.close()

# print(lineview)


htmlIndex = open("fonts.html", "w+")
htmlIndex.write(htmlFileTxt.format(fontcsses=fontcsses,
                                   header=headerFileTxt,
                                   thefonts=thefonts,)
                )
htmlIndex.close()

slidersScriptFile = open("js/varSupport.js", "w+")
slidersScriptFile.write(slidersScript_all)
slidersScriptFile.close()
