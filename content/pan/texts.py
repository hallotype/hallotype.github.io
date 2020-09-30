title = 'Pan'

tags = '''type
variable
experiment'''

description = '''Pan is a variable type system. The idea is to slice the glyphs in various ways and draw contours with the slice-data. <br>
Since the drawings are not compatible, featureSubstitutions are needed. Currently three axes [Angle, Steps, Shape] controle what glyph is shown. A special set of tools was needed to create the GSUB table that can handle this.<br><br>

	I started creating this font system in 2017. Back then, in MacOS, only one axis was working for featureSubstitutions. Now in 2020, it seems that it is still not fully solved in MacOS. In browsers it all works prefectly!
'''

from collections import OrderedDict
sd = OrderedDict()
sitecontent = OrderedDict()
sitecontent["cover.png"] = "some text"
sitecontent["SWITCH.gif"] = "some text"
sitecontent['clock.html'] = "hoi"
sitecontent["flowchart.html"] = "hoi" 
sitecontent["varPlay.html"] = "hoi" 


