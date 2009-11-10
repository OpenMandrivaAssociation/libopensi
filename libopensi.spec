%define name	libopensi
%define version 1.0
%define rel	18

Summary:	Library for OpenSi
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:	http://download.gna.org/opensi/%name/%name-%version.tgz
License:	MPL
Group:		System/Libraries
Url:		http://opensi.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	firefox-devel
Requires:	firefox = %{firefox_epoch}:%{firefox_version}

%description
Library for OpenSi.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %buildroot
# Jar for the translation
mkdir -p %{buildroot}%{firefox_mozillapath}/chrome/
cp -r `pwd`  %{buildroot}%{firefox_mozillapath}/chrome/
# installed-chrome.txt addition
mkdir -p %{buildroot}%{firefox_mozillapath}/chrome/rc.d/
cat << EOF > %{buildroot}%{firefox_mozillapath}/chrome/rc.d/10_%{name}.txt
content,install,url,resource:/chrome/libopensi/content/libopensi/
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{firefox_mozillapath}/chrome/libopensi
%{firefox_mozillapath}/chrome/rc.d/*.txt
