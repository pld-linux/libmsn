Summary:	MSN Library
Summary(pl.UTF-8):	Biblioteka MSN
Name:		libmsn
Version:	4.2.1
Release:	7
License:	GPL v2+
Group:		Libraries
Source0:	http://download.sourceforge.net/libmsn/%{name}-%{version}.tar.bz2
# Source0-md5:	38e46e589720eefd71f92b6b76993bf0
Patch0:		c++.patch
Patch1:		openssl.patch
Patch2:		%{name}-throw.patch
URL:		https://sourceforge.net/projects/libmsn/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmsn is a reusable, open-source, fully documented library for
connecting to Microsoft's MSN Messenger service.

%description -l pl.UTF-8
libmsn to mająca otwarte źródła, w pełni udokumentowana biblioteka do
łączenia się z usługą MSN Messenger Microsoftu.

%package devel
Summary:	Header files for MSN library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki MSN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MSN library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki MSN.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/msntest
%attr(755,root,root) %{_libdir}/libmsn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmsn.so.0.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsn.so
%{_pkgconfigdir}/libmsn.pc
%{_includedir}/msn
