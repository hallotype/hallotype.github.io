from os.path import basename
import os
import glob

from getAxes import getAxes
from checkCharSets import checkCharSets

# process the fonts
os.system("sh processFonts.sh")
fontsAxes = getAxes()
charSets = checkCharSets()

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
<p contenteditable="true" class="{fontname}{extraClasses}">OHamburgefonstiv</p>
"""
slidersScript = ""
sliderTemplate = """
const {fontname}{tag} = document.querySelector("#{fontname}{tag}");
{fontname}{tag}.addEventListener("mousemove", (event) => [
  let parent = document.querySelector(".{fontname}");
  parent.style.cssText = "font-variation-settings: '{tag}' " + {fontname}{tag}.value;
]);
"""

for font in glob.glob(fontFolder+"**"):
    if font.split(".")[-1] not in validFontExtensions:
        continue
    # print(font)
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
    aff = aff.replace("[", "{")
    aff = aff.replace("]", "}")
    fontCss += aff
    extraClasses = ""
    if fontname in charSets:
        extraClasses = " "
        for extraClass in charSets[fontname]:
            extraClasses += extraClass
    typebody += htmlThing.format(fontname=fontname, extraClasses=extraClasses)
    if fontname in fontsAxes:
        typebody += "<div id='sliders-" + fontname + "'>"
        slidersScript += 'var %s_dragging = false;\n' % fontname
        slidersScript += 'const %sSliders = document.querySelector("#sliders-%s");\n' % (
            fontname, fontname)

        for ax in fontsAxes[fontname]:
            typebody += "<input type='range' class='ax' min='%s' max='%s' value='%s' id=%s%s>%s " % (
                ax['min'], ax['max'], ax['def'], fontname, ax['tag'],  ax['tag']
            )
            # slider = sliderTemplate.format(
            #     fontname=fontname,
            #     tag=ax['tag']
            # )
            # slider = slider.replace("[", "{")
            # slider = slider.replace("]", "}")
            # slidersScript += slider
            slidersScript += 'const %s%s = document.querySelector("#%s%s");\n' % (
                fontname, ax['tag'], fontname, ax['tag'],)

        typebody += "</div>"

        slidersScript += """
        %sSliders.addEventListener("mousedown", (event) => {
          %s_dragging = true;
        });
        %sSliders.addEventListener("mouseup", (event) => {
          %s_dragging = false;
        });
        """ % (fontname, fontname, fontname, fontname)

        for ax in fontsAxes[fontname]:
            slidersScript += """
%s%s.addEventListener("mousemove", (event) => {
  if (%s_dragging) {
    let parent = document.querySelector(".%s");
    parent.style.cssText =
      "font-variation-settings:" +
          """ % (fontname, ax['tag'], fontname, fontname)

            for i, ax_ in enumerate(fontsAxes[fontname]):
                if i == 0:
                    slidersScript += '''"'%s' " + %s%s.value''' % (
                        ax_['tag'], fontname, ax_['tag'])
                else:
                    slidersScript += '''+",'%s' " + %s%s.value''' % (
                        ax_['tag'], fontname, ax_['tag'])
            slidersScript += ";}});"

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

slidersScriptFile = open("js/script.js", "w+")
slidersScriptFile.write(slidersScript)
slidersScriptFile.close()
