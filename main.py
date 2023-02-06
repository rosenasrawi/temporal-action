from logdata import *
filename, sub, ses = newLogfile()

from functions import *
from statistics import mean

from triggers import *

portEEG = connectEEG()
tracker = connectTracker(sub, ses)
startTracker(tracker)

for i in range(8):    
    
    if i != 0: calibrateTracker()

    runBlock(filename, portEEG, tracker)

stopTracker()