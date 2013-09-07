Name: lua-gd-openresty
Version: 2.0.33r2
Release: 1
Summary: gd bindings for the Lua programming language
Summary(pt_BR): Bindings da biblioteca gd para a linguagem Lua
Packager: Alexandre Erwin Ittner <aittner@netuno.com.br>
License: MIT
Group: Libraries
Group(pt_BR): Bibliotecas
Source0: %{name}-%{version}.tar.gz
URL: http://lua-gd.luaforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: openresty
Requires: gd >= 2.0.33
BuildRequires: lua-devel
BuildRequires: gd-devel >= 2.0.33
Prefix: /usr
Provides: luagd

%description
Lua-GD is a library that allows you to use the gd graphic library from
programs written in the Lua programming language.


%description -l pt_BR
Lua-GD é uma biblioteca que permite usar a biblioteca gráfica gd em
programas escritos na linguagem Lua.


%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}/opt/openresty/lualib
cp *.so %{buildroot}/opt/openresty/lualib/

%clean
rm -rf %{buildroot} $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING doc/* demos
/opt/openresty/lualib/*.so*

%changelog
* Sat Sep 7 2013 Anton Jouline <anton.jouline@cbsinteractive.com>
- added Openresty spec
* Sun Apr 30 2006 Alexandre Erwin Ittner <aittner@netuno.com.br>
- New version. License update.
* Sun Aug 28 2005 Alexandre Erwin Ittner <aittner@netuno.com.br>
- First version of this package.

