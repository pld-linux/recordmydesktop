#
# Conditional build
%bcond_without	gtk	# don't build GTK+ frontend
%bcond_without	qt	# don't build Qt frontend
%bcond_without  x	# don't build for X Window System frontends
%define		module	recordMyDesktop
#
Summary:	Desktop session recorder
Summary(pl.UTF-8):	Rejestrator pulpitu
Name:		recordmydesktop
Version:	0.3.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/recordmydesktop/%{name}-%{version}.tar.gz
# Source0-md5:	9834d0fa7dfb67366434cc1c3a857e9c
Source1:	http://dl.sourceforge.net/recordmydesktop/gtk-%{name}-%{version}.tar.gz
# Source1-md5:	2637b9be9801e0b2c3b6dae8f86a8b59
Source2:	http://dl.sourceforge.net/recordmydesktop/qt-%{name}-%{version}.tar.gz
# Source2-md5:	bf1525740755615ae172ae27fef68fb5
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
%if %{with qt}
BuildRequires:	python-PyQt4-devel
%endif
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
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

%description gtk
GTK+ frontend for recordmydesktop.

%description gtk -l pl.UTF-8
Frontend do recordmydesktop oparty na GTK+.

%package qt
Summary:	Qt frontend for recordmydesktop
Summary(pl.UTF-8):	Frontend do recordmydesktop oparty na Qt
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	python-PyQt4

%description qt
Qt frontend for recordmydesktop.

%description qt -l pl.UTF-8
Frontend do recordmydesktop oparty na Qt.

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
%setup -q -a 1 -a 2

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
cd ..
%endif

%if %{with qt}
cd qt-%{name}-%{version}
sed -i -e 's@#! /bin/sh@#!/bin/bash@' configure
%configure
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean %{py_sitescriptdir}/%{module}

%if %{with gtk}
%{__make} -C gtk-%{name}-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang gtk-recordMyDesktop
%endif

%if %{with qt}
%{__make} -C qt-%{name}-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -rf __find.*
%find_lang qt-recordMyDesktop

%py_postclean %{py_sitescriptdir}/qt_recordMyDesktop
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
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%endif

%if %{with gtk}
%files gtk -f gtk-recordMyDesktop.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-recordMyDesktop
%{_desktopdir}/gtk-recordmydesktop.desktop
%{_pixmapsdir}/gtk-recordmydesktop.png
%endif

%if %{with qt}
%files qt -f qt-recordMyDesktop.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qt-recordMyDesktop
%{_desktopdir}/qt-recordmydesktop.desktop
%{_pixmapsdir}/qt-recordmydesktop*.png
%{py_sitescriptdir}/qt_recordMyDesktop
%endif
