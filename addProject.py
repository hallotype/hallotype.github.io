from time import strftime
import os
import sys

text = """title = '%s'

tags = '''type
variable
experiment'''

description = '''Something something something'''

from collections import OrderedDict
sitecontent = OrderedDict()
sitecontent["cover.png"] = "some text"


"""

def addProject(folder):
	os.mkdir("content/%s"%folder)

	t = open("content/%s/texts.py"% folder, "w+")
	t.write(text%folder)
	t.close()

addProject(folder=sys.argv[1])