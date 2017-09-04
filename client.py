# -*- encoding:utf-8 -*-
import threading, time
def doWaiting():
  print 'start waiting:', time.strftime('%H:%M:%S')
  # time.sleep(3)
  print 'stop waiting', time.strftime('%H:%M:%S')
thread1 = threading.Thread(target = doWaiting)
thread1.start()
time.sleep(1) #确保线程thread1已经启动
print 'start join'
thread1.join() #将一直堵塞，直到thread1运行结束。
print 'end join'
