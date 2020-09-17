import glob
import os
import importlib
from importlib.machinery import SourceFileLoader
import string
import random

# gen proj page
def generateProjectPage(project):
	print(project['path'])
	print((project['texts'].description))
	
	link = project['texts'].title.replace(" ","") + ".html"
	proj = open(link, 'w+')
	projHtml = str(projHtmlTemp)
	content = ""
	if project['content']:
		for index, img in enumerate(project['content']):
			# first image
			content += """<img src='%s/%s'/>\n"""%(project['path'],img)
			# then description
			if index == 0 and project['texts'].description:
				content += """<p class="description">%s</p>\n""" % project['texts'].description
			# then more images
			# then more images

	projHtml = projHtml.format(
					title = project['texts'].title,
					header = headerFileTxt,
					project = content)
	proj.write(projHtml)
	proj.close()



# load templates

headerFile = open("header.html", "r")
headerFileTxt = headerFile.read()
headerFile.close()

projTem = open("templateProjectItem.html", "r")
projTemp = projTem.read()
projTem.close()

projHtmlTem = open("templateProjectHtml.html", "r")
projHtmlTemp = projHtmlTem.read()
projHtmlTem.close()

# get content order
order = open('order','r').read().split("\n")
projects = ""

# get contents
for index, o in enumerate(order):
	path = os.path.join("content",o)
	if os.path.exists(path):
		#print (path)

		cover = glob.glob(path+"/cover*")
		if cover:
			cover = cover[0]
		# print(cover)
	
		# if there is no cover, skip the project!
		if not cover: continue


		textsPath = os.path.join(path,"texts.py")
		
		projectTexts = SourceFileLoader(string.ascii_letters[index], textsPath).load_module()
		content = {}
		if hasattr(projectTexts, "sitecontent"):
			content = projectTexts.sitecontent

		project = {
			"texts": projectTexts,
			"cover": cover,
			"path": path,
			"content": content,
		}

		generateProjectPage(project)



		# make homepage items


		tags = "<ol>"
		for tag in projectTexts.tags.split("\n"):
			tags+="<li>%s</li>"%tag
		tags+="</ol>"

		link = projectTexts.title.replace(" ","") + ".html"


		

		projectTxt = projTemp.format(
										cover = cover,
										link = link,
										title = projectTexts.title,
										tags =  tags
		)
		projects += projectTxt

	
htmlFile = open("templateindex.html", "r")
htmlFileTxt = htmlFile.read()
htmlFile.close()



htmlIndex = open("index.html", "w+")
htmlIndex.write(htmlFileTxt.format(
							# fontcsses=fontcsses,
                        	header=headerFileTxt,
                        	projects = projects
                        	)
        )
htmlIndex.close()
