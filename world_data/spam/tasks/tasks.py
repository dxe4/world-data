import os
import csv

import pycountry
from invoke import task

from spam.models import Country, CountryInfo
from spam.util import get_indicator_details


DATA_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '../tmp'))


def _get_header(reader):
    next(reader)
    next(reader)
    return [i.lower().replace(" ", "_") for i in next(reader)]


# TODO the color map staff somehow need to be tested
def _transorm(a, b, ab_diff, x_diff, x_min, value):
    new_value = a + ((ab_diff) / (x_diff)) * (value - x_min)
    new_value = abs(b - new_value) * 2.5
    new_value = '#%02x%02x%02x' % (new_value, new_value, new_value)
    return new_value


def to_color_map(values, a=0, b=50):
    result = []

    ab_diff = b - a
    x_min = min(values)
    x_max = max(values)
    x_diff = x_max - x_min

    for i in values:
        val = a + ((ab_diff) / (x_diff)) * (i - x_min)
        result.append(val)

    return result


def convert_country_code(alpha3):
    country = pycountry.countries.get(alpha3=alpha3)
    return country.alpha2


def make_country(row):
    code_3 = row.pop('country_code')
    code_2 = convert_country_code(code_3)
    name = row.pop('country_name')

    country = Country(code_3=code_3,
                      code_2=code_2,
                      name=name)
    return country


def make_country_info(row):
    '''
    WARNING by design this depends on state
    make_country has to be called first
    '''
    indicator_name = row.pop('idnicator_name')
    indicator_id, indicator_code = get_indicator_details()

    years = row.keys()
    values = [float(i) for i in row.values()]
    color_map_values = to_color_map(values)

    country_info = CountryInfo(indicator_name=indicator_name,
                               indicator_id=indicator_id,
                               indicator_code=indicator_code,
                               years=years, values=values,
                               color_map_values=color_map_values)
    return country_info


def make_objects(row):
    country = make_country(row)
    country_info = make_country_info(row)
    return country, country_info


def _read_csv(fpath):
    result = []

    with open(fpath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        header = _get_header(reader)

        for csv_row in reader:
            row = dict(zip(header, csv_row))
            country, country_info = make_objects(row)
            result.append([country, country_info])

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
