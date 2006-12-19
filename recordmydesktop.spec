Summary:	Desktop session recorder
Summary(pl):	Rejestrator pulpitu
Name:		recordmydesktop
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.gz
# Source0-md5:	780dae22c7f02addfc3c666eaf2ef29c
URL:		http://recordmydesktop.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple command line tool that performs the basic tasks of capturing
and encoding desktop session. It produces files using only open
formats like theora for video and vorbis for audio, using the ogg
container.

%description -l pl
Proste narzêdzie linii poleceñ, które wykonuje podstawowe zadanie
zrzucania i kodowania bie¿±cej sesji pulpitu. Wytwarza on pliki
u¿ywaj±c tylko otwartych formatów takich jak theora dla zapisu video i
vorbis dla zapisu audio, wykorzystuj±c kontener ogg.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/recordmydesktop.1*
