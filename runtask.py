from psychopy import core, event
import random, time

from stimuli import *
from settings import *

def trialSettings(): # Random now
    
    cols = bar['cols']
    random.shuffle(cols)

    tdist = ('LRLR','RLRL')
    tdist = random.choice(tdist)

    tilts = []

    for _, t in enumerate(tdist):
        tilt = random.randint(trange[t][0], trange[t][1])
        tilts.append(tilt)

    return cols, tilts

def singleTrial():

    cols, tilts = trialSettings()

    fixcross.lineColor = fix['basecol']
    fixcross.setAutoDraw(True)
    fixtime = random.randint(timing['fix'][0], timing['fix'][1])

    for _ in range(fixtime):
        window.flip()

    leftbar.fillColor = cols.pop()
    rightbar.fillColor = cols.pop()

    leftbar.ori = tilts.pop()
    rightbar.ori = tilts.pop()

    for _ in range(timing['enc']):
        leftbar.draw(); rightbar.draw()
        window.flip()

    for _ in range(timing['del1']):
        window.flip()

    leftbar.fillColor = cols.pop()
    rightbar.fillColor = cols.pop()

    leftbar.ori = tilts.pop()
    rightbar.ori = tilts.pop()

    for _ in range(timing['enc']):
        leftbar.draw(); rightbar.draw()
        window.flip()

    for _ in range(timing['del2']):
        window.flip()

    
singleTrial()