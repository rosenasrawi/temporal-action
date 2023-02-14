from psychopy import core, event

import random, time
from math import cos, sin
from statistics import mean

from stimuli import *
from settings import *

from logdata import *

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

    return perf, diff

def getOri(tilt):

    ori = [random.randint(bar[tilt[0]][0], bar[tilt[0]][1]),
           random.randint(bar[tilt[1]][0], bar[tilt[1]][1])]

    return ori

def setBlock():

    cols = bar['cols'].copy()
    names = bar['colnames']
    random.shuffle(cols)

    col1.color = cols[0]; col1.text = names[bar['cols'].index(cols[0])]
    col2.color = cols[1]; col2.text = names[bar['cols'].index(cols[1])]
    
    return cols

def setTrial(trial, cols, logdata):
    
    tcol = cols[:2]; ncol = cols[2:]
    random.shuffle(ncol) 
    
    order, loc, tilt = trials[trial]

    if order == 'second':
        tcol.reverse()

    tori = getOri(tilt); nori = getOri(tilt)
    nori.reverse()
    
    if loc == 'LR':
        enc1 = [tcol[0], ncol[0], tori[0], nori[0]]
        enc2 = [ncol[1], tcol[1], nori[1], tori[1]]
    elif loc == 'RL':
        enc1 = [ncol[0], tcol[0], nori[0], tori[0]]
        enc2 = [tcol[1], ncol[1], tori[1], nori[1]]

    logdata = addSpec(logdata,
                      data = (trial, order, loc, tilt, 
                              enc1[2], enc1[3], enc2[2], enc2[3],
                              enc1[0], enc1[1], enc2[0], enc2[1],
                              tori[0], tcol[0], loc[0],
                              tori[1], tcol[1], loc[1]),
                      ki = 0)

    if order == 'second':
        tori.reverse()

    return enc1, enc2, tori, logdata

def getTrigger(trial, event):

    trigger = trial + events[event]

    return trigger

def showCue(practice = False):

    fixcross.setAutoDraw(False)
    if practice: time2practice.draw()
    else: time2block.draw()
    col1.draw(); then.draw(); col2.draw()

    space2start.draw()
    window.flip()

    event.waitKeys(keyList = 'space')

def showFix(tfix):

    fixcross.lineColor = fix['basecol']
    
    for _ in range(tfix):
        fixcross.draw()
        window.flip()

def showBars(settings, trial, time, send = False, portEEG = None, tracker = None):

    leftbar.fillColor, rightbar.fillColor, leftbar.ori, rightbar.ori = settings

    if send: 
        window.callOnFlip(tracker.send_message, 'trig' + str(getTrigger(trial, 'enc'+time)))
        window.callOnFlip(portEEG.setData, getTrigger(trial, 'enc'+time))
    else:
        window.callOnFlip(print, getTrigger(trial, 'enc'+time))

    for f in range(timing['enc']):
        fixcross.draw(); leftbar.draw(); rightbar.draw()
        window.flip()
        if send and f == 2: portEEG.setData(0)

def showStim(trial, cols, send = False, portEEG = None, tracker = None):

    logdata = log.copy()

    tfix = random.randint(timing['fix'][0], timing['fix'][1])
    enc1, enc2, tori, logdata = setTrial(trial, cols, logdata)
    
    showFix(tfix)

    showBars(enc1, trial, '1', send, portEEG, tracker)
    showFix(timing['del1'])

    showBars(enc2, trial, '2', send, portEEG, tracker)
    showFix(timing['del2'])

    return tori, logdata

def showPracticeDial():

    ori = getOri('LR')
    centerbar.ori = random.choice(ori)
    
    kb.clearEvents()
    released = []; pressed = []; turns = 0
    
    turntop.pos = (0, dial['hpos'])
    turnbot.pos = (0, -dial['hpos'])

    dialcirc.draw(); centerbar.draw()
    turntop.draw(); turnbot.draw()
    practicedial.draw()

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
        dialcirc.draw(); centerbar.draw()
        turntop.draw(); turnbot.draw()
        practicedial.draw()
        
        window.flip()

