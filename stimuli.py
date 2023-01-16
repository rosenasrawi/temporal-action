from psychopy import visual
from psychopy.hardware import keyboard

from settings import *

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

fixcross = visual.ShapeStim(
    win = window, 
    vertices = ((0,-fix['size']), (0,fix['size']), (0,0), (-fix['size'],0), (fix['size'],0)),
    lineWidth = fix['line'],
    closeShape = False,
    units = 'pix')

def makeBar(pos):

    barstim = visual.Rect(
        win = window,
        units = "pix",
        width = bar['size'][0],
        height = bar['size'][1],
        pos = pos)

    return barstim

leftbar = makeBar(pos = (-bar['shift'], 0))
rightbar = makeBar(pos = (bar['shift'], 0))

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

def makeText(input, pos = (0,0), col = text['col']):

    textstim = visual.TextStim(
        win = window, 
        font = text['font'],
        text = input,
        color = col,
        pos = pos,
        height = text['size'])

    return textstim

feedback = makeText('', text['fbpos'])

col1 = makeText(bar['colnames'][0], text['ltpos'], col = bar['cols'][0])
col2 = makeText(bar['colnames'][1], text['rtpos'], col = bar['cols'][1])

first = makeText('Report FIRST target FIRST')
second = makeText('Report SECOND target FIRST')

space2start = makeText('Press SPACE to continue',  text['bpos'])
