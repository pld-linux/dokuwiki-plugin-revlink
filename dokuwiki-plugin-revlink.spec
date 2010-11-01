%define		plugin		revlink
Summary:	DokuWiki revlink plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20090125
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.dokuwiki.org/_export/code/plugin:revlink?codeblock=0#/syntax.php
# Source0-md5:	dc4cb942df8aeda0c22753f7901478f2
URL:		http://www.dokuwiki.org/plugin:revlink
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20090125
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Extend internal link syntax to allow linking to a previous revision a
of page.

%prep
%setup -qcT
cp -a %{SOURCE0} .

version=$(awk -F"'" '/date/&&/=>/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
