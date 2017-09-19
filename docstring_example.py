


'''

prerequisites

based on python 2.x
need python xxx module
make xxx command is in PATH

usage:
	1) change the variable: xxx, xxx
	2) thisscript.py arg1 arg2 arg3

process:
	1) step 1
	2) step 2
	3) step 3

know issues
	1) issue1
	2) issue2

other
	Any issues or improvements please contact jiangbingo@hotmail.com


'''


import sys 

def loop(): pass

if __name__ =="__main__":
	print len(sys.argv)
	for i in sys.argv:
		print i 

	if not len(sys.argv)==4:
		print __doc__
	else:
		loop()