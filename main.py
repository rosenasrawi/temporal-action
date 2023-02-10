from logdata import *
filename, sub, ses = newLogfile()

from functions import *
from triggers import *

send = True
portEEG = connectEEG()
tracker = connectTracker(sub, ses)

startTracker(tracker)

for block in range(runs['stotal']):
    runBlock(filename, send, portEEG, tracker)
    showBreak(block+1, runs['stotal'])

showSaving()
stopTracker(tracker)
showEnd()