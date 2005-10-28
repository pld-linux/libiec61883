Summary:	Streaming library for IEEE1394
Summary(pl):	Biblioteka strumieni dla IEEE1394
Name:		libiec61883
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libraw1394/%{name}-%{version}.tar.gz
# Source0-md5:	7f531c1599bfe8f385a2cb4e56e9d93b
URL:		http://www.linux1394.org/
BuildRequires:	libraw1394-devel >= 1.2.0
Requires:	libraw1394 >= 1.2.0
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

%description -l pl
Ta biblioteka jest implementacj± czê¶ci 1 (CIP, rejestry ³±cz, CMP),
czê¶ci 2 (DV-SD), czê¶ci 4 (MPEG2-TS) oraz czê¶ci 6 (AMDTP) standardu
IEC 61883. Poza IIDC prawie wszystkie urz±dzenia multimedialne
FireWire u¿ywaj± protoko³ów IEC 61883.

Biblioteka libiec61883 udostêpnia wysokopoziomowe API do przekazywania
strumieni DV, MPEG-2 i d¼wiêku po linuksowym IEEE 1394. Obejmuje to
zarówno przyjmowanie jak i przesy³anie. U¿ywa nowego API "rawiso" z
libraw1394, które w sposób przezroczysty udostêpnia mmapowane DMA do
wydajnego przesy³ania danych. Biblioteka reprezentuje tak¿e trzeci±
generacjê technologii wej¶cia/wyj¶cia dla projektu Linux 1394 dla tych
rodzajów no¶ników usuwaj±c z³o¿ono¶æ dodatkowych modu³ów j±dra, wêz³ów
/dev oraz procfs. £±czy mo¿liwo¶ci rejestrów sterowania ³±czami i
zarz±dzania po³±czeniami, które wcze¶niej istnia³y w postaci
eksperymentalnej w niewydanej wersji libavc1394.

%package devel
Summary:	libiec61883 header files
Summary(pl):	Pliki nag³ówkowe biblioteki libiec61883
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraw1394-devel >= 1.2.0

%description devel
libiec61883 devel package.

%description devel -l pl
Pliki nag³ówkowe biblioteki libiec61883.

%package static
Summary:	libiec61883 static library
Summary(pl):	Statyczna biblioteka do obs³ugi formatu IEEE-1394
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libiec61883 static librawy.

%description static -l pl
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libiec61883.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiec61883.so
%{_libdir}/libiec61883.la
%{_includedir}/libiec61883
%{_pkgconfigdir}/libiec61883.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libiec61883.a
