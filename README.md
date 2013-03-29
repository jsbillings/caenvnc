CAEN VNC Client
===============

The CAEN VNC client is a package that installs the 'caenvnc' script, along with helper scripts and all the requirements needed to connect to the [CAEN VNC service](http://www.engin.umich.edu/caen/connect/vnc.html).

Building
========

Debian/Ubuntu

    $ make clean
    $ make deb

The package will appear in ..

Redhat/Fedora

    $ make clean
    $ make rpm

The package will appear in ./rpmbuild/noarch/
