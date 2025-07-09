import os
import argparse

from CONFIG import *

from DIR import *
import DATABASE

conf = Config()

def gen(t,c): # GENERATE (type, count) -> Key List
    pass

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

def ls(ls,t): # LIST, LIST UNUSED, LIST DEACTIVATED, LIST ACTIVATED (type)
    pass

def kts(K,T): # KEY TYPE SET (KEY, TYPE)
    pass

def ktg (K): # KEY TYPE GET (KEY) -> Type
    pass

def tp(): # TYPE
    pass

DATABASE.set("1234-0003","trial","username")
DATABASE.set("1234-0001")
DATABASE.set("1234-0002","month")

DATABASE.write()
DATABASE.read()
