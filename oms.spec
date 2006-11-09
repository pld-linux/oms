Summary:	OMS - Open Media System, a multimedia framework
Summary(pl):	¦rodowisko multimedialne Open Media System
Name:		oms
Version:	0.1.2
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.linuxvideo.org/oms/data/%{name}-%{version}.tar.gz
# Source0-md5:	8eb5d1004dc4918085c335683a82c583
Patch0:		%{name}-opt.patch
Patch1:		%{name}-types.patch
URL:		http://www.linuxvideo.org/oms/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
OMS - Open Media System, a multimedia framework.

%description -l pl
¦rodowisko multimedialne Open Media System (OMS)

%package devel
Summary:	Development libraries and headers of OMS
Summary(pl):	Pliki nag³ówkowe do OMS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development libraries and headers of OMS.

%description devel -l pl
Pliki nag³ówkowe do OMS.

%package static
Summary:	Static libraries of OMS
Summary(pl):	Statyczne biblioteki OMS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries of OMS.

%description static -l pl
Statyczne biblioteki OMS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -I%{_includedir}"
%configure \
	--enable-static \
	--enable-shared

%{__make} m4datadir=%{_aclocaldir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/b*
%attr(755,root,root) %{_bindir}/c*
%attr(755,root,root) %{_bindir}/d*
%attr(755,root,root) %{_bindir}/n*
%attr(755,root,root) %{_bindir}/oms_*
%attr(755,root,root) %{_bindir}/p*
%attr(755,root,root) %{_bindir}/t*
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_libdir}/oms
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oms-config
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_aclocaldir}/*.m4
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
