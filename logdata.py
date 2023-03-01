from datetime import datetime
import csv, os

from settings import log, logdir

def newLogfile():

    os.chdir(logdir)

    sub = input('Subject: ')
    ses = input('Session: ')
    now = datetime.now().strftime('%m%d%Y_%H%M%S')

    filename = 'rn6_' + sub + '_' + ses + '_' + now + '.csv'

    with open(filename, mode = 'w') as logfile:
        data = csv.DictWriter(logfile, delimiter = ',', fieldnames = log.keys())
        data.writeheader()

    return filename, sub, ses

def addSpec(logdata, data, ki):

    keys = list(map(str, log.keys()))

    keys = keys[ki : ki+len(data)]

    for i, d in enumerate(data):
        logdata[keys[i]] = d

    return logdata

def addTrial(logdata, filename):

    os.chdir(logdir)

    with open(filename, mode = 'a', newline = '') as logfile:
        writer = csv.DictWriter(logfile, fieldnames = log.keys())
        writer.writerow(logdata)