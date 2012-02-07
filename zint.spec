Summary:	Barcode generator
Summary(pl.UTF-8):	Generator kodów kreskowych
Name:		zint
Version:	2.4.3
Release:	3
License:	GPL v3+
Group:		Applications
Source0:	http://downloads.sourceforge.net/zint/%{name}-%{version}.tar.gz
# Source0-md5:	2b47caff88cb746f212d6a0497185358
BuildRequires:	QtCore-devel
BuildRequires:	QtUiTools-devel
BuildRequires:	cmake >= 2.6.0
BuildRequires:	libpng-devel
BuildRequires:	qt4-build
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zint is a C library for encoding data in several barcode variants. The
bundled command-line utility provides a simple interface to the
library. Features of the library:
- Over 50 symbologies including all ISO/IEC standards, like QR codes.
- Unicode translation for symbologies which support Latin-1 and Kanji
  character sets.
- Full GS1 support including data verification and automated insertion
  of FNC1 characters.
- Support for encoding binary data including NULL (ASCII 0)
  characters.
- Health Industry Barcode (HIBC) encoding capabilities.
- Output in PNG, EPS and SVG formats with user adjustable sizes and
  colors.
- Verification stage for SBN, ISBN and ISBN-13 data.

%package devel
Summary:	Header files for zint library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zint
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zint library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zint.

%package qt
Summary:	Zint Barcode Studio
Summary(pl.UTF-8):	Zint Barcode Studio
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description qt
Zint Barcode Studio is a Qt-based GUI which allows desktop users to
generate barcodes which can then be embedded in documents or HTML
pages.

%description qt -l pl.UTF-8
Zint Barcode Studio jest aplikacją z interfejsem Qt, która umożliwia
użytkownikom komputerów generować kody kreskowe. Mogą one później
zostać włączone do dokumentów lub stron HTML.

%package qt-devel
Summary:	Header files for QZint library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QZint
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description qt-devel
Header files for QZint library.

%description qt-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki QZint.

%prep
%setup -q

find -type f -exec chmod 644 {} \;

%build
%cmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install zint.png $RPM_BUILD_ROOT%{_pixmapsdir}
install zint-qt.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%post qt -p /sbin/ldconfig
%postun	qt -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme
%attr(755,root,root) %{_bindir}/zint
%attr(755,root,root) %{_libdir}/libzint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libzint.so.2.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libzint.so
%{_includedir}/zint.h
%{_datadir}/cmake/Modules/FindZint.cmake

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zint-qt
%attr(755,root,root) %{_libdir}/libQZint.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQZint.so.2.4
%{_pixmapsdir}/zint.png
%{_desktopdir}/zint-qt.desktop

%files qt-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQZint.so
%{_includedir}/qzint.h
