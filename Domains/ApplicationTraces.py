DB_FILES = [
    'Library/com.apple.itunesstored/itunesstored2.sqlitedb', 'Library/CoreDuet/People/interactionC.db',
    'Library/FrontBoard/applicationState.db', 'Library/Databases/DataUsage.sqlite', 'Library/Keyboard/langlikelihood.dat'
]
PLIST_FILES = [
    'Library/Caches/locationd/clients.plist', 'Library/Preferences/com.apple.corespotlightui.plist'
]
LOG_FILES = ['Library/Logs/mobile_installation_helper.log']

import fileParser as fp
from iOSbackup import iOSbackup

def getApplicationTracesInfo(b: iOSbackup):
    print("------- APPLICATION TRACES -------")
    fp.getDbFiles(b, DB_FILES, "ApplicationTraces")
    fp.getLogFiles(b, LOG_FILES, "ApplicationTraces")
    fp.getPlistFiles(b, PLIST_FILES, "ApplicationTraces")