%define name gnomecatalog
%define version 0.2.1
%define release %mkrel 3
%define frel 1

Summary: CD-ROM catalog for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}-%frel.tar.bz2
License: GPL
Group: Archiving/Other
Url: http://gnomecatalog.sf.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
BuildArch: noarch
Requires: pygtk2.0 pygtk2.0-libglade gnome-python-gconf
Requires: gnome-python gnome-python-gnomevfs
Requires: gnome-python-gtkhtml2 python-sqlite2
Requires(post): desktop-file-utils, shared-mime-info
Requires(postun): desktop-file-utils, shared-mime-info

%description
CD-ROM catalog for GNOME.

%prep
%setup -q -n %name

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root %buildroot
%find_lang %name
rm -rf %buildroot%_prefix/lib/mime 
mkdir -p $RPM_BUILD_ROOT/%{_menudir}

cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="System/Archiving/Other" title="GNOME Catalog" \
  longtitle="Make disk/CD catalogs" mimetypes="application/x-gnomecatalog" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Archiving-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


mkdir -p $RPM_BUILD_ROOT/%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT/%{_liconsdir}
convert -scale 32 share/pixmaps/gcatalog.png %buildroot%_iconsdir/%name.png
convert -scale 16 share/pixmaps/gcatalog.png %buildroot%_miconsdir/%name.png
install share/pixmaps/gcatalog.png %buildroot%_liconsdir/%name.png
mv %buildroot%_datadir/icons/Default/ %buildroot%_datadir/icons/hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor

%postun
%clean_menus
%clean_mime_database
%clean_desktop_database
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/%name
%_datadir/application-registry/*
%_datadir/applications/*
%_datadir/mime-info/*
%_datadir/mime/packages/*
%_datadir/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-gcatalog.png
%py_puresitedir/*
%_menudir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png


