from collections import OrderedDict
title = 'Pan'

tags = '''type
variable
experiment'''

description = '''Pan is a variable type system. The idea is to slice the glyphs in various ways and draw contours with the slice-data. <br>
Since the drawings are not compatible, featureSubstitutions are needed. Currently three axes [Angle, Steps, Shape] controle what glyph is shown. A special set of tools was needed to create the GSUB table that can handle this.<br><br>

'''

sd = OrderedDict()
sitecontent = OrderedDict()
sitecontent["cover.png"] = "some text"
sitecontent['coretext.html'] = 'ct'
sitecontent["SWITCH.gif"] = "some text"
sitecontent['clock.html'] = "hoi"
sitecontent['angler.html'] = "angles"
sitecontent["flowchart.html"] = "hoi"
sitecontent["varPlay.html"] = "hoi"
