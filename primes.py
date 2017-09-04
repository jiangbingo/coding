# !/usr/bin/env python
# -*- encoding:utf-8 -*-

def deprecated(replacement):
    def deprecated(func):
        warning_msg="**WARN** keyword '%s' is deprecated,use '%s' instead"%(func.func_name,replacement)

        def _wrapped(*args,**kwargs):
            print(warning_msg)
            return func(*args,**kwargs)

        _wrapped.func_doc = warning_msg
        _wrapped.func_name = func.func_name

        return _wrapped
    return deprecated

class example(object):
        
    def foo():
        pass


        
