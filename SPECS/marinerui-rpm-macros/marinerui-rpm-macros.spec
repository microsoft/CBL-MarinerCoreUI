Summary:        RPM macros required by CBL-MarinerUI package builds
Name:           marinerui-rpm-macros
Version:        1.0.0
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://github.com/microsoft/CBL-MarinerCoreUI
Source0:        macros.marinerui

BuildArch:      noarch

%description
The package contains RPM macros, which are necessary by some CBL-MarinerUI package builds.

%prep
%setup -q -c -T

%build

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_libdir}/rpm/macros.d/macros.marinerui

%files
%{_libdir}/rpm/macros.d/macros.marinerui

%changelog
* Thu Dec 17 2020 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.0.0-1
- Original version for CBL-Mariner.
