#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
HTML Site Scarping module.
"""
__author__		=	"Yuval Pruss"
__copyright__	= 	"Copyright 2016, The Winner Project"

from lxml import html
import requests

class Scarper(object):
	def __init__(self, site):
		self.site = site
	
	def scarpeSite(self):
		self.page = requests.get(self.site)
		self.tree = html.fromstring(self.page.content)
	
	def findElement(self, htmlElement, htmlClass, encodedResult= False):
		res = self.tree.xpath('//' + htmlElement + '[@class="' + htmlClass + '"]/text()')
		if encodedResult:
			for x in xrange(len(res)):
				res[x] = res[x].encode('utf8')
				res[x] = res[x].replace('\'', '\\\'');
		return res

if __name__ == '__main__':
	print "self.site -> The scarped site"
	print "self.tree -> The structer of the site"