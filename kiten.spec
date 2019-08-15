#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kiten
Version  : 19.08.0
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.0/src/kiten-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/kiten-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/kiten-19.08.0.tar.xz.sig
Summary  : Japanese Reference/Study Tool
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kiten-bin = %{version}-%{release}
Requires: kiten-data = %{version}-%{release}
Requires: kiten-lib = %{version}-%{release}
Requires: kiten-license = %{version}-%{release}
Requires: kiten-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : khtml-dev
BuildRequires : kjs-dev
BuildRequires : qtbase-dev mesa-dev

%description
****************************************
**                Kiten                 **
**      a Japanese reference tool       **
****************************************

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
%setup -q -n kiten-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565901525
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565901525
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kiten
cp COPYING %{buildroot}/usr/share/package-licenses/kiten/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kiten/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kiten/COPYING.LIB
cp data/font/copyright.txt %{buildroot}/usr/share/package-licenses/kiten/data_font_copyright.txt
pushd clr-build
%make_install
popd
%find_lang kiten

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kiten
/usr/bin/kitengen
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
/usr/share/kxmlgui5/kiten/kitenui.rc
/usr/share/kxmlgui5/kitenkanjibrowser/kanjibrowserui.rc
/usr/share/kxmlgui5/kitenradselect/radselectui.rc
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
/usr/include/libkiten/kromajiedit.h
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
/usr/share/doc/HTML/it/kiten/index.cache.bz2
/usr/share/doc/HTML/it/kiten/index.docbook
/usr/share/doc/HTML/nl/kiten/index.cache.bz2
/usr/share/doc/HTML/nl/kiten/index.docbook
/usr/share/doc/HTML/pt/kiten/index.cache.bz2
/usr/share/doc/HTML/pt/kiten/index.docbook
/usr/share/doc/HTML/pt_BR/kiten/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kiten/index.docbook
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
/usr/lib64/libkiten.so.5
/usr/lib64/libkiten.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kiten/COPYING
/usr/share/package-licenses/kiten/COPYING.DOC
/usr/share/package-licenses/kiten/COPYING.LIB
/usr/share/package-licenses/kiten/data_font_copyright.txt

%files locales -f kiten.lang
%defattr(-,root,root,-)

