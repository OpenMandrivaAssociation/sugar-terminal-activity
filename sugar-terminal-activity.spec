# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-terminal-activity
Version: 21
Release: %mkrel 1
Summary: Terminal for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Terminal/Terminal-21.tar.bz2

Requires: sugar-toolkit >= 0.83.6
Requires: python-vte >= 0.17

BuildRequires: sugar-toolkit >= 0.83.6
BuildRequires: gettext  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
The terminal activity provides a vte-based terminal for the Sugar interface.

%prep
%setup -q -n Terminal-21


%build
python  \
	setup.py \
	build

%install
rm -rf %{buildroot}
[ -f setup.py ] && chmod 0755 setup.py
python  \
	setup.py \
	install \
	--prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.Terminal

%clean
rm -rf %{buildroot}

%files -f org.laptop.Terminal.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc COPYING MAINTAINERS NEWS README

