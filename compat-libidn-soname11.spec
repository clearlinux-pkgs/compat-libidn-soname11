#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x860B7FBB32F8119D (simon@yubico.com)
#
Name     : compat-libidn-soname11
Version  : 1.33
Release  : 3
URL      : http://mirrors.kernel.org/gnu/libidn/libidn-1.33.tar.gz
Source0  : http://mirrors.kernel.org/gnu/libidn/libidn-1.33.tar.gz
Source99 : http://mirrors.kernel.org/gnu/libidn/libidn-1.33.tar.gz.sig
Summary  : IETF stringprep, nameprep, punycode, IDNA text processing.
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: compat-libidn-soname11-bin
Requires: compat-libidn-soname11-lib
Requires: compat-libidn-soname11-license
Requires: compat-libidn-soname11-data
Requires: compat-libidn-soname11-man
BuildRequires : docbook-xml
BuildRequires : emacs
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : valgrind

%description
See the end for copying conditions.
Libidn is a package for internationalized string handling based on the
Stringprep, Punycode, IDNA and TLD specifications.  Libidn is a GNU
project.  See the file COPYING for licensing information.

%package bin
Summary: bin components for the compat-libidn-soname11 package.
Group: Binaries
Requires: compat-libidn-soname11-data = %{version}-%{release}
Requires: compat-libidn-soname11-license = %{version}-%{release}
Requires: compat-libidn-soname11-man = %{version}-%{release}

%description bin
bin components for the compat-libidn-soname11 package.


%package data
Summary: data components for the compat-libidn-soname11 package.
Group: Data

%description data
data components for the compat-libidn-soname11 package.


%package dev
Summary: dev components for the compat-libidn-soname11 package.
Group: Development
Requires: compat-libidn-soname11-lib = %{version}-%{release}
Requires: compat-libidn-soname11-bin = %{version}-%{release}
Requires: compat-libidn-soname11-data = %{version}-%{release}
Provides: compat-libidn-soname11-devel = %{version}-%{release}

%description dev
dev components for the compat-libidn-soname11 package.


%package dev32
Summary: dev32 components for the compat-libidn-soname11 package.
Group: Default
Requires: compat-libidn-soname11-lib32 = %{version}-%{release}
Requires: compat-libidn-soname11-bin = %{version}-%{release}
Requires: compat-libidn-soname11-data = %{version}-%{release}
Requires: compat-libidn-soname11-dev = %{version}-%{release}

%description dev32
dev32 components for the compat-libidn-soname11 package.


%package doc
Summary: doc components for the compat-libidn-soname11 package.
Group: Documentation
Requires: compat-libidn-soname11-man = %{version}-%{release}

%description doc
doc components for the compat-libidn-soname11 package.


%package lib
Summary: lib components for the compat-libidn-soname11 package.
Group: Libraries
Requires: compat-libidn-soname11-data = %{version}-%{release}
Requires: compat-libidn-soname11-license = %{version}-%{release}

%description lib
lib components for the compat-libidn-soname11 package.


%package lib32
Summary: lib32 components for the compat-libidn-soname11 package.
Group: Default
Requires: compat-libidn-soname11-data = %{version}-%{release}
Requires: compat-libidn-soname11-license = %{version}-%{release}

%description lib32
lib32 components for the compat-libidn-soname11 package.


%package license
Summary: license components for the compat-libidn-soname11 package.
Group: Default

%description license
license components for the compat-libidn-soname11 package.


%package man
Summary: man components for the compat-libidn-soname11 package.
Group: Default

%description man
man components for the compat-libidn-soname11 package.


%prep
%setup -q -n libidn-1.33
pushd ..
cp -a libidn-1.33 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537329616
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1537329616
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/compat-libidn-soname11
cp COPYING %{buildroot}/usr/share/doc/compat-libidn-soname11/COPYING
cp COPYING.LESSERv2 %{buildroot}/usr/share/doc/compat-libidn-soname11/COPYING.LESSERv2
cp COPYING.LESSERv3 %{buildroot}/usr/share/doc/compat-libidn-soname11/COPYING.LESSERv3
cp COPYINGv2 %{buildroot}/usr/share/doc/compat-libidn-soname11/COPYINGv2
cp COPYINGv3 %{buildroot}/usr/share/doc/compat-libidn-soname11/COPYINGv3
cp doc/specifications/COPYING.UCD %{buildroot}/usr/share/doc/compat-libidn-soname11/doc_specifications_COPYING.UCD
cp java/LICENSE-2.0.txt %{buildroot}/usr/share/doc/compat-libidn-soname11/java_LICENSE-2.0.txt
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## install_append content
rm -rf %{buildroot}/usr/share/locale
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/idn

