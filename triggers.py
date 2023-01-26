from psychopy import parallel, event

from ctypes import windll
windll.LoadLibrary("C:\\PROGS\\inpoutx64.dll")
from eyelinkPackages import eyelinker

import os

from stimuli import window, calibwait
from settings import eyedir

def connectEEG():
    
    portEEG = parallel.ParallelPort(address = 0x3050)
    portEEG.setData(255); portEEG.setData(0)
    
    return portEEG

def connectTracker(sub, ses):
    tracker = eyelinker.EyeLinker(window = window, eye = 'BOTH',
                                  filename = 'rn4_' + sub + ses + '.edf')

    return tracker

def startTracker(tracker):
    os.chdir(eyedir)

    tracker.open_edf() # open a data file
    tracker.init_tracker()
    tracker.start_recording()

def calibrateTracker(tracker):
    tracker.stop_recording()

    calibwait.draw()
    window.flip()
    event.waitKeys(keyList = 'r')
    
    tracker.start_recording()

def stopTracker(tracker):
    os.chdir(eyedir)

    tracker.stop_recording()
    tracker.transfer_edf()
    tracker.close_edf()

def sendTrigger(portEEG, tracker, trig):

    window.callOnFlip(portEEG.setData, trig)
    window.callOnFlip(tracker.send_message, 'trig' + str(trig))
