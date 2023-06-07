PLIST_FILES = [
    'Library/Preferences/com.apple.assistant.backedup.plist',
    'Library/Preferences/com.apple.assistant.support.plist',
    'Library/Preferences/com.apple.AssistantServices.plist',
]

import fileParser as fp
from iOSbackup import iOSbackup

def getSiriInfo(b: iOSbackup):
    print("------- SIRI -------")
    fp.getPlistFiles(b, PLIST_FILES, "Siri")