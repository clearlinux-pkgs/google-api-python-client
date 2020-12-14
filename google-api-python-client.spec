#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-api-python-client
Version  : 1.10.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/db/03/d29e87227c076345ebf87eea014024ae1299bc097184907807708c3f6dbf/google-api-python-client-1.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/db/03/d29e87227c076345ebf87eea014024ae1299bc097184907807708c3f6dbf/google-api-python-client-1.10.0.tar.gz
Summary  : Google API Client Library for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: google-api-python-client-python = %{version}-%{release}
Requires: google-api-python-client-python3 = %{version}-%{release}
Requires: google-api-core
Requires: google-auth
Requires: google-auth-httplib2
Requires: httplib2
Requires: six
Requires: uritemplate
BuildRequires : buildreq-distutils3
BuildRequires : google-api-core
BuildRequires : google-auth
BuildRequires : google-auth-httplib2
BuildRequires : httplib2
BuildRequires : six
BuildRequires : uritemplate

%description
# Google API Client
[![PyPI version](https://badge.fury.io/py/google-api-python-client.svg)](https://badge.fury.io/py/google-api-python-client)

%package python
Summary: python components for the google-api-python-client package.
Group: Default
Requires: google-api-python-client-python3 = %{version}-%{release}

%description python
python components for the google-api-python-client package.


%package python3
Summary: python3 components for the google-api-python-client package.
Group: Default
Requires: python3-core
Provides: pypi(google_api_python_client)
Requires: pypi(google_api_core)
Requires: pypi(google_auth)
Requires: pypi(google_auth_httplib2)
Requires: pypi(httplib2)
Requires: pypi(six)
Requires: pypi(uritemplate)

%description python3
python3 components for the google-api-python-client package.


%prep
%setup -q -n google-api-python-client-1.10.0
cd %{_builddir}/google-api-python-client-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596515645
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
