PLIST_FILES = [
    'Library/Preferences/com.apple.assistant'
]

import files_parser as fp
from iOSbackup import iOSbackup

def getSiriInfo(b: iOSbackup):
    plist_files = fp.find_files(b, PLIST_FILES)
    fp.getPlistFiles(b, plist_files, "Siri")