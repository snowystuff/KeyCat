import os
import time
import string
from Crypto.Random import random
from cryptography.fernet import Fernet

from DIR import *
from CONFIG import *

conf = Config()

table = {}
keyPath = os.path.join(appDir, conf.get("key"))

masks = [
    "N", # Uppercase hex digit (0-F)
    "n", # Lowercase hex digit
    "I", # Digit (0-9)
    "i", # Non-lookalike digit
    
    "A", # Any letter (A-Z)
    "a", # Any non-lookalike letter
    "[", # Uppercase letter
    "]", # Non-lookalike uppercase letter
    "(", # Lowercase letter
    ")", # Non-lookalike lowercase letter
    
    "B", # Any alphanumeric
    "b", # Any non-lookalike alphanumeric
    "#", # Any non-lookalike alphanumeric (number bias)
    "{", # Uppercase alphanumeric
    "}", # Non-lookalike uppercase alphanumeric
    "^", # Non-lookalike uppercase alphanumeric (number bias)
    "<", # Lowercase alphanumeric
    ">", # Non-lookalike lowercase alphanumeric
    "*", # Non-lookalike lowercase alphanumeric (number bias)
    ]

nlookLetterU = 'ACDEFHJKLMNPQRTUVWXYZ' # S, O, I, G, B
nlookLetterL = 'abcdefhijkmnpqrstuvwxyz' # g, l, o

nlookDigit = '234789' # 0, 1, 5, 6
numberStrings = '0123456789'

sep = ','
new = ';'

chunk = 65536
tk = b"0Qm3dfrB9K81TqKroirdp9Sw3ZwfXFl4EuipKP1Ahn0="

def now():
    return int(time.time())

def maskOne(i):
    if i==0:
        return format(random.randint(0,15),'x').upper()
    elif i==1:
        return format(random.randint(0,15),'x')
    elif i==2:
        return str(random.randint(0,9))
    elif i==3:
        return random.choice(nlookDigit)
    elif i==4:
        return random.choice(string.ascii_letters)
    elif i==5:
        return random.choice(nlookLetterU+nlookLetterL)
    elif i==6:
        return random.choice(string.ascii_uppercase)
    elif i==7:
        return random.choice(nlookLetterU)
    elif i==8:
        return random.choice(string.ascii_lowercase)
    elif i==9:
        return random.choice(nlookLetterL)
    elif i==10:
        return random.choice(string.ascii_lowercase+string.ascii_uppercase+numberStrings)
    elif i==11:
        return random.choice(nlookLetterU+nlookLetterL+nlookDigit)
    elif i==12:
        return random.choice(nlookLetterU+nlookLetterL+numberStrings)
    elif i==13:
        return random.choice(string.ascii_uppercase+numberStrings)
    elif i==14:
        return random.choice(nlookLetterU+nlookDigit)
    elif i==15:
        return random.choice(nlookLetterU+numberStrings)
    elif i==16:
        return random.choice(string.ascii_lowercase+numberStrings)
    elif i==17:
        return random.choice(nlookLetterL+nlookDigit)
    elif i==18:
        return random.choice(nlookLetterL+numberStrings)
    else:
        return ""

def maskAll(string):
    masked = list(string)

    for idx,val in enumerate(masked):
        for i,v in enumerate(masks):
            if masked[idx] == masks[i]:
                masked[idx]=maskOne(i)
                break
    masked = "".join(masked)
    
    return masked

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

    string = None
    try:
        with open(dbFile,'rb') as file:
            data = file.read()
            if data:
                string = ''
                chunks = data.split(b'\x00')
                for i in chunks:
                    dec = f.decrypt(i).decode()
                    string += dec
                file.close()
    except FileNotFoundError:
        os.makedirs(os.path.dirname(dbFile), exist_ok=True)
        with open(dbFile,'w') as file:
            file.close()
        with open(dbFile,'rb') as file:
            string = file.read()

    if string:
        keyInfo = string.split(new)
        for val in keyInfo:
            i=val.split(sep)
            table[i[0]] = {'t':i[1],'v':i[2],'ct':i[3],'at':i[4]}
    

def setKey(k,t=default,v=None,ct=now(),at=None):
    global table
    d = {'t':str(t) or default,'ct':str(ct or now())}
    if v:
        d |= {'v':str(v)}
    table[k] = d
    table = dict(sorted(table.items()))
    return

def get(k):
    return table.get(k)

def gen():
    key = conf.get("format")

    parts = key.split("$")
    for i,v in enumerate(parts):
        if i % 2 != 0:
            parts[i] = maskAll(v)

    key = "".join(parts)

    setKey(key,default,None,now())
    
    return key

read()