def showDial(trial, moment, send = False, portEEG = None, tracker = None):

    kb.clearEvents()
    turntop.pos = (0, dial['hpos'])
    turnbot.pos = (0, -dial['hpos'])

    released = []; pressed = []; turns = 0

    if send: 
        window.callOnFlip(tracker.send_message, 'trig' + str(getTrigger(trial, 'probe' + moment)))
        window.callOnFlip(portEEG.setData, getTrigger(trial, 'probe' + moment))
    else:
        window.callOnFlip(print, getTrigger(trial, 'probe' + moment))

    fixcross.lineColor = fix['probecol']
    fixcross.draw()
    window.flip()

    ptime = time.time()

    if send: core.wait(2/monitor['Hz']); portEEG.setData(0)

    pressed = event.waitKeys(keyList = ['z', 'm', 'q'])

    ktime = time.time()

    if 'm' in pressed: 
        key = 'm'; rad = dial['step']; keyevent = 'respR'
    elif 'z' in pressed: 
        key = 'z'; rad = -dial['step']; keyevent = 'respL'
    if 'q' in pressed:
        core.quit()
    
    if send:
        window.callOnFlip(tracker.send_message, 'trig' + str(getTrigger(trial, keyevent + moment)))
        portEEG.setData(getTrigger(trial, keyevent + moment))
        core.wait(2/monitor['Hz']); portEEG.setData(0)
    else:
        window.callOnFlip(print, getTrigger(trial, keyevent + moment))

    while released == [] and turns <= dial['max']:

        released = kb.getKeys(keyList = [key], waitRelease = True, clear = True)

        turntop.pos = turnHandle(turntop.pos, rad)
        turnbot.pos = turnHandle(turnbot.pos, rad)

        turns += 1
        dialcirc.draw(); fixcross.draw()
        turntop.draw(); turnbot.draw()
        window.flip()

    rtime = time.time()

    DT = ktime - ptime
    RT = rtime - ktime

    fixcross.lineColor = fix['basecol']

    return key, turns, keyevent + moment, DT, RT

def showFeedback(perf, cols):
    
    for i in range(len(perf)):

        feedback.text = perf[i]
        feedback.color = cols[i]

        for _ in range(timing['fb']):
            feedback.draw()
            window.flip()

        for _ in range(timing['del4']):
            window.flip()

def showBlockfb(blockperf):

    showFix(timing['enc'])

    blockfb.text = 'Average score this block: ' + blockperf + '/100'

    blockfb.draw(); space2start.draw()
    window.flip()

    event.waitKeys(keyList = 'space')

def showBreak(block, total):

    blockcount.text = 'You have completed ' + str(block) + '/' + str(total) + ' blocks'

    blockcount.draw(); takebreak.draw(); space2start.draw()
    window.flip()

    event.waitKeys(keyList = 'space')

def showEnd():

    taskend.draw(); space2close.draw()
    window.flip()
    
    event.waitKeys(keyList = 'space')

def showSaving():

    savingdata.draw()
    window.flip()

def runBlock(blocknum, filename, send = False, portEEG = None, tracker = None):

    trialtypes = runs['block'].copy()
    random.shuffle(trialtypes)
    
    cols = setBlock()
    showCue(True)
    # runPractice(cols)
    
    blockperf = 0
    showCue()

    for trialnum, trial in enumerate(trialtypes):

        tori, logdata = showStim(trial, cols, send, portEEG, tracker)
        perfs = []; repdata = []
        
        triggers = [getTrigger(trial, 'enc1'), getTrigger(trial, 'enc2'),
                    getTrigger(trial, 'enc2'), getTrigger(trial, 'probe2')]

        for i, targori in enumerate(tori):

            key, turns, keyevent, DT, RT = showDial(trial, str(i+1), send, portEEG, tracker); 

            triggers.append(getTrigger(trial, keyevent))

            if i == 0: showFix(timing['del3'])

            repori = getReportori(key, turns)
            perf, diff = getPerformance(repori, targori)
            repdata += [round(repori), turns, key, perf, diff, DT, RT]

            perfs.append(perf)

        logdata = addSpec(logdata, repdata + triggers, ki = 18)
        logdata['trialnum'] = trialnum
        logdata['blocknum'] = blocknum

        blockperf += round(mean(perfs))
        showFeedback(list(map(str,perfs)), cols[:2])
        addTrial(logdata, filename)
    
    blockperf = str(round((blockperf / len(trialtypes))))
    showBlockfb(blockperf)

    return logdata

def runPractice(cols):
    
    trialtypes = runs['practice'].copy()
    random.shuffle(trialtypes)

    blockperf = 0

    for _, trial in enumerate(trialtypes):

        tori, _ = showStim(trial, cols)
        perfs = []

        for i, targori in enumerate(tori):

            key, turns, _, _, _ = showDial(trial, str(i+1)); 

            if i == 0: showFix(timing['del3'])

            repori = getReportori(key, turns)
            perf, _ = getPerformance(repori, targori)

            perfs.append(perf)

        blockperf += round(mean(perfs))
        showFeedback(list(map(str,perfs)), cols[:2])
    
    blockperf = str(round((blockperf / len(trialtypes))))
    showBlockfb(blockperf)
