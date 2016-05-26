#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Winner Logic module.
"""
__author__		=	"Yuval Pruss"
__copyright__	= 	"Copyright 2016, The Winner Project"

class WinnerLogic(object):
	def groupTeamsByGames(self, teamsArr):
		returnArr = []
		counter = 1
		teamCount = 1
		new = True
		for x in teamsArr:
			if new:
				returnArr.append(counter)
				new = False
			else:
				if teamCount == 3:
					new = True
					teamCount = 0
					returnArr.append(counter)
					counter += 1
				else:
					if "x‬" in x:
						returnArr.append(counter)
					else:
						new = True
						teamCount = 0
						returnArr.append(counter)
						counter += 1
			teamCount += 1
		return returnArr

if __name__ == '__main__':
	pass