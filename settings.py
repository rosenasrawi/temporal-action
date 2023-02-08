from math import pi, atan2, degrees
import itertools

def deg2pix(deg):
    dpix = degrees(atan2(.5 * monitor['h'], monitor['d'])) / (.5 * monitor['res'][0])
    return int(deg/dpix)

def sec2frm(sec):
    return int(monitor['Hz'] * sec)

screen = 'mac'
# screen = 'lab'

if screen == 'lab':
    logdir = r'C:\Users\memticipation-std\Desktop\[Server Data] (previously uploaded data can be found here)\Betul-Rose\logfiles'
    eyedir = r'C:\Users\memticipation-std\Desktop\[Server Data] (previously uploaded data can be found here)\Betul-Rose\logfiles'
    res = (1920,1080); Hz = 239
    h = 30; d = 50

elif screen == 'mac':
    logdir = '/Users/rosenasrawi/Documents/VU PhD/Projects/rn6 - Temporal action/Data/Logfiles'
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
    'basecol': (0.2, 0.2, 0.2),
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

calib = {
    'rad': deg2pix(0.15),
    'mrad': deg2pix(0.075),
    'edge': deg2pix(1),
    'line': deg2pix(0.05),
    'col': (0.5, 0.5, 0.5),
    'mcol': (-0.3, -0.3, -0.3),
    'pos': list(itertools.product([-bar['shift'], 0, bar['shift']],
                                  [bar['shift'], 0, -bar['shift']])),
    'count': ('', '3', '', '2', '', '1', '')
}

timing = {
    'fix': (sec2frm(.5), sec2frm(.8)),
    'enc': sec2frm(.25),
    'del1': sec2frm(1.25),
    'del2': sec2frm(1.75),
    'del3': sec2frm(1),
    'del4': sec2frm(.5),
    'fb': sec2frm(.25),
    'calib': sec2frm(1),
    'count': sec2frm(.5)
}

text = {
    'font': 'Courier New',
    'col': (0.5, 0.5, 0.5),
    'size': deg2pix(0.4),
    'fbpos': (0, 0),
    'lpos': (-deg2pix(3), 0),
    'rpos': (deg2pix(3), 0),
    'bpos': (0, -deg2pix(2)),
    'tpos': (0, deg2pix(2))
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
    'respR2': 70,
    'calib': [0,1,2,3,4,5,6,7,8]
}

log = {
    'trial': None, 'order': None, 'loc': None, 'tilt': None,

    'ori1': None, 'ori2': None, 'ori3': None, 'ori4': None,
    'col1': None, 'col2': None, 'col3': None, 'col4': None,
    
    'tori1': None, 'tcol1': None, 'tloc1': None,
    'tori2': None, 'tcol2': None, 'tloc2': None,

    'rori1': None, 'turns1': None, 'key1': None, 'perf1': None, 'diff1': None,
    'rori2': None, 'turns2': None, 'key2': None, 'perf2': None, 'diff2': None,

    'trigenc1': None, 'trigenc2': None, 
    'trigprobe1': None, 'trigprobe2': None,
    'trigresp1': None, 'trigresp2': None
}

runs = {
    'practice': [1,2,3,4,5,6,7,8],
    'block': [1,2,3,4,5,6,7,8],
    'ptotal': 4,
    'stotal': 2
}