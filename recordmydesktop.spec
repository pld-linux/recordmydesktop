Summary:	Desktop session recorder
Summary(pl):	Rejestrator pulpitu
Name:		recordmydesktop
Version:	0.3.1
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.gz
# Source0-md5:	780dae22c7f02addfc3c666eaf2ef29c
URL:		http://recordmydesktop.sourceforge.net/
#BuildRequires:	-
# alsa (libasound)
#X
#libICE-dev
#libSM-dev
#libXext
#libXdamage
#libXfixes
#libogg
#libvorbis
#libtheora
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple command line tool that performs the basic tasks of capturing
and encoding and an interface that exposes the program functionality
in a usable way.

%prep
%setup -q

%build
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
