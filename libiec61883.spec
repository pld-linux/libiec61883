Summary:	Streaming library for IEEE1394
Summary(pl.UTF-8):	Biblioteka strumieni dla IEEE1394
Name:		libiec61883
Version:	1.1.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.linux1394.org/dl/%{name}-%{version}.tar.gz
# Source0-md5:	08f46840912ae2032499186228842a32
URL:		http://www.linux1394.org/
BuildRequires:	libraw1394-devel >= 1.2.1
BuildRequires:	pkgconfig
Requires:	libraw1394 >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is an implementation of IEC 61883, part 1 (CIP, plug
registers, and CMP), part 2 (DV-SD), part 4 (MPEG2-TS), and part 6
(AMDTP). Outside of IIDC, nearly all FireWire multimedia devices use
IEC 61883 protocols.

The libiec61883 library provides a higher level API for streaming DV,
MPEG-2 and audio over Linux IEEE 1394. This includes both reception
and transmission. It uses the new "rawiso" API of libraw1394, which
transparently provides mmap-ed DMA for efficient data transfer. It
also represents the third generation of I/O technology for Linux 1394
for these media types thereby removing the complexities of additional
kernel modules, /dev nodes, and procfs. It also consolidates features
for plug control registers and connection management that previously
existed in experimental form in an unreleased version of libavc1394.

%description -l pl.UTF-8
Ta biblioteka jest implementacją części 1 (CIP, rejestry łącz, CMP),
części 2 (DV-SD), części 4 (MPEG2-TS) oraz części 6 (AMDTP) standardu
IEC 61883. Poza IIDC prawie wszystkie urządzenia multimedialne
FireWire używają protokołów IEC 61883.

Biblioteka libiec61883 udostępnia wysokopoziomowe API do przekazywania
strumieni DV, MPEG-2 i dźwięku po linuksowym IEEE 1394. Obejmuje to
zarówno przyjmowanie jak i przesyłanie. Używa nowego API "rawiso" z
libraw1394, które w sposób przezroczysty udostępnia mmapowane DMA do
wydajnego przesyłania danych. Biblioteka reprezentuje także trzecią
generację technologii wejścia/wyjścia dla projektu Linux 1394 dla tych
rodzajów nośników usuwając złożoność dodatkowych modułów jądra, węzłów
/dev oraz procfs. Łączy możliwości rejestrów sterowania łączami i
zarządzania połączeniami, które wcześniej istniały w postaci
eksperymentalnej w niewydanej wersji libavc1394.

%package devel
Summary:	libiec61883 header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libiec61883
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraw1394-devel >= 1.2.1

%description devel
libiec61883 devel package.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libiec61883.

%package static
Summary:	libiec61883 static library
Summary(pl.UTF-8):	Statyczna biblioteka do obsługi formatu IEEE-1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libiec61883 static librawy.

%description static -l pl.UTF-8
Statyczna biblioteka libiec61883.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/plug*
%attr(755,root,root) %{_libdir}/libiec61883.so.*.*
%{_mandir}/man1/plug*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiec61883.so
%{_libdir}/libiec61883.la
%{_includedir}/libiec61883
%{_pkgconfigdir}/libiec61883.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libiec61883.a
