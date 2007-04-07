#
# Conditional build
%bcond_without	gtk	# don't build gtk frontend

Summary:	Desktop session recorder
Summary(pl.UTF-8):	Rejestrator pulpitu
Name:		recordmydesktop
Version:	0.3.4
Release:	1
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
Summary:	GTK frontend for recordmydesktop
Summary(pl.UTF-8):	Frontend do recordmydesktop napisany w GTK
Group:		X11/Applications
Requires:	%{name} = %{version}

%description gtk
GTK frontend for recordmydesktop.

%description gtk -l pl.UTF-8
Frontend do recordmydesktop napisany w GTK.

%prep
%setup -q -a 1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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

%if %{with gtk}
%files -f %{name}-gtk.lang gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk-recordMyDesktop
%{_desktopdir}/gtk-recordmydesktop.desktop
%{_pixmapsdir}/gtk-recordmydesktop.png
%endif
