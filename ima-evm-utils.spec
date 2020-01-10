Name:         ima-evm-utils
Version:      1.2.1
Release:      1
Summary:      IMA/EVM control utilities
License:      GPLv2
URL:          http://linux-ima.sourceforge.net/
Source0:      http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool m4 asciidoc libxslt openssl-devel keyutils-libs-devel git

%description
ima-evm-utils package provides the evmctl utility that can be used for producing
and verifying digital signatures, which are used by Linux kernel integrity subsystem.
It can be also used to import keys into the kernel keyring.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{version}-%{release}
Obsoletes:%{name}-static < %{version}-%{release}

%description devel
This package provides the header files for %{name}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1 -Sgit

%build
mkdir -p m4
autoreconf -f -i
%configure 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%check
make check

%pre

%preun

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog README
%license COPYING AUTHORS
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_docdir}/%{name}/*.sh
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/libimaevm.a
%{_libdir}/libimaevm.la

%files help
%doc %{_mandir}/*/*

%changelog
* Fri Jan 10 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: clean code

* Wed Oct 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1-7
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: change the directory of AUTHORS

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1-6
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: revise spec file with new rules

* Mon Aug 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1-5
- Package init
