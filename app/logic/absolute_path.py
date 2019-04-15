import os
import sys

def getAbsolutePath(relativePath,filename=None,makeDirs=False):
    filepath = os.path.join(sys.path[0],relativePath)
    if makeDirs == True:
        try:
            os.makedirs(filepath)
        except:
            pass
    if filename != None:
        filepath = os.path.join(filepath,filename)
    return filepath