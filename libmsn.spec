
%define		_beta	beta1

Summary:	MSN Library
Summary(pl.UTF-8):	Biblioteka MSN
Name:		libmsn
Version:	4.0
Release:	0.%{_beta}.1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	f5b79c230ec7e7654b5efe8c61ea1602
Patch0:		%{name}-lib64.patch
URL:		http://sourceforge.net/projects/libmsn/
BuildRequires:	cmake
Requires(pre,post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MSN Library.

%description -l pl.UTF-8
Biblioteka MSN.

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
%setup -q -n %{name}-%{version}-%{_beta}
%patch0 -p0

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
%attr(755,root,root) %ghost %{_libdir}/libmsn.so.0.1
%attr(755,root,root) %{_libdir}/libmsn.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsn.so
%{_includedir}/msn
