#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Image-Info
Version  : 1.41
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Info-1.41.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/Image-Info-1.41.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libimage-info-perl/libimage-info-perl_1.41-1.debian.tar.xz
Summary  : 'Extract meta information from image files'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
This Perl extension allows you to extract meta information from various
types of image files. The following file formats are supported:

%package dev
Summary: dev components for the perl-Image-Info package.
Group: Development
Provides: perl-Image-Info-devel = %{version}-%{release}

%description dev
dev components for the perl-Image-Info package.


%prep
%setup -q -n Image-Info-1.41
cd ..
%setup -q -T -D -n Image-Info-1.41 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Image-Info-1.41/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1Bundle/Image/Info/Everything.pm
/usr/lib/perl5/vendor_perl/5.28.1Bundle/Image/Info/PNG.pm
/usr/lib/perl5/vendor_perl/5.28.1Bundle/Image/Info/SVG.pm
/usr/lib/perl5/vendor_perl/5.28.1Bundle/Image/Info/XBM.pm
/usr/lib/perl5/vendor_perl/5.28.1Bundle/Image/Info/XPM.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/BMP.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/GIF.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/ICO.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/JPEG.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/PNG.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/PPM.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/SVG.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/SVG/XMLLibXMLReader.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/SVG/XMLSimple.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/TIFF.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/WBMP.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/XBM.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/Info/XPM.pm
/usr/lib/perl5/vendor_perl/5.28.1Image/TIFF.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Bundle::Image::Info::Everything.3
/usr/share/man/man3/Bundle::Image::Info::PNG.3
/usr/share/man/man3/Bundle::Image::Info::SVG.3
/usr/share/man/man3/Bundle::Image::Info::XBM.3
/usr/share/man/man3/Bundle::Image::Info::XPM.3
/usr/share/man/man3/Image::Info.3
/usr/share/man/man3/Image::Info::BMP.3
/usr/share/man/man3/Image::Info::GIF.3
/usr/share/man/man3/Image::Info::ICO.3
/usr/share/man/man3/Image::Info::PPM.3
/usr/share/man/man3/Image::Info::SVG.3
/usr/share/man/man3/Image::Info::TIFF.3
/usr/share/man/man3/Image::Info::WBMP.3
/usr/share/man/man3/Image::Info::XBM.3
/usr/share/man/man3/Image::Info::XPM.3
