    # with open('event.log','r') as fe:
    #     fe.readlines()

import os

with open('event.log','a') as f:
f.write(str(severity)+str(msg) + os.linesep)
# f.write("".join(str(msg)) + os.linesep)



 [loggers]
keys=root,models

[handlers]
keys=nbs,eventHandler

[formatters]
keys=default

[logger_root]
level=DEBUG
handlers=nbs

[logger_event]
level=DEBUG
handlers=eventHandler

[handler_nbs]
class=handlers.NbsFileHandler
level=DEBUG
formatter=default
args=('nbs.log', 'a')

[handler_eventHandler]
class=logging.handlers.EventFileHandler
level=DEBUG
formatter=default
args=('event.log', 'a',1000)


[formatter_default]
format=%(asctime)s %(name)s T[%(threadName)s] %(levelname)8s %(message)s
datefmt=
class=logging.Formatter


# -*- coding:  utf-8 -*-
#!/usr/bin/env python

from bottle import route,get, post, request
from models import Events


login_form='''<form action="/login" method="post">
             Username: <input name="username" type="text" />
             Password: <input name="password" type="password" />
             <input value="Login" type="submit">
           </form>
'''
def check_login(username, password):
    if username == 'nbsadmin' and password == '123456':
        return True
    else:
        return False

@route('/login')
def login():
    return login_form

@route('/login',method = 'POST')
def do_login():
        username = request.forms.get('username','').strip()  # username
        password = request.forms.get('password','').strip()  # password

        if check_login(username,password):
            Events.log_info(' "%s" load in' % username)
            return '<p> log in succeed </p>'
        else:
            return '<p>please check your username and password</p>'

        # import ipdb;ipdb.set_trace()


        # # self.logger = logging.getLogger(logger)
        # fmter = logging.Formatter(fmt="%(asctime)s %(message)s",datefmt="%Y-%m-%d %H:%M:%S")

        # fevent = logging.filehandler(filename='event.log',encoding="utf-8")
        # fevent.setFormatter(fmter)
        # fevent.setLevel()
        # # print to the CMD
        # console = logging.StreamHandler()
        # console.setFormatter(fmter)
        # console.setLevel(logging.DEBUG)
