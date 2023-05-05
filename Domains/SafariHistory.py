DB_FILES = [
    'Library/Safari/History.db'
]

import fileParser as fp
from iOSbackup import iOSbackup

def getSafariHistoryInfo(b: iOSbackup):
    print("------- SAFARI HISTORY -------")
    fp.getDbFiles(b, DB_FILES, "SafariHistory")