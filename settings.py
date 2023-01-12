from math import pi, atan2, degrees

# Monitor settings

monitor = {'res': (1536,960), 
           'Hz': 120, # Temporary bug fix
           'col': (-0.3, -0.3, -0.3),
           'h': 22,
           'd': 50}

# Degree visual angles to pixels

def deg2pix(deg):

    dpix = degrees(atan2(.5 * monitor['h'], monitor['d'])) / (.5 * monitor['res'][0])
    pix = int(deg/dpix)

    return pix

def sec2frm(sec):

    frm = int(monitor['Hz'] * sec)

    return frm

# Stimuli

fix = {
    'size': deg2pix(0.2),
    'line': deg2pix(0.05),
    'basecol': (0.5, 0.5, 0.5),
    'probecol': (0.9, 0.9, 0.9)
}

bar = {
    'size': (deg2pix(0.4), deg2pix(3)),
    'shift': deg2pix(4),
    'cols': ["#ff8a65","#64b5f6","#81c784","#ce93d8"]
}

dial = {
    'rad': deg2pix(1.5),
    'hrad': deg2pix(0.15),
    'edge': deg2pix(1),
    'line': deg2pix(0.05),
    'col': (0.5, 0.5, 0.5),
    'hpos': deg2pix(1.5)
}


# Timing

timing = {
    'fix': (sec2frm(.5), sec2frm(.8)),
    'enc': sec2frm(.25),
    'del1': sec2frm(1.25),
    'del2': sec2frm(1.75),
    'del3': sec2frm(1)
}

trange = {
    'L': (-80, -10),
    'R': (10, 80)
}

turn = {
    'max': monitor['Hz'],
    'rad': (0.5*pi) / monitor['Hz']
}

