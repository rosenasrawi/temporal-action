from logdata import *
filename, sub, ses = newLogfile()

from functions import *
from triggers import *

send = True
portEEG = connectEEG()
tracker = connectTracker(sub, ses)

startTracker(tracker)
showStart()
blockcols = balanceCols()

for blocknum in range(runs['stotal']):
    
    if blocknum in [0,2,4,6]: 
        cols = blockcols.pop(0)
        setCue(cols)
        showCue(True)
        runPractice(cols)

    trialtypes = runs['sblock'].copy()
    random.shuffle(trialtypes)
    runBlock(blocknum, filename, trialtypes, cols, send, portEEG, tracker)
    
    if blocknum != runs['stotal']: 
        showBreak(blocknum+1, runs['stotal'])

showSaving()
stopTracker(tracker)
showEnd()