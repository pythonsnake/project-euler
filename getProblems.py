# -*- coding: utf-8 -*-
"""
Get the problems and store them in problem{number}.py as Docstrings
"""
import sys
import urllib
import lxml
import lxml.html

min=int(sys.argv[1])
max=int(sys.argv[2])

if min>max: print "No"
while max>=min:
	source = urllib.urlopen('http://projecteuler.net/problem={0}'.format(str(min))).read()
	tree = lxml.html.document_fromstring(source)
	problem = tree.xpath("//div[@class='problem_content']")[0].text_content().strip().capitalize().encode("utf-8")
	name = "problem{0}.py".format(min)

	with open(name, "w") as x:
		x.write('"""\n{0}\n"""'.format(problem))
	min+=1