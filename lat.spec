%global debug_package %{nil}
Summary:	LAT - LDAP Administration Tool
Name:		lat
Version:	1.2.4
Release:	1
License:	GPLv2
Group:		System/Configuration/Other
URL:		http://sourceforge.net/projects/ldap-at/
source0:  http://downloads.sourceforge.net/project/ldap-at/LAT/LAT%20-%20%{version}/%{name}-%{version}.tar.gz
BuildRequires:	mono-devel
BuildRequires:	gnome-sharp2
BuildRequires:	libgnome-keyring-devel
BuildRequires:	autoconf2.5
BuildRequires:	intltool
BuildRequires:	scrollkeeper
BuildRequires:	desktop-file-utils
BuildRequires:	dbus-sharp
BuildRequires:	avahi-sharp
BuildRequires:	gnome-sharp2-devel
buildrequires:  pkgconfig(glade-sharp-2.0)
Requires(post):	scrollkeeper
Requires(postun):	scrollkeeper

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

%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="GNOME" \
  --add-category="Network" \
  --add-category="X-MandrivaLinux-System-Configuration-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

mkdir -p %buildroot%_datadir/pkgconfig
mv %buildroot%_prefix/lib/pkgconfig/*.pc %buildroot%_datadir/pkgconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_prefix}/lib/%{name}
%attr(755,root,root) %{_prefix}/lib/%{name}/*
%{_mandir}/man1/lat.1*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/pkgconfig/lat-plugins.pc


%changelog
* Wed Sep 24 2008 Funda Wang <fundawang@mandriva.org> 1.2.3-2mdv2009.0
+ Revision: 287695
- move .pc files into arch-independent location

* Fri Aug 22 2008 Funda Wang <fundawang@mandriva.org> 1.2.3-1mdv2009.0
+ Revision: 275014
- fix br
- New version 1.2.3

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Feb 25 2007 Pascal Terjan <pterjan@mandriva.org> 1.2.2-1mdv2007.0
+ Revision: 125513
- 1.2.2

* Fri Nov 17 2006 Pascal Terjan <pterjan@mandriva.org> 1.2.1.1-3mdv2007.1
+ Revision: 85103
- Fix the x86_64 workaround (but why aren't we noarch ?)

* Thu Nov 16 2006 Pascal Terjan <pterjan@mandriva.org> 1.2.1.1-2mdv2007.1
+ Revision: 84963
- bump release
- Fix building on x86_64 until I understand if this should be noarch
- Enforce avahi support and siable networkmanager
- Disable parallel build
- 1.2.1.1
- Import lat

* Tue Sep 12 2006 Jerome Soyer <saispo@mandriva.org> 1.1.90-1mdv2007.0
- New release 1.1.90

* Wed Aug 30 2006 Jerome Soyer <saispo@mandriva.org> 1.1.6-1mdv2007.0
- New release 1.1.6

* Wed Aug 16 2006 Pascal Terjan <pterjan@mandriva.org> 1.1.5-2mdv2007.0
- BuildRequires avahi-sharp

* Tue Aug 01 2006 Jerome Soyer <saispo@mandriva.org> 1.1.5-1mdv2007.0
- Use development version for features

* Tue Jul 11 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.6-3mdv2007.0
- Don't use _desktopdir, once again it works on the cluster only because of 
  jpackage-utils...

* Thu Jul 06 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.6-2mdv2007.0
- Use _tmppath, not _tmpdir

* Thu Jul 06 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.6-1
- New release 1.0.6

* Sat Jun 17 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.5-1mdv2007.0
- Initial package

