from ctypes import windll
windll.LoadLibrary("C:\\PROGS\\inpoutx64.dll")

from psychopy import parallel, event
from eyelinkPackages import eyelinker

import os

from stimuli import window, calibwait
from settings import eyedir

def connectEEG():
    
    portEEG = parallel.ParallelPort(address = 0x3050)
    portEEG.setData(255); portEEG.setData(0)
    
    return portEEG

def connectTracker(subject, session):

    tracker = eyelinker.EyeLinker(window = window, eye = 'BOTH',
                                  filename = 'rn6_' + subject + session + '.edf')

    return tracker

def startTracker(tracker):
    os.chdir(eyedir)

    tracker.open_edf()
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
