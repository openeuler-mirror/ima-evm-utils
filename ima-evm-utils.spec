Name:         ima-evm-utils
Version:      1.3.1
Release:      4
Summary:      IMA/EVM control utilities
Group:        System/Libraries
License:      GPLv2
URL:          http://linux-ima.sourceforge.net/
Source0:      http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%{name}-%{version}.tar.gz

BuildRequires: autoconf automake libtool m4 asciidoc libxslt openssl-devel
BuildRequires: keyutils-libs-devel git
Requires:     %{name}-libs = %{version}-%{release}

%description
ima-evm-utils package provides the evmctl utility that can be used for producing
and verifying digital signatures, which are used by Linux kernel integrity subsystem.
It can be also used to import keys into the kernel keyring.

%package libs
Summary: shared library for IMA/EVM

%description libs
This package provides shared library for IMA/EVM.

%package devel
Requires: %{name}-libs = %{version}-%{release}
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

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README NEWS
%license COPYING AUTHORS
%{_bindir}/*

%files libs
%defattr(-,root,root)
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
* Wed Dec 1 2021 openEuler Buildteam <buildteam@openeuler.org> - 1.3.1-4
- remove libimaevm.so.1

* Mon Sep 21 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.3.1-3
- provide both libimaevm.so.1 and libimaevm.so.2

* Thu Sep 17 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.3.1-2
- provide libimaevm.so.1

* Wed Aug 19 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.3.1-1
- update to 1.3.1

* Mon Jan 20 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-8
- add %{name}-libs

* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-7
- delete libimaevm0

* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-6
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: clean code

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: clean code

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: clean code

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-3
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: clean code

* Mon Jan 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: clean code

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
