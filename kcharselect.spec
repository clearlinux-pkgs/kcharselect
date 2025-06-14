#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcharselect
Version  : 25.04.2
Release  : 82
URL      : https://download.kde.org/stable/release-service/25.04.2/src/kcharselect-25.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/25.04.2/src/kcharselect-25.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/25.04.2/src/kcharselect-25.04.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0
Requires: kcharselect-bin = %{version}-%{release}
Requires: kcharselect-data = %{version}-%{release}
Requires: kcharselect-license = %{version}-%{release}
Requires: kcharselect-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Logo is from the breeze-icons repo, with the icon name: accessories-character-map
Images are generated with the following bash command after you get the SVG file from breeze-icons repo:
for s in 16 32 64 128 256 512 1024 ; do rsvg-convert -w${s} -h${s} accessories-character-map.svg > ${s}-apps-kcharselect.png ; done

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kcharselect-25.04.2
cd %{_builddir}/kcharselect-25.04.2
pushd ..
cp -a kcharselect-25.04.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749515578
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749515578
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcharselect
cp %{_builddir}/kcharselect-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kcharselect/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kcharselect-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kcharselect/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/kcharselect-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcharselect/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/kcharselect-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcharselect/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcharselect-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcharselect/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
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
/usr/share/doc/HTML/sl/kcharselect/index.cache.bz2
/usr/share/doc/HTML/sl/kcharselect/index.docbook
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

