#!/usr/bin/env python

import os, sys

sys.path.insert(0,os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print(sys.path)

from tmath_tables_py.train import main

if __name__ == '__main__': 
    main()
