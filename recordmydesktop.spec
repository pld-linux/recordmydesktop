#
# Conditional build
%bcond_without	gtk	# don't build GTK+ frontend
%bcond_without  x	# don't build for X Window System frontends
%define		module	recordMyDesktop
#
Summary:	Desktop session recorder
Summary(pl.UTF-8):	Rejestrator pulpitu
Name:		recordmydesktop
Version:	0.3.4
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.gz
# Source0-md5:	56163494390dd208213c1563043eb3ee
Source1:	http://dl.sourceforge.net/recordmydesktop/gtk-%{name}-%{version}.tar.gz
# Source1-md5:	5d160b4a907848c77f5649e04886547f
URL:		http://recordmydesktop.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
%if %{with gtk}
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
%endif
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple command line tool that performs the basic tasks of capturing
and encoding desktop session. It produces files using only open
formats like Theora for video and Vorbis for audio, using the Ogg
container.

%description -l pl.UTF-8
Proste narzędzie linii poleceń, które wykonuje podstawowe zadanie
zrzucania i kodowania bieżącej sesji pulpitu. Wytwarza on pliki
używając tylko otwartych formatów takich jak Theora do zapisu obrazu i
Vorbis do zapisu dźwięku, wykorzystując kontener Ogg.

%package gtk
Summary:	GTK+ frontend for recordmydesktop
Summary(pl.UTF-8):	Frontend do recordmydesktop oparty na GTK+
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-x11 = %{version}-%{release}

%description gtk
GTK+ frontend for recordmydesktop.

%description gtk -l pl.UTF-8
Frontend do recordmydesktop oparty na GTK+.

%package x11
Summary:	X Window System resource for recordmydesktop
Summary(pl.UTF-8):	Zasoby X Window System do recordmydesktop
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description x11
X Window System resource for recordmydesktop.

%description x11 -l pl.UTF-8
Zasoby X Window System do recordmydesktop.

%prep
%setup -q -a 1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x
%{__make}

%if %{with gtk}
cd gtk-%{name}-%{version}
%configure
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gtk}
%{__make} -C gtk-%{name}-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}-gtk --all-name
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/recordmydesktop.1*

%if %{with x}
%files x11
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*
%endif

%if %{with gtk}
%files gtk -f %{name}-gtk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-recordMyDesktop
%{_desktopdir}/gtk-recordmydesktop.desktop
%{_pixmapsdir}/gtk-recordmydesktop.png
%endif
