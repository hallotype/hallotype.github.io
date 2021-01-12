title = 'Quake'

tags = '''binary data
'''

description = '''While playing the iconic game Quake, I noticed the nice pixel typeface in the game. I was curious about how the typeface is stored in the source code and if I could extract the data and draw the font into a font editor. <br>
<br>
I found that the font was stored as a special texture, in a file with other textures. This 'CONCHAR' chunk of data is 16 kb. A grid of 128 x 128. Top left to top right and top to bottom. Every byte represents a color in the palette. <br>
Quakes color palette has 256 colors = 16 x 16 colors. Every row is a defined color, in this row are the shades of this color. This is smart system to easily create light and shadow effects. The palette is stored as an array of 256 x 3 bytes; 3 because RGB. <br><br>



'''

from collections import OrderedDict
sitecontent = OrderedDict()
sitecontent["cover.gif"] = "some text"
sitecontent["drawchars.html"] = "some text"


