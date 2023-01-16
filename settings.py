from math import pi, atan2, degrees

def deg2pix(deg):

    dpix = degrees(atan2(.5 * monitor['h'], monitor['d'])) / (.5 * monitor['res'][0])
    pix = int(deg/dpix)

    return pix

def sec2frm(sec):

    frm = int(monitor['Hz'] * sec)

    return frm

monitor = {
    'res': (1536,960), 
    'Hz': 120, # Temporary bug fix
    'col': (-0.3, -0.3, -0.3),
    'h': 22,
    'd': 50
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
    'ltpos': (-deg2pix(1), deg2pix(2)),
    'tpos': (0, deg2pix(2)),
    'rtpos': (deg2pix(1), deg2pix(2)),
    'bpos': (0, -deg2pix(2))
}
