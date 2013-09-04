#!/usr/bin/make

VERSION := $(shell cat VERSION)
RELEASE := $(shell git describe --abbrev=4 HEAD 2>/dev/null | tr '-' '_')

clean:
	rm -rf rpmbuild

debian: deb

deb:	
	cp -r packaging/debian ./
	chmod 755 debian/rules
	fakeroot debian/rules clean
	fakeroot debian/rules
	fakeroot debian/rules binary

make_rpm:
	mkdir -p rpmbuild/SOURCES rpmbuild/SPECS
	cp caenvnc caenvnchelper caenvnc.desktop rpmbuild/SOURCES
	cp packaging/redhat/caenvnc.spec rpmbuild/SPECS

srpm:	make_rpm
	rpmbuild --define "caenvnc_version $(VERSION)" \
	--define "caenvnc_release $(RELEASE)" \
	--define "_topdir %(pwd)/rpmbuild" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_specdir %{_topdir}/SPECS" \
	--define "_sourcedir %{_topdir}/SOURCES" \
	-bs rpmbuild/SPECS/caenvnc.spec

rpm:	make_rpm
	rpmbuild --define "caenvnc_version $(VERSION)" \
	--define "caenvnc_release $(RELEASE)" \
	--define "_topdir %(pwd)/rpmbuild" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_specdir %{_topdir}/SPECS" \
	--define "_sourcedir %{_topdir}/SOURCES" \
	-ba rpmbuild/SPECS/caenvnc.spec
