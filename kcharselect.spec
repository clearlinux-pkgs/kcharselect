#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcharselect
Version  : 19.04.0
Release  : 7
URL      : https://download.kde.org/stable/applications/19.04.0/src/kcharselect-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/kcharselect-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/kcharselect-19.04.0.tar.xz.sig
Summary  : Character Selector
Group    : Development/Tools
License  : GPL-2.0
Requires: kcharselect-bin = %{version}-%{release}
Requires: kcharselect-data = %{version}-%{release}
Requires: kcharselect-license = %{version}-%{release}
Requires: kcharselect-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
No detailed description available

%package bin
Summary: bin components for the kcharselect package.
Group: Binaries
Requires: kcharselect-data = %{version}-%{release}
Requires: kcharselect-license = %{version}-%{release}

%description bin
bin components for the kcharselect package.


%package data
Summary: data components for the kcharselect package.
Group: Data

%description data
data components for the kcharselect package.


%package doc
Summary: doc components for the kcharselect package.
Group: Documentation

%description doc
doc components for the kcharselect package.


%package license
Summary: license components for the kcharselect package.
Group: Default

%description license
license components for the kcharselect package.


%package locales
Summary: locales components for the kcharselect package.
Group: Default

%description locales
locales components for the kcharselect package.


%prep
%setup -q -n kcharselect-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557004195
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557004195
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcharselect
cp COPYING %{buildroot}/usr/share/package-licenses/kcharselect/COPYING
pushd clr-build
%make_install
popd
%find_lang kcharselect

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kcharselect

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kcharselect.desktop
/usr/share/metainfo/org.kde.kcharselect.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcharselect/index.cache.bz2
/usr/share/doc/HTML/ca/kcharselect/index.docbook
/usr/share/doc/HTML/cs/kcharselect/index.cache.bz2
/usr/share/doc/HTML/cs/kcharselect/index.docbook
/usr/share/doc/HTML/de/kcharselect/index.cache.bz2
/usr/share/doc/HTML/de/kcharselect/index.docbook
/usr/share/doc/HTML/de/kcharselect/kcharselect.png
/usr/share/doc/HTML/el/kcharselect/index.cache.bz2
/usr/share/doc/HTML/el/kcharselect/index.docbook
/usr/share/doc/HTML/el/kcharselect/kcharselect.png
/usr/share/doc/HTML/en/kcharselect/index.cache.bz2
/usr/share/doc/HTML/en/kcharselect/index.docbook
/usr/share/doc/HTML/en/kcharselect/kcharselect.png
/usr/share/doc/HTML/es/kcharselect/index.cache.bz2
/usr/share/doc/HTML/es/kcharselect/index.docbook
/usr/share/doc/HTML/et/kcharselect/index.cache.bz2
/usr/share/doc/HTML/et/kcharselect/index.docbook
/usr/share/doc/HTML/fr/kcharselect/index.cache.bz2
/usr/share/doc/HTML/fr/kcharselect/index.docbook
/usr/share/doc/HTML/gl/kcharselect/index.cache.bz2
/usr/share/doc/HTML/gl/kcharselect/index.docbook
/usr/share/doc/HTML/it/kcharselect/index.cache.bz2
/usr/share/doc/HTML/it/kcharselect/index.docbook
/usr/share/doc/HTML/nl/kcharselect/index.cache.bz2
/usr/share/doc/HTML/nl/kcharselect/index.docbook
/usr/share/doc/HTML/pt/kcharselect/index.cache.bz2
/usr/share/doc/HTML/pt/kcharselect/index.docbook
/usr/share/doc/HTML/pt_BR/kcharselect/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcharselect/index.docbook
/usr/share/doc/HTML/pt_BR/kcharselect/kcharselect.png
/usr/share/doc/HTML/ru/kcharselect/index.cache.bz2
/usr/share/doc/HTML/ru/kcharselect/index.docbook
/usr/share/doc/HTML/sr/kcharselect/index.cache.bz2
/usr/share/doc/HTML/sr/kcharselect/index.docbook
/usr/share/doc/HTML/sv/kcharselect/index.cache.bz2
/usr/share/doc/HTML/sv/kcharselect/index.docbook
/usr/share/doc/HTML/uk/kcharselect/index.cache.bz2
/usr/share/doc/HTML/uk/kcharselect/index.docbook
/usr/share/doc/HTML/uk/kcharselect/kcharselect.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcharselect/COPYING

%files locales -f kcharselect.lang
%defattr(-,root,root,-)

