from logdata import *
filename, sub, ses = newLogfile()

from functions import *

for block in range(runs['stotal']):
    runBlock(filename)
    showBreak(block+1, runs['stotal'])

showEnd()