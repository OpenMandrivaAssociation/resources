%undefine _debugsource_packages
%define appid net.nokyan.Resources

Name:           resources
Version:        1.8.0
Release:        1
Summary:        Monitor your system processes
License:        GPL-3.0-or-later
URL:            https://github.com/nokyan/resources
Source0:        https://github.com/nokyan/resources/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  appstream
BuildRequires:  appstream-util
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  rust-packaging
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       dmidecode
Requires:       polkit

%description
Resources is a simple yet powerful monitor for your system resources and
processes, written in Rust and using GTK 4 and libadwaita for its GUI.

%prep
%autosetup -a1

%build
%meson -Dprofile=default
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/polkit-1/actions/%{appid}.policy
%{_libexecdir}/%{name}/
