Summary:        Multitouch Protocol Translation Library
Name:           mtdev
Version:        1.1.5
Release:        19%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://bitmath.org/code/mtdev/
Source0:        https://bitmath.org/code/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool

%description
%{name} is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking.

%package devel
Summary:        Multitouch Protocol Translation Library Development Package

Requires:       %{name} = %{version}-%{release}
Requires:       pkg-config

Provides:       pkgconfig(mtdev)

%description devel
Multitouch protocol translation library development package.

%prep
%setup -q

%build
autoreconf --force -v --install || exit 1
%configure --disable-static
%make_build

%install
%make_install

# We intentionally don't ship *.la files
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_libdir}/libmtdev.so.*

%files devel
%{_includedir}/mtdev.h
%{_includedir}/mtdev-plumbing.h
%{_includedir}/mtdev-mapping.h
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc
%{_bindir}/mtdev-test

%changelog
* Wed Dec 16 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.1.5-19
- Initial CBL-Mariner import from Fedora 33 (license: MIT).
- License verified

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.1.5-17
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Peter Hutterer <peter.hutterer@redhat.com> 1.1.5-12
- Add gcc to BR

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.5-11
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Peter Hutterer <peter.hutterer@redhat.com>
- remove unnecessary defattr

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Dan Horák <dan[at]danny.cz> 1.1.5-2
- drop ExcludeArch, mtdev becomes the required part of the desktop stack

* Mon Mar 24 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.1.5-1
- mtdev 1.1.5

* Mon Aug 12 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.1.4-1
- mtdev 1.1.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-3
- Less RHEL customization

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.3-1
- mtdev 1.1.3

* Thu Sep 27 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-4
- fix %%{?dist}

* Mon Aug 13 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-3
- Drop xorg-x11-util-macros build requires, not needed anymore
- Don't build on s390 (or ppc, if on RHEL)
- Force autoreconf to avoid libtool errors

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.1.2-1
- mtdev 1.1.2
- upstream provides tarballs now, add the needed spec file changes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3.20110105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2.20110105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.1.0-1.20110105
- Update to release 1.1.0

* Tue Aug 03 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.8-1.20100803
- Update to release 1.0.8

* Thu Jul 08 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.1-2.20100706
- Require util-macros >= 1.5

* Tue Jul 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.0.1-1.20100706
- Initial package
