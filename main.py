from functions import *
from statistics import mean

from logdata import *
from triggers import *

filename = newLogfile()

portEEG = connectEEG()
tracker = connectTracker()

for _ in range(8):    
    
    runPractice()
    runBlock(filename, portEEG, tracker)
