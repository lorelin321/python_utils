# read the data as sequence of tuples
#  the csv library is programmed to use the encoding rules use by Microsoft Excel

import csv
import re
from collections import namedtuple

csv_file_name = 'midas_extract.csv'
with open(csv_file_name) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    # for row in f_csv:
    #      row is a tuple in this example
    #      to access certain fields, we need to use indexing

# without using indexing

with open(csv_file_name) as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)

        # process row

# reading tab delimited values

with open(csv_file_name) as f:
    f_csv = csv.reader(f, delimiter='\t')
    for row in f_csv:
        pass
#         process row


# scrub the headers for a safer evaluation
# re module for regular expressions

with open(csv_file_name) as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        assert isinstance(r, object)
        row = Row(*r)
# process rows

# convert csv data types

col_types = [str, float, str, str]
with open(csv_file_name) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))


# reading dicts using type conversions
print('Reading as dicts with type conversion')
field_types = [('Price', float), ('Change', float), ('Volumn', int)]

with open(csv_file_name) as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)