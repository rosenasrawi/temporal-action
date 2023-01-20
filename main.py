from functions import *

def runBlock(trialtypes):

    cols = showCue()

    blockperf = 0

    for _, trial in enumerate(trialtypes):

        tori = showStim(trial, cols)
        perf = 0

        for i, targori in enumerate(tori):

            key, turns = showDial(); 
            if i == 0: showFix(timing['del3'])

            repori = getReportori(key, turns)
            perf += getPerformance(repori, targori)

        blockperf += round(perf/2)
        showFeedback(str(round(perf/2)))
    
    blockperf = str(round((blockperf / len(trialtypes))))
    showBlockfb(blockperf)

for _ in range(2):    
    trialtypes = [1,2,3,4,5,6,7,8]
    random.shuffle(trialtypes)
    runBlock(trialtypes)