# KeyCat config module

import json
import os
from DIR import *

class Config:
    # Check for config.json
    
    def __init__(self):
        self.__data = self.default()
        try:
            with open(configFile,'r') as file:
                config = file.read()
                self.__data = self.__copy(self.default(),json.loads(config))
                file.close()
        except FileNotFoundError:
            self.__write()
            
    def __write(self):
        dump = json.dumps(self.__data)
        os.makedirs(os.path.dirname(configFile), exist_ok=True)
        with open(configFile,'w') as file:
            file.write(dump)
            file.close()

    def set(self,key,value):
        if self.__data[key]:
            self.__data[key] = value
        self.__write()
        return

    def get(self,key):
        if self.__data[key]:
            return self.__data[key]
        return

    def setAll(self,dictionary):
        self.__data = self.__copy(self.__data,dictionary)
        self.__write()
        return

    def getAll(self):
        return self.__data

    def default(self):
        return { # Default config
            "key": keyName,
            "keyFile": True,
            "format": "$NNNN$-$NNNN$-$NNNN$",
            "caseSensitive": False,
            "allowReusedValue": False,
            } 

    def __copy(self,dictionary,reference):
        for v in reference:
            if dictionary[v]:
                dictionary[v] = reference[v]
        return dictionary

    def reset(self):
        pass
