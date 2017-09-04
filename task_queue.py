# coding=utf-8

import threading
from time import ctime,sleep

def music(func):
	for i in range(2):
		print "I was listening to %s.%s"%(func,ctime())
		sleep(1)

def movie(func):
	for i in range(2):
		print "I was listening to %s.%s"%(func,ctime())

		sleep(3)

threads = []
t1 = threading.Thread(target=music,args=(u"music"))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u"movie"))
threads.append(t2)

if __name__ == '__main__':
	print threads
	for t in threads:
		t.setDaemon(True)
		t.start()
	print "all over %s"%ctime()


