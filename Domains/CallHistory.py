DB_FILES = ['Library/CallHistoryDB/CallHistoryTemp.storedata']

import fileParser as fp
from iOSbackup import iOSbackup

def getCallHistoryInfo(b: iOSbackup):
    print("------- CALL HISTORY -------")
    fp.getDbFiles(b, DB_FILES, "CallHistory")