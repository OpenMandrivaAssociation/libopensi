%define name	libopensi
%define version 1.0
%define rel	13
%define firefox_version %(rpm -q --whatprovides mozilla-firefox --queryformat %{VERSION})
%define firefox_epoch %(rpm -q --whatprovides mozilla-firefox --queryformat %{EPOCH})
%define mozillalibdir %{_libdir}/firefox-%{firefox_version}

Summary:	Library for OpenSi
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:	http://download.gna.org/opensi/%name/%name-%version.tgz
License:	MPL
Group:		System/Libraries
Url:		http://opensi.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mozilla-firefox
Requires(pre):	mozilla-firefox = %{firefox_epoch}:%{firefox_version}

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
