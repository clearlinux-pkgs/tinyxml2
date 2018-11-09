#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tinyxml2
Version  : 7.0.0
Release  : 7
URL      : https://github.com/leethomason/tinyxml2/archive/7.0.0.tar.gz
Source0  : https://github.com/leethomason/tinyxml2/archive/7.0.0.tar.gz
Summary  : simple, small, C++ XML parser
Group    : Development/Tools
License  : Zlib
Requires: tinyxml2-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
Patch1: cve-2018-11210.nopatch

%description
The (default) Release configuration of this project builds a ready to use static library.
The Debug configuration of this project builds an executable console application that
executes all tests provided for tinyxml2 in the xmltest.cpp file.

%package abi
Summary: abi components for the tinyxml2 package.
Group: Default

%description abi
abi components for the tinyxml2 package.


%package dev
Summary: dev components for the tinyxml2 package.
Group: Development
Requires: tinyxml2-lib = %{version}-%{release}
Provides: tinyxml2-devel = %{version}-%{release}

%description dev
dev components for the tinyxml2 package.


%package lib
Summary: lib components for the tinyxml2 package.
Group: Libraries

%description lib
lib components for the tinyxml2 package.


%prep
%setup -q -n tinyxml2-7.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541748089
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1541748089
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files abi
%defattr(-,root,root,-)
/usr/share/abi/libtinyxml2.so.7.0.0.abi

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/cmake/tinyxml2/tinyxml2Config.cmake
/usr/lib64/cmake/tinyxml2/tinyxml2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/tinyxml2/tinyxml2Targets.cmake
/usr/lib64/libtinyxml2.so
/usr/lib64/pkgconfig/tinyxml2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtinyxml2.so.7
/usr/lib64/libtinyxml2.so.7.0.0
