Summary:	MSN Library
Summary(pl.UTF-8):	Biblioteka MSN
Name:		libmsn
Version:	4.2.1
Release:	6
License:	GPL
Group:		Libraries
Source0:	http://download.sourceforge.net/libmsn/%{name}-%{version}.tar.bz2
# Source0-md5:	38e46e589720eefd71f92b6b76993bf0
Patch0:		c++.patch
Patch1:		openssl.patch
URL:		http://sourceforge.net/projects/libmsn/
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
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

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/msntest
%attr(755,root,root) %ghost %{_libdir}/libmsn.so.0.3
%attr(755,root,root) %{_libdir}/libmsn.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsn.so
%{_pkgconfigdir}/libmsn.pc
%{_includedir}/msn
