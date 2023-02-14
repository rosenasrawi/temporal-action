from logdata import *
filename, sub, ses = newLogfile()

from functions import *
from triggers import *

send = True
portEEG = connectEEG()
tracker = connectTracker(sub, ses)

startTracker(tracker)

for blocknum in range(runs['stotal']):
    if blocknum != 0: showBreak(block+1, runs['stotal'])
    runBlock(blocknum, filename, send, portEEG, tracker)

showSaving()
stopTracker(tracker)
showEnd()