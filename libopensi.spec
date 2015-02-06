%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Library for OpenSi
Name:		libopensi
Version:	1.0
Release:	21
Source0:	http://download.gna.org/opensi/%{name}/%{name}-%{version}.tgz
License:	MPL
Group:		System/Libraries
Url:		http://opensi.org/
BuildRequires:	firefox-devel
Requires:	firefox >= %{firefox_epoch}:%{firefox_version}

%description
Library for OpenSi.

%prep
%setup -q -n %{name}

%build

%install
# Jar for the translation
mkdir -p %{buildroot}%{firefox_mozillapath}/chrome/
cp -r `pwd`  %{buildroot}%{firefox_mozillapath}/chrome/
# installed-chrome.txt addition
mkdir -p %{buildroot}%{firefox_mozillapath}/chrome/rc.d/
cat << EOF > %{buildroot}%{firefox_mozillapath}/chrome/rc.d/10_%{name}.txt
content,install,url,resource:/chrome/libopensi/content/libopensi/
EOF

%files
%{firefox_mozillapath}/chrome/libopensi
%{firefox_mozillapath}/chrome/rc.d/*.txt

