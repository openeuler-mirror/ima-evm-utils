Name:         ima-evm-utils
Version:      1.3.2
Release:      2
Summary:      IMA/EVM control utilities
License:      GPLv2
URL:          http://linux-ima.sourceforge.net/
Source0:      http://sourceforge.net/projects/linux-ima/files/ima-evm-utils/%{name}-%{version}.tar.gz

Patch9000:    add-save-command-to-support-digest-list-building.patch

BuildRequires: autoconf automake libtool asciidoc vim-common
BuildRequires: libxslt openssl-devel keyutils-libs-devel tpm2-tss-devel
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
Summary: Development files for %{name}
Requires: %{name}-libs = %{version}-%{release}
Provides: %{name}-static = %{version}-%{release}
Obsoletes:%{name}-static < %{version}-%{release}

%description devel
This package provides the header files for %{name}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -f -i
%configure \
  --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc NEWS README AUTHORS
%license COPYING
%{_bindir}/*

%files libs
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%{_docdir}/%{name}/*.sh
%{_includedir}/*.h
%{_libdir}/*.so

%files help
%doc %{_mandir}/*/*

%changelog
* Tue Feb 2 2021 openEuler Buildteam <buildteam@openeuler.org> - 1.3.2-2
- fix make check fail issue

* Fri Jan 15 2021 openEuler Buildteam <buildteam@openeuler.org> - 1.3.2-1
- update to 1.3.2

* Fri Jul 3 2020 Anakin Zhang <benjamin93@163.com> - 1.2.1-9
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: add save command and support IMA digest list

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
