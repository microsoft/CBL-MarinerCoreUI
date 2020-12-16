Summary:        X.Org X11 X server
Name:           xorg-x11-server
Version:        1.20.10
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2

BuildRequires:  make

%description
X.Org X11 X server

%prep
%autosetup

%build
%configure

%install
%make_install

%files
%license COPYING
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/

%changelog
* Thu Dec 10 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.20.10-1
- Original version for CBL-Mariner.