%files data
%defattr(-,root,root,-)
%exclude /usr/share/emacs/site-lisp/idna.el
%exclude /usr/share/emacs/site-lisp/punycode.el

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/idn-free.h
%exclude /usr/include/idn-int.h
%exclude /usr/include/idna.h
%exclude /usr/include/pr29.h
%exclude /usr/include/punycode.h
%exclude /usr/include/stringprep.h
%exclude /usr/include/tld.h
%exclude /usr/lib64/libidn.so
%exclude /usr/lib64/pkgconfig/libidn.pc
%exclude /usr/share/man/man3/idn_free.3
%exclude /usr/share/man/man3/idna_strerror.3
%exclude /usr/share/man/man3/idna_to_ascii_4i.3
%exclude /usr/share/man/man3/idna_to_ascii_4z.3
%exclude /usr/share/man/man3/idna_to_ascii_8z.3
%exclude /usr/share/man/man3/idna_to_ascii_lz.3
%exclude /usr/share/man/man3/idna_to_unicode_44i.3
%exclude /usr/share/man/man3/idna_to_unicode_4z4z.3
%exclude /usr/share/man/man3/idna_to_unicode_8z4z.3
%exclude /usr/share/man/man3/idna_to_unicode_8z8z.3
%exclude /usr/share/man/man3/idna_to_unicode_8zlz.3
%exclude /usr/share/man/man3/idna_to_unicode_lzlz.3
%exclude /usr/share/man/man3/pr29_4.3
%exclude /usr/share/man/man3/pr29_4z.3
%exclude /usr/share/man/man3/pr29_8z.3
%exclude /usr/share/man/man3/pr29_strerror.3
%exclude /usr/share/man/man3/punycode_decode.3
%exclude /usr/share/man/man3/punycode_encode.3
%exclude /usr/share/man/man3/punycode_strerror.3
%exclude /usr/share/man/man3/stringprep.3
%exclude /usr/share/man/man3/stringprep_4i.3
%exclude /usr/share/man/man3/stringprep_4zi.3
%exclude /usr/share/man/man3/stringprep_check_version.3
%exclude /usr/share/man/man3/stringprep_convert.3
%exclude /usr/share/man/man3/stringprep_locale_charset.3
%exclude /usr/share/man/man3/stringprep_locale_to_utf8.3
%exclude /usr/share/man/man3/stringprep_profile.3
%exclude /usr/share/man/man3/stringprep_strerror.3
%exclude /usr/share/man/man3/stringprep_ucs4_nfkc_normalize.3
%exclude /usr/share/man/man3/stringprep_ucs4_to_utf8.3
%exclude /usr/share/man/man3/stringprep_unichar_to_utf8.3
%exclude /usr/share/man/man3/stringprep_utf8_nfkc_normalize.3
%exclude /usr/share/man/man3/stringprep_utf8_to_locale.3
%exclude /usr/share/man/man3/stringprep_utf8_to_ucs4.3
%exclude /usr/share/man/man3/stringprep_utf8_to_unichar.3
%exclude /usr/share/man/man3/tld_check_4.3
%exclude /usr/share/man/man3/tld_check_4t.3
%exclude /usr/share/man/man3/tld_check_4tz.3
%exclude /usr/share/man/man3/tld_check_4z.3
%exclude /usr/share/man/man3/tld_check_8z.3
%exclude /usr/share/man/man3/tld_check_lz.3
%exclude /usr/share/man/man3/tld_default_table.3
%exclude /usr/share/man/man3/tld_get_4.3
%exclude /usr/share/man/man3/tld_get_4z.3
%exclude /usr/share/man/man3/tld_get_table.3
%exclude /usr/share/man/man3/tld_get_z.3
%exclude /usr/share/man/man3/tld_strerror.3

%files dev32
%defattr(-,root,root,-)
%exclude /usr/lib32/libidn.so
%exclude /usr/lib32/pkgconfig/32libidn.pc
%exclude /usr/lib32/pkgconfig/libidn.pc

%files doc
%defattr(0644,root,root,0755)
%exclude /usr/share/info/libidn-components.png
%exclude /usr/share/info/libidn.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libidn.so.11
/usr/lib64/libidn.so.11.6.16

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libidn.so.11
/usr/lib32/libidn.so.11.6.16

%files license
%defattr(-,root,root,-)
%exclude /usr/share/doc/compat-libidn-soname11/COPYING
%exclude /usr/share/doc/compat-libidn-soname11/COPYING.LESSERv2
%exclude /usr/share/doc/compat-libidn-soname11/COPYING.LESSERv3
%exclude /usr/share/doc/compat-libidn-soname11/COPYINGv2
%exclude /usr/share/doc/compat-libidn-soname11/COPYINGv3
%exclude /usr/share/doc/compat-libidn-soname11/doc_specifications_COPYING.UCD
%exclude /usr/share/doc/compat-libidn-soname11/java_LICENSE-2.0.txt

%files man
%defattr(-,root,root,-)
%exclude /usr/share/man/man1/idn.1
