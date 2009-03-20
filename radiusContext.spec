# TODO:
# - cron stuff
# - web package with cgi for users
Summary:	RADIUS accounting log analysis package
Name:		radiusContext
Version:	1.93
Release:	0.1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.tummy.com/pub/tummy/radiusContext/%{name}-%{version}.tar.gz
# Source0-md5:	1adb07cb0c645288a50d25f6b22d7fd1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
radiusContext is a RADIUS accounting log analysis package modeled after the
radiusreport package (http://www.tibus.net/pgregg/projects/radiusreport/).

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitedir}}

install latestlist loginlist raddetail stdreport $RPM_BUILD_ROOT%{_bindir}
install *.py $RPM_BUILD_ROOT%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* WHATSNEW samples
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.py[co]
