Summary:	video codec library
Name:		capseo
Version:	0.3.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.de.debian.org/debian/pool/main/c/capseo/%{name}_%{version}~svn158.orig.tar.gz
# Source0-md5:	46660f02f7d5b8fcf7c9b5cc89eca6fe
URL:		http://rm-rf.in/capseo
BuildRequires:	libtheora-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
capseo is a realtime video encoder/decoder library. The capseo codec
is meant to encode fast, not to generate the smallest files on your
file system.

%package devel
Summary:	Header files and develpment documentation for capseo
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do capseo
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for capseo.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do capseo.

%package static
Summary:	Static capseo library
Summary(pl.UTF-8):	Biblioteka statyczna capseo
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static capseo library.

%prep
%setup -q -n %{name}-%{version}~svn158.orig

%build
%configure \
	--enable-theora
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
