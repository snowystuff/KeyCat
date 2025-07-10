import os
import argparse
import sys

from CONFIG import *

from DIR import *
import DATABASE

conf = Config()

def get(table,index):
    try:
        return table[index]
    except:
        return

def gen(t=default,c=1): # GENERATE (type, count) -> Key List
    t=t or default
    c=c or 1
    for i in range(c):
        print(DATABASE.gen())
    DATABASE.write()

def dl(K): # DELETE (KEY)
    pass

def cl(cl,t): # CLEAR, CLEAR UNUSED, CLEAR DEACTIVATED (type)
    pass

def act(K,V): # ACTIVATE (KEY, VALUE)
    pass

def ver(K,V): # VERIFY (KEY, VALUE) -> Boolean
    pass

def dac(K): # DEACTIVATE (KEY)
    pass

def ls(ls,t,c,i): # LIST, LIST UNUSED, LIST DEACTIVATED, LIST ACTIVATED (type, count, index) -> Key List
    pass

def kts(K,T): # KEY TYPE SET (KEY, TYPE)
    pass

def ktg (K): # KEY TYPE GET (KEY) -> Type
    pass

def tp(): # TYPE
    pass

arg = sys.argv
if len(arg) > 1:
    cmd = arg[1].lower()
    if cmd == "gen":
        t = None
        c = None
        if typeFlag in arg:
            idx = arg.index(typeFlag)
            t = arg[idx+1]
        if countFlag in arg:
            idx = arg.index(countFlag)
            c = int(arg[idx+1])
        gen(t,c)
    elif cmd == "ls" or cmd == "lsu" or cmd == "lsd":
        t = None
        c = None
        i = False
        
else: # return help info
    pass
