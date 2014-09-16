import os
import csv

from invoke import task

DATA_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '../tmp'))


def _get_header(reader):
    next(reader)
    next(reader)
    return [i.lower().replace(" ", "_") for i in next(reader)]


def _read_csv(fpath):
    result = []

    with open(fpath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = _get_header(reader)
        for row in reader:
            item = dict(zip(header, row))
            result.append(item)

    return result


@task
def build(fname):
    '''
    $ invoke hi thefname
    $ invoke hi --name thefname
    '''

    fpath = os.path.join(DATA_PATH, fname)
    print('Importing data from csv {}'.format(fpath))
    rows = _read_csv(fpath)
    print('Done !')
