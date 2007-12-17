%define name	libopensi
%define version 1.0
%define release 3
#(peroyvind): yes, doing this twice is done on purpose to work around weird issue..
%{expand:%%define firefox_version %(mozilla-firefox-config --version)}
%{expand:%%define firefox_version %(mozilla-firefox-config --version)}
%define mozillalibdir %{_libdir}/mozilla-firefox-%{firefox_version}

Summary:	Library for OpenSi
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{name}-%{version}.tar.bz2
License:	MPL
Group:		System/Libraries
Url:		http://opensi.org/
BuildRequires:	mozilla-firefox
Requires(pre):	mozilla-firefox = %{firefox_version}

%description
Library for OpenSi.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %buildroot
# Jar for the translation
mkdir -p %{buildroot}%{mozillalibdir}/chrome/
cp -r `pwd`  %{buildroot}%{mozillalibdir}/chrome/
# installed-chrome.txt addition
mkdir -p %{buildroot}%{mozillalibdir}/chrome/rc.d/
cat << EOF > %{buildroot}%{mozillalibdir}/chrome/rc.d/10_%{name}.txt
content,install,url,resource:/chrome/libopensi/content/libopensi/
EOF

%post
if test -x %{mozillalibdir}/mozilla-rebuild-databases.pl; then %{mozillalibdir}/mozilla-rebuild-databases.pl; fi

%postun
if test -x %{mozillalibdir}/mozilla-rebuild-databases.pl; then %{mozillalibdir}/mozilla-rebuild-databases.pl; fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{mozillalibdir}/chrome/%{name}
%{mozillalibdir}/chrome/rc.d/10_%{name}.txt

