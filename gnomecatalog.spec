%define name gnomecatalog
%define version 0.3.4.2
%define release 4

Summary: CD-ROM catalog for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Archiving/Other
Url: http://gnomecatalog.sf.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: imagemagick
BuildRequires: desktop-file-utils
BuildArch: noarch
Requires: pyvorbis
Requires: python-kaa-metadata
Requires: pygtk2.0 pygtk2.0-libglade gnome-python-gconf
Requires: gnome-python gnome-python-gnomevfs
Requires: gnome-python-gtkhtml2 python-sqlite2

Requires(post): desktop-file-utils, shared-mime-info
Requires(postun): desktop-file-utils, shared-mime-info

%description
CD-ROM catalog for GNOME.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root %buildroot
%find_lang %name
rm -rf %buildroot%_prefix/lib/mime 

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Archiving-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


mkdir -p $RPM_BUILD_ROOT/%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT/%{_liconsdir}
convert -scale 32 share/pixmaps/gcatalog.png %buildroot%_iconsdir/%name.png
convert -scale 16 share/pixmaps/gcatalog.png %buildroot%_miconsdir/%name.png
install share/pixmaps/gcatalog.png %buildroot%_liconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_mime_database
%clean_desktop_database
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README
%_bindir/%name
%_mandir/man1/*.1*
%_datadir/%name
%_datadir/application-registry/*
%_datadir/applications/*
%_datadir/mime-info/*
%_datadir/mime/packages/*
%_datadir/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-gcatalog.png
%py_puresitedir/*
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png




%changelog
* Fri Nov 04 2011 Götz Waschk <waschk@mandriva.org> 0.3.4.2-3mdv2012.0
+ Revision: 717577
- rebuild

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 0.3.4.2-2mdv2011.0
+ Revision: 592875
- rebuild for new python 2.7

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 0.3.4.2-1mdv2011.0
+ Revision: 383901
- new version

* Mon Dec 29 2008 Götz Waschk <waschk@mandriva.org> 0.3.4.1-3mdv2009.1
+ Revision: 320970
- rebuild for new python

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.3.4.1-2mdv2009.0
+ Revision: 266922
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 0.3.4.1-1mdv2009.0
+ Revision: 199947
- New version 0.3.4.1

* Sat Feb 02 2008 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdv2008.1
+ Revision: 161409
- depend on pyvorbis

* Sun Jan 20 2008 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdv2008.1
+ Revision: 155408
- new version
- update deps
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.2.1-3mdv2007.0
+ Revision: 88366
- fix installation
- Import gnomecatalog

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.2.1-3mdv2007.1
- update file list

* Tue Aug 01 2006 G�tz Waschk <waschk@mandriva.org> 0.2.1-2mdv2007.0
- macros
- xdg menu

* Fri Jul 29 2005 G�tz Waschk <waschk@mandriva.org> 0.2.1-2mdk
- fix buildrequires

* Fri Jul 29 2005 G�tz Waschk <waschk@mandriva.org> 0.2.1-1mdk
- New release 0.2.1

* Wed Jul 27 2005 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdk
- initial package

