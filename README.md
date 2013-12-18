CAEN VNC Client
===============

The CAEN VNC client is a package that installs the 'caenvnc' script, along with helper scripts and all the requirements needed to connect to the [CAEN VNC service](http://caen.engin.umich.edu/connect/linux-login-service).

Building
========

Debian/Ubuntu (.deb)

    $ make clean
    $ make deb

The package will appear in the current directory

Redhat/Fedora (.rpm)

    $ make clean
    $ make rpm

The package will appear in ./rpmbuild/noarch/
