from logdata import *
filename, sub, ses = newLogfile()

from functions import *

for _ in range(8):
    showPracticeDial()

for blocknum in range(runs['stotal']):
    if blocknum != 0: showBreak(blocknum+1, runs['stotal'])
    runBlock(blocknum, filename)

showEnd()