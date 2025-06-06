import pdb
import os
def start_debug(n):
	if os.environ.has_key("DEBUG") and os.environ["DEBUG"] == n:
		pdb.set_trace()
def print_debug(level, msg):
	if os.environ.has_key("DEBUG_MSG") and os.environ["DEBUG_MSG"] == level:
		print "[%s] %s" %(level, msg)
