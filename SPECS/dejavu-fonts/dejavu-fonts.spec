%global _fontdir %{_datadir}/fonts
%global _mono_fontdir %{_datadir}/fonts/dejavu-sans-mono-fonts
%global _sans_fontdir %{_datadir}/fonts/dejavu-sans-fonts
%global _serif_fontdir %{_datadir}/fonts/dejavu-serif-fonts

Summary:        The DejaVu font families
Name:           dejavu-fonts
Version:        2.37
Release:        2%{?dist}
License:        Bistream Vera Font AND Arev Fonts
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Base
URL:            https://dejavu-fonts.github.io/
Source0:        https://sourceforge.net/projects/dejavu/files/dejavu/%{version}/%{name}-ttf-%{version}.tar.bz2

BuildRequires:  tar

%description
The DejaVu fonts are a font family based on the Vera Fonts. Its
purpose is to provide a wider range of characters while maintaining
the original look and feel through the process of collaborative development

%prep
%setup -q -n %{name}-ttf-%{version}

%install
install -d %{buildroot}%{_fontdir}
install ttf/*.ttf %{buildroot}%{_fontdir}/

%files
%defattr(-,root,root)
%license LICENSE
%{_fontdir}/*.ttf

%changelog
* Fri Jul 09 2021 Pawel Winogrodzki <pawelwi@microsoft.com> 2.37-2
- Renaming to 'dejavu-fonts'.
- Adding 'dejavu-sans-mono-fonts' and 'dejavu-serif-fonts' subpackages.
- Adding font configurations.

* Fri May 21 2021 Jon Slobodzian <joslobo@microsoft.com> 2.37-1
- Original version for CBL-Mariner.
