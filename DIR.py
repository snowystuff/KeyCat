from platformdirs import *
import os

appDir = user_config_dir("KeyCat")
configFile = full_file_path = os.path.join(appDir, "config.json")
