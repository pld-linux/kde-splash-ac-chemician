
%define		_splash		ac-chemician

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	0.1
Release:	1
License:	GPL v2
Group:		X11/Amusements
Source0:	%{_splash}-%{version}.tar.bz2
# Source0-md5:	c84da7ef908664e1243fd84da23f4492
Requires:	kdebase-desktop
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"PLD AC chemician" KDE splash screen.

%description -l pl
Ekran startowy KDE "Chemik PLD".

%prep
%setup  -q -n ac-chemician

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

install * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/%{_splash}
