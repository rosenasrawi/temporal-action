from psychopy import core, event

import random
from math import cos, sin
from statistics import mean

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

    return perf

def getOri():

    ori = [random.randint(bar['L'][0], bar['L'][1]),
           random.randint(bar['R'][0], bar['R'][1])]

    return ori

def trialSettings():
    
    cols = bar['cols'].copy()

    tcol = cols[:2]; ncol = cols[2:]
    random.shuffle(tcol); random.shuffle(ncol)

    tori = getOri(); nori = getOri()
    random.shuffle(tori)

    if tori[0] < 0: nori.reverse()

    t1 = random.choice(['L','R'])

    if t1 == 'L':
        enc1 = [tcol[0], ncol[0], tori[0], nori[0]]
        enc2 = [ncol[1], tcol[1], nori[1], tori[1]]
    else:
        enc1 = [ncol[0], tcol[0], nori[0], tori[0]]
        enc2 = [tcol[1], ncol[1], tori[1], nori[1]]

    return enc1, enc2, tori

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

def showFix(tfix):
    fixcross.lineColor = fix['basecol']
    
    for _ in range(tfix):
        fixcross.draw()
        window.flip()

def showBars(settings):

    lcol, rcol, lori, rori = settings

    leftbar.fillColor = lcol; leftbar.ori = lori
    rightbar.fillColor = rcol; rightbar.ori = rori 

    for _ in range(timing['enc']):
        fixcross.draw(); leftbar.draw(); rightbar.draw()
        window.flip()

def showStim():

    tfix = random.randint(timing['fix'][0], timing['fix'][1])
    enc1, enc2, tori = trialSettings()
    
    showFix(tfix)

    showBars(enc1)
    showFix(timing['del1'])

    showBars(enc2)
    showFix(timing['del2'])

    return tori

def showDial():
    
    kb.clearEvents()
    turntop.pos = (0, dial['hpos'])
    turnbot.pos = (0, -dial['hpos'])

    released = []; pressed = []; turns = 0

    fixcross.lineColor = fix['probecol']
    fixcross.draw()
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
        dialcircle.draw(); fixcross.draw()
        turntop.draw(); turnbot.draw()
        window.flip()

    fixcross.lineColor = fix['basecol']

    return key, turns

def showFeedback(perf):

    fixcross.lineColor = fix['basecol']
    feedback.text = perf
    
    for _ in range(timing['fb']):
        fixcross.draw(); feedback.draw()
        window.flip()

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