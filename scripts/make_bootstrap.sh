#!/bin/bash 
# Created by Andre Anjos <andre.dos.anjos@cern.ch>
# Sex 04 Abr 2008 14:36:05 CEST

if [ $# != 1 ]; then
  echo "usage: $0 <installdir>";
  exit 1;
fi

# Base environment definitions
export PYTHONPATH=$1
export PATH=$1:${PATH}

# Automatically set!
python_version=`python -c 'import sys;print "%d.%d" % sys.version_info[0:2]'`

# We install/upgrade the setuptools
echo "### Installing 'virtualenv'..."
[ ! -d $1 ] && mkdir $1;
[ -f ez_setup.py ] && rm -f ez_setup.py;
wget --quiet http://peak.telecommunity.com/dist/ez_setup.py;
python ez_setup.py --install-dir=$1 --quiet --upgrade virtualenv;

# Now we generate the bootstrap script 
echo "### Generating bootstrap..."
python ./make_bootstrap.py bootstrap.py ./extra_text.py
chmod 755 ./bootstrap.py
echo "### Done!"

exit 0;
