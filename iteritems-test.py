# import iteritems

import threading
import  time


class  myThread(threading.Thread):
	"""docstring for  myThread"""
	def __init__(self, threadname):
		threading.Thread.__init__(self,name = threadname)

		self.st = 2

	def run(self):
		time.sleep(self.st)

		print self.getName()	


	def setSt(self,t):
		self.st = t


def fun1():
	t1.start()
	print 'func2 done'

def fun2():
	t2.start()
	print "fun2 done"


t1 = myThread('tttt1')
t2 = myThread('tttt2')

t2.setSt(3)
# t2.setDaemon(True)

fun1()
fun2()

print "now u will see me"
