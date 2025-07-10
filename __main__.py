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

def gen(t=default,c=0): # GENERATE (type, count) -> Key List
    t=t or default
    c=c or 0
    print(DATABASE.gen())

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

def ls(ls,t): # LIST, LIST UNUSED, LIST DEACTIVATED, LIST ACTIVATED (type) -> Key List
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
        t = get(arg,2)
        c = get(arg,3)
        gen(t,c)
    elif cmd == "dl":
        pass
else: # return help info
    pass
