#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-api-python-client
Version  : 1.4.2
Release  : 1
URL      : https://pypi.python.org/packages/source/g/google-api-python-client/google-api-python-client-1.4.2.tar.gz
Source0  : https://pypi.python.org/packages/source/g/google-api-python-client/google-api-python-client-1.4.2.tar.gz
Summary  : Google API Client Library for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: google-api-python-client-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the google-api-python-client package.
Group: Default

%description python
python components for the google-api-python-client package.


%prep
%setup -q -n google-api-python-client-1.4.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
