# Import libraries

from psychopy import core, event
import random, time
from math import degrees, cos, sin

# Import task scripts

from stimuli import *
from settings import *

def turnHandle(pos, rad):

    x, y = pos

    pos = (x * cos(rad) + y * sin(rad), -x * sin(rad) + y * cos(rad))

    return pos


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

def showStim():

    cols, tilts = trialSettings()

    fixcross.lineColor = fix['basecol']
    fixtime = random.randint(timing['fix'][0], timing['fix'][1])

    fixcross.setAutoDraw(True)

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

    fixcross.setAutoDraw(False)    

def showDial():
    
    released = []; pressed = []
    turns = 0

    fixcross.lineColor = fix['probecol']
    fixcross.setAutoDraw(True)
    window.flip()

    pressed = event.waitKeys(keyList = ['z', 'm', 'q', 'escape'])

    dialcircle.setAutoDraw(True)
    turntop.setAutoDraw(True)
    turnbot.setAutoDraw(True)

    if 'm' in pressed: 
        key = 'm'; rad = turn['rad']
    elif 'z' in pressed: 
        key = 'z'; rad = -turn['rad']

    if 'q' in pressed:
        core.quit()
    
    while released == [] and turns <= turn['max']:

        released = kb.getKeys(keyList = [key], waitRelease = True, clear = True)

        turntop.pos = turnHandle(turntop.pos, rad)
        turnbot.pos = turnHandle(turnbot.pos, rad)

        turns += 1

        window.flip()

    turntop.pos = (0, dial['hpos'])
    turnbot.pos = (0, -dial['hpos'])

for _ in range(5):    
    showStim()
    showDial()
