import os
import time
from cryptography.fernet import Fernet

from DIR import *
from CONFIG import *

conf = Config()

table = {}
keyPath = os.path.join(appDir, conf.get("key"))

sep = ','
new = ';'

chunk = 65536
tk = b"0Qm3dfrB9K81TqKroirdp9Sw3ZwfXFl4EuipKP1Ahn0="

def now():
    return int(time.time())

def empty():
    try:
        with open(dbFile,'w') as file:
            file.close()
    except FileNotFoundError:
        os.makedirs(os.path.dirname(dbFile), exist_ok=True)
        with open(dbFile,'w') as file:
            file.close()

f = Fernet(tk)

def write():
    global table
    data=""
    for i,va in enumerate(table):
        t=table[va].get('t') or default
        v=table[va].get('v') or ""
        ct=str(table[va].get('ct') or now())
        at=str(table[va].get('at') or "")
        n = new
        if i == 0:
            n = ""
        data+=n+va+sep+t+sep+v+sep+ct+sep+at
    chunks = [data[i:i + chunk] for i in range(0, len(data), chunk)]
    
    empty()
    try:
        with open(dbFile,'ab') as file:
            for i,v in enumerate(chunks):
                enc = f.encrypt(v.encode())
                dat = enc
                if i > 0:
                    dat = b'\x00' + enc
                file.write(dat)
            file.close()
    except:
        raise Exception("Error with database file.")

def read():
    global table

    string = ""
    try:
        with open(dbFile,'rb') as file:
            data = file.read()
            chunks = data.split(b'\x00')
            for i in chunks:
                dec = f.decrypt(i).decode()
                string += dec
            file.close()
    except FileNotFoundError:
        os.makedirs(os.path.dirname(dbFile), exist_ok=True)
        with open(dbFile,'w') as file:
            file.close()
    except:
        raise Exception("Error with database file.")

    keyInfo = string.split(new)
    for val in keyInfo:
        i=val.split(sep)
        table[i[0]] = {'t':i[1],'v':i[2],'ct':i[3],'at':i[4]}
    

def set(k,t=default,v=None,ct=now(),at=None):
    global table
    d = {'t':str(t) or default,'ct':str(ct or now())}
    if v:
        d |= {'v':str(v)}
    table[k] = d
    table = dict(sorted(table.items()))
    return

def get(k):
    return table.get(k)

read()
