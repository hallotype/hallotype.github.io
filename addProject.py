from time import strftime
import os
import sys

text = """title = 'name'

tags = '''type
variable
experiment'''

description = '''Something something something'''

"""

def addProject(folder):
	os.mkdir("content/%s"%folder)

	t = open("content/%s/texts.py"% folder, "w+")
	t.write(text)
	t.close()

addProject(folder=sys.argv[1])