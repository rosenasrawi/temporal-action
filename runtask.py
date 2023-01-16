from psychopy import core, event

import random
from math import cos, sin

from stimuli import *
from settings import *

def turnHandle(pos, rad):
    
    x, y = pos
    pos = (x * cos(rad) + y * sin(rad), -x * sin(rad) + y * cos(rad))

    return pos

def getReportori(key, turns):
    
    repori = degrees(turns * dial['step'])

    if key == 'z':
        repori *= -1
    
    return repori
 
def getPerformance(repori, targori):

    diff = abs(targori - round(repori))

    if diff > 90:
        diff -= 180
        diff *= -1

    perf = round(100 - diff/90 * 100)

    return str(perf)

def trialSettings():
    
    cols = bar['cols'].copy()

    tcol = cols[:2]; ncol = cols[2:]
    random.shuffle(tcol); random.shuffle(ncol)

    tori = [random.randint(bar['L'][0], bar['L'][1]),
            random.randint(bar['R'][0], bar['R'][1])]

    nori = [random.randint(bar['L'][0], bar['L'][1]),
            random.randint(bar['R'][0], bar['R'][1])]
    
    random.shuffle(tori)
    if tori[0] < 0: nori.reverse()

    t1 = random.choice(['L','R'])

    if t1 == 'L': 
        cols = [tcol[0], ncol[0], ncol[1], tcol[1]]
        tilts = [tori[0], nori[0], nori[1], tori[1]]
    else: 
        cols = [ncol[0], tcol[0], tcol[1], ncol[1]]
        tilts = [nori[0], tori[0], tori[1], nori[1]]

    return cols, tilts, tori

def showCue(block):

    fixcross.setAutoDraw(False)
    col1.draw(); col2.draw()
    
    if block == 'First':
        first.draw()
    elif block == 'Second':
        second.draw()   

    space2start.draw()
    window.flip()

    event.waitKeys(keyList = 'space')

def showStim():

    cols, tilts, tori = trialSettings()

    fixcross.lineColor = fix['basecol']
    fixcross.setAutoDraw(True)

    fixtime = random.randint(timing['fix'][0], timing['fix'][1])

    for _ in range(fixtime):
        window.flip()

    leftbar.fillColor = cols.pop(0)
    rightbar.fillColor = cols.pop(0)
    leftbar.ori = tilts.pop(0)
    rightbar.ori = tilts.pop(0)

    for _ in range(timing['enc']):
        leftbar.draw(); rightbar.draw()
        window.flip()

    for _ in range(timing['del1']):
        window.flip()

    leftbar.fillColor = cols.pop(0)
    rightbar.fillColor = cols.pop(0)
    leftbar.ori = tilts.pop(0)
    rightbar.ori = tilts.pop(0)

    for _ in range(timing['enc']):
        leftbar.draw(); rightbar.draw()
        window.flip()

    for _ in range(timing['del2']):
        window.flip()

    fixcross.setAutoDraw(False)

    return tori

def showDial():
    
    turntop.pos = (0, dial['hpos'])
    turnbot.pos = (0, -dial['hpos'])

    released = []; pressed = []; turns = 0

    fixcross.lineColor = fix['probecol']
    fixcross.setAutoDraw(True)
    window.flip()

    pressed = event.waitKeys(keyList = ['z', 'm', 'q'])

    if 'm' in pressed: 
        key = 'm'; rad = dial['step']
    elif 'z' in pressed: 
        key = 'z'; rad = -dial['step']
    if 'q' in pressed:
        core.quit()
    
    while released == [] and turns <= dial['max']:

        released = kb.getKeys(keyList = [key], waitRelease = True, clear = True)

        turntop.pos = turnHandle(turntop.pos, rad)
        turnbot.pos = turnHandle(turnbot.pos, rad)

        turns += 1
        dialcircle.draw(); turntop.draw(); turnbot.draw()
        window.flip()

    return key, turns

def showFeedback(perf):

    fixcross.lineColor = fix['basecol']
    feedback.text = perf
    
    for _ in range(timing['fb']):
        feedback.draw()
        window.flip()

    for _ in range(timing['del3']):
        window.flip()

def runBlock(block):

    showCue(block)

    for _ in range(5):
        tori = showStim()
        if block == 'Second': tori.reverse()

        for _, targori in enumerate(tori):

            key, turns = showDial()
            repori = getReportori(key, turns)
            perf = getPerformance(repori, targori)

            showFeedback(perf)
        
runBlock(block = 'First')
runBlock(block = 'Second')
