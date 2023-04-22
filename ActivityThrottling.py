from iOSbackup import iOSbackup
import plistlib, json

PLIST_FILES = ['Library/Preferences/com.apple.coreduetd.plist', 'Library/Preferences/com.apple.contextstored.plist']

import files_parser as fp
from iOSbackup import iOSbackup

def getActivityThrottlingInfo(b: iOSbackup):
    fp.getPlistFiles(b, PLIST_FILES, "ActivityThrottling")