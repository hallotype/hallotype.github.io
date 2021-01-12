title = 'Smart Type'

tags = '''features 
engineering'''

description = '''The idea to put smart stuff inside the font is an old idea. 
Still some things are in the settings of the text editor, graphic app, operation system, etc.
<br>
We, type designers, come up with all kind of ideas which require to educate our clients to put on, or off, some OpenType features.<br>
And we all know how that ends.
<br>
<br>

Here I show an idea how to make the font in charge of turning on or off OpenType features. <br>
<br>
<b>FSET table</b><br>
The idea is simple: add a new table to the font. This table has the default state of all the features in the font. FSET, for Feature Settings.
When the font is used, this table is read and the OpenType features are set. Now the font behaves just like the type designer intended.<br><br> 


'''

from collections import OrderedDict
sitecontent = OrderedDict()
sitecontent["cover.png"] = "some text"
sitecontent["example_smcp.html"] = "some text"
sitecontent["screenshotDB.png"] = "some text"


