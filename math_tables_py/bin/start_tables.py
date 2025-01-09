#!/usr/bin/env python

import os, sys

from ..train import main

sys.path.insert(0,os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(sys.path)

if __name__ == '__main__': 
    main()
