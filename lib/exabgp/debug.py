# encoding: utf-8
"""
debug.py

Created by Thomas Mangin on 2011-03-29.
Copyright (c) 2009-2015 Exa Networks. All rights reserved.
"""

import os
import sys
from exabgp.util.panic import panic
from exabgp.util.panic import footer

def bug_report (type, value, trace):
	print panic

	import traceback

	print "-- Traceback\n\n"
	traceback.print_exception(type,value,trace)

	from exabgp.logger import Logger
	logger = Logger()

	print "\n\n-- Configuration\n\n"
	print logger.config()
	print "\n\n-- Logging History\n\n"
	print logger.history()
	print "\n\n\n"

	print footer


def intercept (type, value, trace):
	bug_report(type, value, trace)
	if os.environ.get('PDB',None) not in [None,'0','']:
		import pdb
		pdb.pm()

def setup_report ():
	sys.excepthook = intercept
