title = 'piksels'

tags = '''type
pixel'''

description = '''This Piksels project is an idea for a variable system for pixels fonts.
All the pixel in the glyphs are components. And all the pixel-shapes are present as seperate glyphs.
A scripts builds the designspace according to the various pixel-shapes present and some parameters [ proportion, slant, rotation ], and all the needed sources are generated. Then the variable font can be generated.
In this example I have 6 alphabets, these are accessible via FeatureVariations. '''

from collections import OrderedDict
sd = OrderedDict()
sitecontent = OrderedDict()
sitecontent["cover.gif"] = "some text"
sitecontent["spectrum.gif"] = "some text"
sitecontent["DK2.gif"] = "some text"
sitecontent["CASTLE.gif"] = "some text"
sitecontent["fontOverview.png"] = "some text"


