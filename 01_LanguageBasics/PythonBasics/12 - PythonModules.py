# MODULI
import os    # modul importan direktno, treba ih referincirati s full package name
print (os.path.abspath("."))

import os as regexp         # import, ali s drugacijim nazivom namespacea
print regexp.search('a', 'a')

import os.path              # moze se importati i submodul, uz kompletno referenciranje
print (os.path.abspath("."))

from datetime import date
print date.today()


# POPIS NAJKORISNIJIH MODULA
import string       # stringovi - http://docs.python.org/library/string.html
import re           # reghularni izrazi - http://docs.python.org/library/re.html
import datetime     # http://docs.python.org/library/datetime.html
import calendar     # http://docs.python.org/library/calendar.html
import math         # http://docs.python.org/library/math.html
import cmath        # kompleksni brojevi http://docs.python.org/library/cmath.html
import decimal      # decimal floating point arithmetic - http://docs.python.org/library/decimal.html
import os           # http://docs.python.org/library/os.html
import os.path      # common pathname manipulacije - http://docs.python.org/library/os.path.html
import sys          # system-specific parameters & functions - http://docs.python.org/library/sys.html
import pickle       # python object serialization - http://docs.python.org/library/pickle.html
import cPickle      # native C verzija, (do 1000 puta brza) - http://docs.python.org/library/pickle.html#module-cPickle
import marshal      # internal python object serialization - http://docs.python.org/library/marshal.html
import sqlite3      # interfejs za SQLite baze - http://docs.python.org/library/sqlite3.html
import zlib         # za compress/decompress - http://docs.python.org/library/zlib.html
import zipfile      # rad s ZIP arhivama - http://docs.python.org/library/zipfile.html
import csv          # rad s CSV fajlovima - http://docs.python.org/library/csv.html
import hashlib      # za rad s hashevima - http://docs.python.org/library/hashlib.html
import logging      # za rad s logovima - http://docs.python.org/library/logging.html
import json         # JSON encoder / decoder - http://docs.python.org/library/json.html
import HTMLParser   # simple html parser - http://docs.python.org/library/htmlparser.html
import webbrowser   # web-browse controller - http://docs.python.org/library/webbrowser.html
import urllib2      # library for opening URLs - http://docs.python.org/library/urllib2.html



