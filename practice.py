from logdata import *
filename, sub, ses = newLogfile()

from functions import *

for _ in range(4):
    practiceDial()

for blocknum in range(runs['ptotal']):

    trialtypes = runs['pblock'].copy()
    random.shuffle(trialtypes)
    cols = randomCols()
    setCue(cols)

    showCue(True)
    runPractice(cols)
    runBlock(blocknum, filename, trialtypes, cols)

showEnd()