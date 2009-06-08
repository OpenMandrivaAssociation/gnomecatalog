%define name gnomecatalog
%define version 0.3.4.2
%define release %mkrel 1

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


