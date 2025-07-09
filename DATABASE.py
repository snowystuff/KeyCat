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

chunk = 16
tk = b"0Qm3dfrB9K81TqKroirdp9Sw3ZwfXFl4EuipKP1Ahn0="

def now():
    return int(time.time())

def emptyDatabase():
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
    for i in table:
        t=table[i].get('t') or default
        v=table[i].get('v') or ""
        ct=str(table[i].get('ct') or now())
        at=str(table[i].get('at') or "")
        data+=i+sep+t+sep+v+sep+ct+sep+at+new
    chunks = [data[i:i + chunk] for i in range(0, len(data), chunk)]
    
    emptyDatabase()
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
    except:
        raise Exception("Error with database file.")

    print(string)
    

def set(k,t=default,v=None):
    global table
    d = {'t':str(t) or default}
    if v:
        d |= {'v':str(v)}
    table[k] = d
    table = dict(sorted(table.items()))
    return

def get(k):
    return table[k]
