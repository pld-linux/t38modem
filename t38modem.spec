Summary:	Fax modem to T.38 gateway
Summary(pl):	Bramka faks modem -> T.38
Name:		t38modem
Version:	0.6.2
Release:	1
License:	MPL
Group:		Networking/Daemons
Source0:	http://www.openh323.org/bin/%{name}_%{version}.tar.gz
# Source0-md5:	8b49e1d7f97ec0b6f2bfb7482f99d1ba
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.11.3
BuildRequires:	pwlib-devel >= 1.4.8
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t38modem is a gateway between a fax application and IP network. From
fax application view point it's a fax modem pool, from IP network view
point it's a H.323 endpoint with T.38 fax support.

%description -l pl
t38modem to bramka miêdzy aplikacj± faksow± a sieci± IP. Z punktu
widzenia aplikacji jest to pula faksmodemów, z punktu widzenia sieci
IP jest to punkt H.323 z obs³ug± faksów T.38.

%prep
%setup -qn %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} %{?debug:debug}%{!?debug:opt}shared \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"

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
