from functions import *

def runBlock(block, trials):

    showCue(block)

    for _ in range(trials):

        tori = showStim()
        if block == 'Second': tori.reverse()

        perf = 0

        for i, targori in enumerate(tori):

            key, turns = showDial(); 
            if i == 0: showFix(timing['del3'])

            repori = getReportori(key, turns)
            perf += getPerformance(repori, targori)

        showFeedback(str(round(perf/2)))
        
runBlock(block = 'First', trials = 5)
runBlock(block = 'Second', trials = 5)