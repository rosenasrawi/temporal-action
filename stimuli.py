from psychopy import visual
from psychopy.hardware import keyboard

from settings import *

# Window

window = visual.Window(
    color = monitor['col'],
    monitor = "testMonitor", 
    size = monitor['res'],
    units = "pix",
    fullscr = False)

kb = keyboard.Keyboard()

mouse = visual.CustomMouse(
    win = window,
    visible = False)

# Stimuli

fixcross = visual.ShapeStim(
    win = window, 
    vertices = ((0,-fix['size']), (0,fix['size']), (0,0), (-fix['size'],0), (fix['size'],0)),
    lineWidth = fix['line'],
    closeShape = False,
    units = 'pix')

# Bars

def makeBar(bar, left = False):

    if left: pos = -bar['shift']
    else: pos = bar['shift']

    barstim = visual.Rect(
        win = window,
        units = "pix",
        width = bar['size'][0],
        height = bar['size'][1],
        pos = (pos,0))

    return barstim

leftbar = makeBar(bar, left = True)
rightbar = makeBar(bar)

# Response dial

def makeCircle(rad, pos = (0,0), handle = False):

    circle = visual.Circle(
        win = window,
        radius = rad,
        edges = dial['edge'],
        lineWidth = dial['line'],
        lineColor = dial['col'],
        pos = pos)

    if handle:
        circle.fillColor = monitor['col']
    return circle

dialcircle = makeCircle(dial['rad'])
turntop = makeCircle(dial['hrad'], pos = (0, dial['hpos']), handle = True)
turnbot = makeCircle(dial['hrad'], pos = (0, -dial['hpos']), handle = True)