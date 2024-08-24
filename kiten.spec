#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kiten
Version  : 24.08.0
Release  : 72
URL      : https://download.kde.org/stable/release-service/24.08.0/src/kiten-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/kiten-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/kiten-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-1.0 GPL-2.0 LGPL-2.0
Requires: kiten-bin = %{version}-%{release}
Requires: kiten-data = %{version}-%{release}
Requires: kiten-lib = %{version}-%{release}
Requires: kiten-license = %{version}-%{release}
Requires: kiten-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# <img src="logo.png" width="40"/> Kiten
A Japanese reference tool.
<a href='https://flathub.org/apps/details/org.kde.kiten'><img width='190px' alt='Download on Flathub' src='https://flathub.org/assets/badges/flathub-badge-i-en.png'/></a>

%package bin
Summary: bin components for the kiten package.
Group: Binaries
Requires: kiten-data = %{version}-%{release}
Requires: kiten-license = %{version}-%{release}

%description bin
bin components for the kiten package.


%package data
Summary: data components for the kiten package.
Group: Data

%description data
data components for the kiten package.


%package dev
Summary: dev components for the kiten package.
Group: Development
Requires: kiten-lib = %{version}-%{release}
Requires: kiten-bin = %{version}-%{release}
Requires: kiten-data = %{version}-%{release}
Provides: kiten-devel = %{version}-%{release}
Requires: kiten = %{version}-%{release}

%description dev
dev components for the kiten package.


%package doc
Summary: doc components for the kiten package.
Group: Documentation

%description doc
doc components for the kiten package.


%package lib
Summary: lib components for the kiten package.
Group: Libraries
Requires: kiten-data = %{version}-%{release}
Requires: kiten-license = %{version}-%{release}

%description lib
lib components for the kiten package.


%package license
Summary: license components for the kiten package.
Group: Default

%description license
license components for the kiten package.


%package locales
Summary: locales components for the kiten package.
Group: Default

