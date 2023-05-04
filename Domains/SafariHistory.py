DB_FILES = [
    'Library/Safari/History.db'
]

import files_parser as fp
from iOSbackup import iOSbackup

def getSafariHistoryInfo(b: iOSbackup):
    fp.getDbFiles(b, DB_FILES, "SafariHistory")