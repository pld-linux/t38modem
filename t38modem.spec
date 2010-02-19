#
Summary:	Fax modem to T.38 gateway
Summary(pl.UTF-8):	Bramka faks modem -> T.38
Name:		t38modem
Version:	1.2.0
Release:	1
License:	MPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tgz
# Source0-md5:	9239576bac0b57a3c8d90671b0249247
Patch0:		opal_flags_support.patch
URL:		http://t38modem.sourceforge.net/
BuildRequires:	opal-devel >= 3.6.6-3
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
%patch0 -p1

%build
%{__make} %{?debug:debug}%{!?debug:opt} \
	USE_OPAL=1 USE_UNIX98_PTY=1 OPALDIR=/usr/include/opal \
	PTLIBDIR=/usr/share/ptlib OPTCCFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe.txt
%attr(755,root,root) %{_bindir}/*
