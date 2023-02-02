from functions import *
from statistics import mean

from logdata import *

def runBlock(trialtypes):

    showCalib()
    
    cols = showCue()

    blockperf = 0

    for _, trial in enumerate(trialtypes):

        tori, logdata = showStim(trial, cols)
        perfs = []; repdata = []
        triggers = [getTrigger(trial, 'enc1'), getTrigger(trial, 'enc2'),
                    getTrigger(trial, 'enc2'), getTrigger(trial, 'probe2')]

        for i, targori in enumerate(tori):

            key, turns, keyevent = showDial(trial, str(i+1)); 

            triggers.append(getTrigger(trial, keyevent))

            if i == 0: showFix(timing['del3'])

            repori = getReportori(key, turns)
            perf, diff = getPerformance(repori, targori)
            repdata += [round(repori), turns, key, perf, diff]

            perfs.append(perf)

        logdata = addSpec(logdata, repdata + triggers, ki = 18)

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


