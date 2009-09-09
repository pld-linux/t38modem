#
Summary:	Fax modem to T.38 gateway
Summary(pl.UTF-8):	Bramka faks modem -> T.38
Name:		t38modem
Version:	1.1.0
Release:	0.1
License:	MPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/t38modem/t38modem-1.1.0.tgz
# Source0-md5:	6a9a6a6e45432aefa065c0436db8b3ac
URL:		http://t38modem.sourceforge.net/
BuildRequires:	opal-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t38modem is a gateway between a fax application and IP network. From
fax application view point it's a fax modem pool, from IP network view
point it's a H.323 endpoint with T.38 fax support.

%description -l pl.UTF-8
t38modem to bramka między aplikacją faksową a siecią IP. Z punktu
widzenia aplikacji jest to pula faksmodemów, z punktu widzenia sieci
IP jest to punkt H.323 z obsługą faksów T.38.

%prep
%setup -q

%build
%{__make} %{?debug:debug}%{!?debug:opt} \
	USE_OPAL=1 OPALDIR=/usr/share/opal \
	OPTCCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
