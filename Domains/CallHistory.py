DB_FILES = ['Library/CallHistoryDB/CallHistoryTemp.storedata']

import files_parser as fp
from iOSbackup import iOSbackup

def getCallHistoryInfo(b: iOSbackup):
    fp.getDbFiles(b, DB_FILES, "CallHistory")