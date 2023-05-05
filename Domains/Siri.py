PLIST_FILES = [
    'Library/Preferences/com.apple.assistant'
]

import fileParser as fp
from iOSbackup import iOSbackup

def getSiriInfo(b: iOSbackup):
    print("------- SIRI -------")
    fp.getPlistFiles(b, PLIST_FILES, "Siri")