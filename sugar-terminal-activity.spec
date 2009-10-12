# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-terminal-activity
Version: 28
Release: %mkrel 1
Summary: Terminal for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Terminal/Terminal-28.tar.bz2

Requires: python-simplejson  
Requires: sugar-toolkit >= 0.86.1
Requires: python-vte >= 0.17

BuildRequires: gettext  
BuildRequires: sugar-toolkit >= 0.86.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
The terminal activity provides a vte-based terminal for the Sugar interface.

%prep
%setup -q -n Terminal-28


%build

rm -f MANIFEST
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
%find_lang org.laptop.Terminal

%clean
rm -rf %{buildroot}

%files -f org.laptop.Terminal.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc COPYING MAINTAINERS NEWS README

