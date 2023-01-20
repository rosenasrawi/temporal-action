from math import pi, atan2, degrees

def deg2pix(deg):
    dpix = degrees(atan2(.5 * monitor['h'], monitor['d'])) / (.5 * monitor['res'][0])
    return int(deg/dpix)

def sec2frm(sec):
    return int(monitor['Hz'] * sec)

screen = 'mac' # 'mac'

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
    'basecol': (0.5, 0.5, 0.5),
    'probecol': (0.9, 0.9, 0.9)
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
    'fb': sec2frm(0.25)
}

text = {
    'font': 'Courier New',
    'col': (0.5, 0.5, 0.5),
    'size': deg2pix(0.4),
    'fbpos': (0, deg2pix(0.4)),
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

log = [
    'trial', 'order', 'loc', 'tilt', 'tfix',

    'ori1', 'ori2', 'ori3', 'ori4',
    'col1', 'col2', 'col3', 'col4',
    
    'tori1', 'tcol1', 'tloc1',
    'tori2', 'tcol2', 'tloc2',

    'rori1', 'turns1', 'key1',
    'rori2', 'turns2', 'key2',
    
    'dif1', 'perf1', 'rtime1', 'rdur1'
    'dif2', 'perf2', 'rtime2', 'rdur2'
]