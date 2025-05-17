#
# Conditional build:
%bcond_with	mmx	# MMX acceleration (obligatory, no runtime detection)
#
%ifarch %{x8664} pentium2 pentium3 pentium4 athlon
%define	with_mmx	1
%endif
Summary:	Video codec library
Summary(pl.UTF-8):	Biblioteka kodeka obrazu
Name:		capseo
Version:	0.3.0
Release:	4
License:	GPL v2
Group:		Libraries
Source0:	http://archive.debian.org/debian/pool/main/c/capseo/%{name}_%{version}~svn158.orig.tar.gz
# Source0-md5:	46660f02f7d5b8fcf7c9b5cc89eca6fe
# dead (2025.05)
#URL:		http://rm-rf.in/capseo
BuildRequires:	OpenGL-devel
BuildRequires:	libogg-devel >= 1:1.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
BuildRequires:	pkgconfig >= 1:0.17.2
%if %{with mmx}
BuildRequires:	yasm
%endif
Requires:	libogg >= 1:1.1
%{?with_mmx:Requires:	cpuinfo(mmx)}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
capseo is a realtime video encoder/decoder library. The capseo codec
is meant to encode fast, not to generate the smallest files on your
file system.

%description -l pl.UTF-8
capseo to biblioteka kodera/dekodera obrazu czasu rzeczywistego. Kodek
ma za zadanie szybko kodować, niekoniecznie generując najmniejsze
pliki.

%package devel
Summary:	Header files for capseo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki capseo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libogg-devel >= 1:1.1
Requires:	libstdc++-devel

%description devel
Header files for capseo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki capseo.

%package static
Summary:	Static capseo library
Summary(pl.UTF-8):	Biblioteka statyczna capseo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static capseo library.

%description static -l pl.UTF-8
Biblioteka statyczna capseo.

%prep
%setup -q -n %{name}-%{version}~svn158.orig

%build
%configure \
	--enable-theora \
%if %{with mmx}
%ifarch %{ix86}
	--with-accel=x86 \
%endif
%ifarch %{x8664}
	--with-accel=amd64
%endif
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcapseo.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/cpsinfo
%attr(755,root,root) %{_bindir}/cpsplay
%attr(755,root,root) %{_bindir}/cpsrecode
%attr(755,root,root) %{_libdir}/libcapseo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcapseo.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcapseo.so
%{_includedir}/capseo.h
%{_pkgconfigdir}/capseo.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcapseo.a
