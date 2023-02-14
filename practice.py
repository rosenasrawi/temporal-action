from logdata import *
filename, sub, ses = newLogfile()

from functions import *

for blocknum in range(runs['stotal']):
    if blocknum != 0: showBreak(blocknum+1, runs['stotal'])
    runBlock(blocknum, filename)

showEnd()