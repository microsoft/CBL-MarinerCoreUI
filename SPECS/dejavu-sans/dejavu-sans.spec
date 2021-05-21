%global _fontdir %{_datadir}/fonts
Summary:        Dejavu-Sans TTF Fonts
Name:           dejavu-sans
Version:        2.37
Release:        1%{?dist}
License:        Bistream Vera Font AND Arev Fonts
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Base
URL:            https://dejavu-fonts.github.io/
Source0:        https://sourceforge.net/projects/dejavu/files/dejavu/%{version}/%{name}-ttf-%{version}.zip


BuildRequires:  unzip

%description
The DejaVu fonts are a font family based on the Vera Fonts. Its
purpose is to provide a wider range of characters while maintaining
the original look and feel through the process of collaborative development

%prep
%setup -q -n %{name}-ttf-%{version}

%install
mkdir -p %{buildroot}%{_fontdir}
mv ttf/*.ttf %{buildroot}%{_fontdir}/

%files
%defattr(-,root,root)
%license LICENSE
%{_fontdir}/*.ttf

%changelog
* Fri May 21 2021 Jon Slobodzian <joslobo@microsoft.com> 2.37-1
- Original version for CBL-Mariner.
