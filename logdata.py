from datetime import datetime
import csv, os

from settings import log

def newLogfile():

    sub = input('Subject: ')
    now = datetime.now().strftime('%m%d%Y_%H%M%S')

    filename = 'rn6_' + sub + '_' + now + '.csv'

    with open(filename, mode = 'w') as logfile:
        data = csv.DictWriter(logfile, delimiter = ',', fieldnames = log)
        data.writeheader()

