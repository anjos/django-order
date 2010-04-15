# Dear emacs, this is -*- Makefile -*-
# Created by Andre Anjos <Andre.dos.Anjos@gmail.com>, 20-Mar-2007

INSTALLDIR=sw
SCRIPT=bootstrap.py

all: generate

.PHONY: clean generate mrproper

generate:
	@rm -f ${SCRIPT} && ./make_bootstrap.sh ${INSTALLDIR}

clean: 
	@find . -name '*~' -print0 | xargs -0 rm -vf 
	@rm -rf ${SCRIPT} ${INSTALLDIR}

mrproper: clean
	@rm -rf ${INSTALLDIR} ez_setup.py
