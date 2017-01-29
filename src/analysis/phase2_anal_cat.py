'''
Phase 2 analysis
'''

import os, csv, xlrd, collections
def readFile(rater1File, rater2File):
      with open(rater1File, 'rU') as f1:
        reader1 = csv.reader(f1)
        next(reader1, None)

      with open(rater2File, 'rU') as f2:
        reader2 = csv.reader(f2)
        next(reader2, None)