%description locales
locales components for the kiten package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kiten-24.08.0
cd %{_builddir}/kiten-24.08.0
pushd ..
cp -a kiten-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724524601
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
export SOURCE_DATE_EPOCH=1724524601
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiten
cp %{_builddir}/kiten-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kiten/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
cp %{_builddir}/kiten-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kiten/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kiten-%{version}/LICENSES/GPL-1.0-or-later.txt %{buildroot}/usr/share/package-licenses/kiten/e154343fcf8229d714c82906b31df9822fd08ebf || :
cp %{_builddir}/kiten-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kiten/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kiten-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kiten/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kiten-%{version}/data/font/KanjiStrokeOrders.ttf.license %{buildroot}/usr/share/package-licenses/kiten/4fe1019be678bc440c6c4a703d34fd4dd77bfd56 || :
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
%find_lang kiten
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kiten
/V3/usr/bin/kitenkanjibrowser
/V3/usr/bin/kitenradselect
/usr/bin/kiten
/usr/bin/kitenkanjibrowser
/usr/bin/kitenradselect

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kiten.desktop
/usr/share/applications/org.kde.kitenkanjibrowser.desktop
/usr/share/applications/org.kde.kitenradselect.desktop
/usr/share/config.kcfg/kiten.kcfg
/usr/share/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf
/usr/share/icons/hicolor/128x128/apps/kiten.png
/usr/share/icons/hicolor/16x16/apps/kiten.png
/usr/share/icons/hicolor/22x22/apps/kiten.png
/usr/share/icons/hicolor/32x32/apps/kiten.png
/usr/share/icons/hicolor/48x48/apps/kiten.png
/usr/share/icons/hicolor/64x64/apps/kiten.png
/usr/share/icons/hicolor/scalable/apps/kiten.svgz
/usr/share/kiten/edict
/usr/share/kiten/kanjidic
/usr/share/kiten/radkfile
/usr/share/kiten/romkana.cnv
/usr/share/kiten/vconj
/usr/share/metainfo/org.kde.kiten.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/libkiten/DictEdict/dictfileedict.h
/usr/include/libkiten/DictEdict/entryedict.h
/usr/include/libkiten/DictKanjidic/dictfilekanjidic.h
/usr/include/libkiten/DictKanjidic/entrykanjidic.h
/usr/include/libkiten/dictionarymanager.h
/usr/include/libkiten/dictionarypreferencedialog.h
/usr/include/libkiten/dictquery.h
/usr/include/libkiten/entry.h
/usr/include/libkiten/entrylist.h
/usr/include/libkiten/historyptrlist.h
/usr/lib64/libkiten.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kiten/index.cache.bz2
/usr/share/doc/HTML/ca/kiten/index.docbook
/usr/share/doc/HTML/de/kiten/index.cache.bz2
/usr/share/doc/HTML/de/kiten/index.docbook
/usr/share/doc/HTML/de/kiten/kiten1.png
/usr/share/doc/HTML/de/kiten/kiten2.png
/usr/share/doc/HTML/en/kiten/common_uncommon_filtering.png
/usr/share/doc/HTML/en/kiten/ending_search.png
/usr/share/doc/HTML/en/kiten/font.png
/usr/share/doc/HTML/en/kiten/grade_search.png
/usr/share/doc/HTML/en/kiten/index.cache.bz2
/usr/share/doc/HTML/en/kiten/index.docbook
/usr/share/doc/HTML/en/kiten/introduction.png
/usr/share/doc/HTML/en/kiten/kanji_information.png
/usr/share/doc/HTML/en/kiten/kanji_list.png
/usr/share/doc/HTML/en/kiten/looking_up_words.png
/usr/share/doc/HTML/en/kiten/radical_selector.png
/usr/share/doc/HTML/en/kiten/search_in_results.png
/usr/share/doc/HTML/en/kiten/stroke_search.png
/usr/share/doc/HTML/en/kiten/verb_deinflection.png
/usr/share/doc/HTML/en/kiten/with_filtering.png
/usr/share/doc/HTML/en/kiten/word_type_results.png
/usr/share/doc/HTML/es/kiten/index.cache.bz2
/usr/share/doc/HTML/es/kiten/index.docbook
/usr/share/doc/HTML/et/kiten/index.cache.bz2
/usr/share/doc/HTML/et/kiten/index.docbook
/usr/share/doc/HTML/fr/kiten/index.cache.bz2
/usr/share/doc/HTML/fr/kiten/index.docbook
/usr/share/doc/HTML/it/kiten/index.cache.bz2
/usr/share/doc/HTML/it/kiten/index.docbook
/usr/share/doc/HTML/nl/kiten/index.cache.bz2
/usr/share/doc/HTML/nl/kiten/index.docbook
/usr/share/doc/HTML/pt/kiten/index.cache.bz2
/usr/share/doc/HTML/pt/kiten/index.docbook
/usr/share/doc/HTML/pt_BR/kiten/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kiten/index.docbook
/usr/share/doc/HTML/ru/kiten/index.cache.bz2
/usr/share/doc/HTML/ru/kiten/index.docbook
/usr/share/doc/HTML/sv/kiten/index.cache.bz2
/usr/share/doc/HTML/sv/kiten/index.docbook
/usr/share/doc/HTML/sv/kiten/kiten1.png
/usr/share/doc/HTML/sv/kiten/kiten2.png
/usr/share/doc/HTML/uk/kiten/common_uncommon_filtering.png
/usr/share/doc/HTML/uk/kiten/ending_search.png
/usr/share/doc/HTML/uk/kiten/font.png
/usr/share/doc/HTML/uk/kiten/grade_search.png
/usr/share/doc/HTML/uk/kiten/index.cache.bz2
/usr/share/doc/HTML/uk/kiten/index.docbook
/usr/share/doc/HTML/uk/kiten/introduction.png
/usr/share/doc/HTML/uk/kiten/kanji_information.png
/usr/share/doc/HTML/uk/kiten/kanji_list.png
/usr/share/doc/HTML/uk/kiten/looking_up_words.png
/usr/share/doc/HTML/uk/kiten/radical_selector.png
/usr/share/doc/HTML/uk/kiten/search_in_results.png
/usr/share/doc/HTML/uk/kiten/stroke_search.png
/usr/share/doc/HTML/uk/kiten/verb_deinflection.png
/usr/share/doc/HTML/uk/kiten/with_filtering.png
/usr/share/doc/HTML/uk/kiten/word_type_results.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkiten.so.6.0.0
/usr/lib64/libkiten.so.6
/usr/lib64/libkiten.so.6.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kiten/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kiten/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kiten/4fe1019be678bc440c6c4a703d34fd4dd77bfd56
/usr/share/package-licenses/kiten/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kiten/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kiten/e154343fcf8229d714c82906b31df9822fd08ebf

%files locales -f kiten.lang
%defattr(-,root,root,-)

