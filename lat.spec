Summary:	LAT - LDAP Administration Tool
Name:		lat
Version:	1.2.2
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Other
URL:		http://people.mmgsecurity.com/~lorenb/lat/
Source0:	http://people.mmgsecurity.com/~lorenb/lat/releases/%{name}-%{version}.tar.bz2
BuildRequires:	mono-devel
BuildRequires:	gnome-sharp2
BuildRequires:	gnome-keyring-devel
BuildRequires:	autoconf2.5
BuildRequires:	intltool
BuildRequires:	scrollkeeper
BuildRequires:	desktop-file-utils
BuildRequires:	dbus-sharp
BuildRequires:	avahi-sharp
Requires(post):	scrollkeeper
Requires(postun):	scrollkeeper
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
LAT stands for LDAP Administration Tool. The tool allows you to browse
LDAP-based directories and add/edit/delete entries contained within.
It can store profiles for quick access to different servers. There are
also different views available such as Users, Groups and Hosts which
allow you to easily manage objects without having to deal with the
intricacies of LDAP.

%prep
%setup -q

%build
aclocal
libtoolize
automake
autoconf
%configure2_5x \
	--enable-networkmanager=no \
	--enable-avahi=yes \
	--libdir=%{_prefix}/lib
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --add-category="Network" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper
#%%update_icon_cache hicolor
%update_menus

%postun
%clean_scrollkeeper
#%%clean_icon_cache hicolor
%clean_menus

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_prefix}/lib/%{name}
%attr(755,root,root) %{_prefix}/lib/%{name}/*
%{_mandir}/man1/lat.1*
%{_datadir}/omf/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/application-registry/%{name}.applications
%exclude %{_localstatedir}/scrollkeeper
%{_prefix}/lib/pkgconfig/lat-plugins.pc


