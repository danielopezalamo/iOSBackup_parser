DB_FILES = ['Library/Keyboard/langlikelihood.dat', 'Library/Keyboard/user_model_database.sqlite']

import files_parser as fp
from iOSbackup import iOSbackup

def getKeyboardInfo(b: iOSbackup):
    fp.getDbFiles(b, DB_FILES, "Keyboard")