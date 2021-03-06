IN = install
GZ = gzip -f
RM = rm -rf
PY = python

all: install

install: docs bashcomp
	$(PY) setup.py install

docs: man/tt.1
	$(IN) man/tt.1 /usr/share/man/man1/tt.1
	$(GZ) /usr/share/man/man1/tt.1

bashcomp: contrib/tt-completion.bash
	$(IN) -m 755 contrib/tt-completion.bash /etc/bash_completion.d/tt

uninstall:
	$(RM) /etc/bash_completion.d/tt
	$(RM) /usr/share/man/man1/tt.1.gz
	$(RM) /usr/local/lib/python2.7/dist-packages/tt-*
	$(RM) /usr/local/bin/tt

clean:
	$(RM) tt.egg-info/ build/ dist/
