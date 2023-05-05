DB_FILES = ['Library/Keyboard/langlikelihood.dat', 'Library/Keyboard/user_model_database.sqlite']

import fileParser as fp
from iOSbackup import iOSbackup

def getKeyboardInfo(b: iOSbackup):
    print("------- KEYBOARD -------")
    fp.getDbFiles(b, DB_FILES, "Keyboard")