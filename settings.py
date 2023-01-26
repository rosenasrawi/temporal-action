from math import pi, atan2, degrees

def deg2pix(deg):
    dpix = degrees(atan2(.5 * monitor['h'], monitor['d'])) / (.5 * monitor['res'][0])
    return int(deg/dpix)

def sec2frm(sec):
    return int(monitor['Hz'] * sec)

screen = 'mac' # 'mac'

datadir = '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action/Data/Logfiles'

if screen == 'LG':
    res = (2560,1440); Hz = 120
    h = 30; d = 50
elif screen == 'mac':
    res = (1536,960); Hz = 120
    h = 22; d = 50

monitor = {
    'res': res, 
    'Hz': Hz,
    'h': h,
    'd': d,
    'col': (-0.3, -0.3, -0.3)
}

fix = {
    'size': deg2pix(0.2),
    'line': deg2pix(0.05),
    'basecol': (0.3, 0.3, 0.3),
    'probecol': (0.8, 0.8, 0.8)
}

bar = {
    'size': (deg2pix(0.4), deg2pix(3)),
    'shift': deg2pix(4),
    'cols': ["#ff8a65","#64b5f6","#81c784","#ce93d8"],
    'colnames': ['ORANGE', 'BLUE', 'GREEN', 'PURPLE'],
    'L': (-80,-10),
    'R': (10, 80)
}

dial = {
    'rad': deg2pix(1.5),
    'edge': deg2pix(1),
    'line': deg2pix(0.05),
    'col': (0.5, 0.5, 0.5),
    'hrad': deg2pix(0.15),
    'hpos': deg2pix(1.5),
    'max': monitor['Hz'],
    'step': (0.5*pi) / monitor['Hz']
}

timing = {
    'fix': (sec2frm(.5), sec2frm(.8)),
    'enc': sec2frm(.25),
    'del1': sec2frm(1.25),
    'del2': sec2frm(1.75),
    'del3': sec2frm(1),
    'del4': sec2frm(.5),
    'fb': sec2frm(.25)
}

text = {
    'font': 'Courier New',
    'col': (0.5, 0.5, 0.5),
    'size': deg2pix(0.4),
    'fbpos': (0, 0),
    'lpos': (-deg2pix(3), 0),
    'rpos': (deg2pix(3), 0),
    'bpos': (0, -deg2pix(2))
}

trials = {
    1: ('first', 'LR', 'LR'), # order, loc, tilt
    2: ('first', 'LR', 'RL'),
    3: ('first', 'RL', 'LR'),
    4: ('first', 'RL', 'RL'),
    5: ('second', 'LR', 'LR'),
    6: ('second', 'LR', 'RL'),
    7: ('second', 'RL', 'LR'),
    8: ('second', 'RL', 'RL')
}

events = {
    'enc1': 0,
    'enc2': 10,
    'probe1': 20,
    'respL1': 30,
    'respR1': 40,
    'probe2': 50,
    'respL2': 60,
    'respR2': 70
}

log = {
    'trial': None, 'order': None, 'loc': None, 'tilt': None,

    'ori1': None, 'ori2': None, 'ori3': None, 'ori4': None,
    'col1': None, 'col2': None, 'col3': None, 'col4': None,
    
    'tori1': None, 'tcol1': None, 'tloc1': None,
    'tori2': None, 'tcol2': None, 'tloc2': None,

    'rori1': None, 'turns1': None, 'key1': None, 'perf1': None, 'diff1': None,
    'rori2': None, 'turns2': None, 'key2': None, 'perf2': None, 'diff2': None
}
