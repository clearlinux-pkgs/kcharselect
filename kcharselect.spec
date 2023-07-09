#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcharselect
Version  : 23.04.3
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.04.3/src/kcharselect-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/kcharselect-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/kcharselect-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0
Requires: kcharselect-bin = %{version}-%{release}
Requires: kcharselect-data = %{version}-%{release}
Requires: kcharselect-license = %{version}-%{release}
Requires: kcharselect-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kcharselect-23.04.3
cd %{_builddir}/kcharselect-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688864565
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688864565
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcharselect
cp %{_builddir}/kcharselect-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kcharselect/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kcharselect-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kcharselect/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/kcharselect-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcharselect/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/kcharselect-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcharselect/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcharselect-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcharselect/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kcharselect
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kcharselect
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
/usr/share/doc/HTML/it/kcharselect/kcharselect.png
/usr/share/doc/HTML/ko/kcharselect/index.cache.bz2
/usr/share/doc/HTML/ko/kcharselect/index.docbook
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
/usr/share/doc/HTML/sr@latin/kcharselect/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kcharselect/index.docbook
/usr/share/doc/HTML/sv/kcharselect/index.cache.bz2
/usr/share/doc/HTML/sv/kcharselect/index.docbook
/usr/share/doc/HTML/tr/kcharselect/index.cache.bz2
/usr/share/doc/HTML/tr/kcharselect/index.docbook
/usr/share/doc/HTML/tr/kcharselect/kcharselect.png
/usr/share/doc/HTML/uk/kcharselect/index.cache.bz2
/usr/share/doc/HTML/uk/kcharselect/index.docbook
/usr/share/doc/HTML/uk/kcharselect/kcharselect.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcharselect/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kcharselect/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kcharselect/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kcharselect/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcharselect/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f kcharselect.lang
%defattr(-,root,root,-)

