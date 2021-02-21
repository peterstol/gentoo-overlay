#!/usr/bin/env python3

import yaml, sys

# Define how to use the program

usage = """Usage: foo.py [eessi version YYYY.MM]
   e.g. 2021.02 with data in eessi_sets.yml"""

if len(sys.argv) != 2:
    print(usage)
    sys.exit(0)

version = sys.argv[1]

# Define prefix for set file.
prefix = 'eessi-'+version+'-'

with open('eessi_sets.yml') as d:

   data = yaml.load_all(d, Loader=yaml.FullLoader)

   for doc in data:
     for k, v in doc.items():
        with open(prefix+k, 'w') as f:
           print( *v, sep = "\n", file=f)
