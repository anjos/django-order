#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sun 28 Feb 19:33:29 2010 

"""Creates or updates the bootstrap script with virtualenv
"""

import os, sys

if len(sys.argv) != 3:
  print '%s: <output.py> <extra_text.py>' % os.path.basename(sys.argv[0])
  sys.exit(1)

import virtualenv
f = open(sys.argv[1], 'wt')
extra = open(sys.argv[2], 'rt')
f.write(virtualenv.create_bootstrap_script(extra.read()))
f.close()
extra.close()
