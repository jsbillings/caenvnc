Name:           caenvnc
Version:        %{caenvnc_version} 
Release:        %{caenvnc_release}%{?dist}.1
Summary:        CAEN VNC client

Group:          Applications/Internet
License:        GPL
URL:            http://www.engin.umich.edu/caen/
Source0:        caenvnc
Source1:        caenvnchelper
Source2:        caenvnc.desktop

Requires:       tk, expect, vinagre, openssh-clients, nc
BuildArch:	noarch

%description
CAEN VNC Client

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}/caenvnc
install -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/%{_bindir}/caenvnchelper
install -D -m 0755 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/applications/caenvnc.desktop

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/caenvnc
%{_bindir}/caenvnchelper
%{_datadir}/applications/caenvnc.desktop

%changelog
* Wed Sep 04 2013 Jonathan S. Billings <jsbillin@umich.edu> - 1.0-1.1
- Added caenvnc.desktop

* Fri Mar 29 2013 Jonathan S. Billings <jsbillin@umich.edu> - 1.0-1
- Created initial version of spec

