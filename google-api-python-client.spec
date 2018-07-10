#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-api-python-client
Version  : 1.6.7
Release  : 30
URL      : http://pypi.debian.net/google-api-python-client/google-api-python-client-1.6.7.tar.gz
Source0  : http://pypi.debian.net/google-api-python-client/google-api-python-client-1.6.7.tar.gz
Summary  : Google API Client Library for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: google-api-python-client-python3
Requires: google-api-python-client-python
Requires: httplib2
Requires: oauth2client
Requires: six
Requires: uritemplate
BuildRequires : httplib2
BuildRequires : oauth2client
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : uritemplate

%description
accessing the Plus, Moderator, and many other Google APIs.

%package python
Summary: python components for the google-api-python-client package.
Group: Default
Requires: google-api-python-client-python3

%description python
python components for the google-api-python-client package.


%package python3
Summary: python3 components for the google-api-python-client package.
Group: Default
Requires: python3-core

%description python3
python3 components for the google-api-python-client package.


%prep
%setup -q -n google-api-python-client-1.6.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525185774
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
