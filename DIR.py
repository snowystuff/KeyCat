from platformdirs import *
import os

appDir = user_config_dir("KeyCat")

confName = "config.json"
dbName = "database"
keyName = "key"

configFile = os.path.join(appDir, confName)
dbFile = os.path.join(appDir, dbName)

default = "default"

typeFlag = "-t"
countFlag = "-c"
