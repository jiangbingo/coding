#-*- encoding:utf-8 -*-
from Tkinter import*
import socket
import time
import threading


class TCP(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server = ('113.251.175.168',8080)
        self.data = ''
    def run(self):
        sock.connect(self.server)
        label['text'] = 'connect success........'
        button1['state'] = 'disabled'
        button2['state'] = 'normal'
        self.data = sock.recv(1024)
        while True:
            self.data = sock.recv(1024)
            if not self.data:
                break
            else:
                print self.data
        te.set(self.data) 

def on_click_Connect():
    thread_tcp.start()
    time.sleep(1)#确保线程被启用 

def on_click_Stop():
    sock.close()
    button2['state'] = 'disabled'
    button1['state'] = 'normal'
    te.set('')
    label['text'] = 'break........'




sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
thread_tcp = TCP()
root = Tk(className = 'TCP Communication')
label = Label(root,text = '......')
label.pack()
te = StringVar()
te.set('')
entry = Entry(root,textvariable = te).pack()
button1 = Button(root,text = 'Connect',command = on_click_Connect)
button1.pack()
button2 = Button(root,text = 'Stop',command = on_click_Stop,state = 'disabled')
button2.pack()
root.mainloop()
