from functions import *
from statistics import mean

from logdata import *

def runBlock(trialtypes):

    cols = showCue()

    blockperf = 0

    for _, trial in enumerate(trialtypes):

        tori, logdata = showStim(trial, cols)
        perfs = []; repdata = []

        for i, targori in enumerate(tori):

            key, turns = showDial(); 
            if i == 0: showFix(timing['del3'])

            repori = getReportori(key, turns)
            perf, diff = getPerformance(repori, targori)
            repdata += [round(repori), turns, key, perf, diff]

            perfs.append(perf)

        logdata = addSpec(logdata, repdata, ki = 18)

        blockperf += round(mean(perfs))
        showFeedback(list(map(str,perfs)), cols[:2])
        addTrial(logdata, filename)
    
    blockperf = str(round((blockperf / len(trialtypes))))
    showBlockfb(blockperf)

    return logdata

filename = newLogfile()

for _ in range(2):    
    trialtypes = [1,2,3,4,5,6,7,8]
    random.shuffle(trialtypes)
    runBlock(trialtypes)


