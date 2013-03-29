Name:           caenvnc
Version:        1.0
Release:        1%{?dist}
Summary:        CAEN VNC client

Group:          Applications/Internet
License:        GPL
URL:            http://www.engin.umich.edu/caen/
Source0:        caenvnc
Source1:        caenvnchelper

Requires:       tk, expect, vinagre, openssh-clients
BuildArch:	noarch

%description
CAEN VNC Client

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}/caenvnc
install -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/caenvnchelper

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/caenvnc
%{_bindir}/caenvnchelper

%changelog
* Fri Mar 29 2013 Jonathan S. Billings <jsbillin@umich.edu> - 1.0-1
- Created initial version of spec

