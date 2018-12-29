#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-api-python-client
Version  : 1.7.6
Release  : 34
URL      : https://files.pythonhosted.org/packages/83/c6/cf9c3c66e986f800c160fdd2ee3d42e172facdcf450c6ccdccb132d21d0c/google-api-python-client-1.7.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/c6/cf9c3c66e986f800c160fdd2ee3d42e172facdcf450c6ccdccb132d21d0c/google-api-python-client-1.7.6.tar.gz
Summary  : Google API Client Library for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: google-api-python-client-python = %{version}-%{release}
Requires: google-api-python-client-python3 = %{version}-%{release}
Requires: google-auth
Requires: google-auth-httplib2
Requires: httplib2
Requires: six
Requires: uritemplate
BuildRequires : buildreq-distutils3
BuildRequires : google-auth
BuildRequires : google-auth-httplib2
BuildRequires : httplib2
BuildRequires : six
BuildRequires : uritemplate

%description
accessing the Plus, Moderator, and many other Google APIs.

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

%description python3
python3 components for the google-api-python-client package.


%prep
%setup -q -n google-api-python-client-1.7.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544139959
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
