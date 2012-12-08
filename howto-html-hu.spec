%define DATE	20040814
%define    language  Hungarian
%define    lang      hu
%define format1      html-%{lang}
%define format2      HTML/%{lang}

Summary:   %language HOWTO documents (html format) from the Linux Documentation Project
Name:      howto-%{format1}
Version:	10.1
Release:	%mkrel 11
Group:		Books/Howtos

Source0:   %name.tar

Url:		http://www.kde.hu/mlp/hogyanok/
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

BuildRequires: howto-utils
Requires:    locales-%lang, xdg-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
untar_howtos; makehowtoindex %lang %language > index.html; cp -a * $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%_datadir/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %language
Comment=HOWTO documents (html format) from the Linux Documentation Project in %language
Exec=xdg-open %_datadir/doc/HOWTO/HTML/%lang/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/HOWTO/%{format2}/
%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 10.1-9mdv2011.0
+ Revision: 665423
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 10.1-8mdv2011.0
+ Revision: 605866
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 10.1-7mdv2010.1
+ Revision: 520701
- rebuilt for 2010.1

* Fri Jul 04 2008 Oden Eriksson <oeriksson@mandriva.com> 10.1-6mdv2009.0
+ Revision: 231700
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 10.1-4mdv2008.1
+ Revision: 150264
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Funda Wang <fwang@mandriva.org> 10.1-3mdv2008.0
+ Revision: 82173
- Rebuild for new era
- Import howto-html-hu



* Thu Jul 07 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.1-2mdk
- fix menu entry (#16628)

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.1-1mdk
- new snapshot

* Mon Mar 22 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 10-0.1mdk
- new snapshot

* Sat Feb 15 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.4mdk
- fix menu generation

* Thu Feb 13 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.3mdk
- synchronize all howtos spec files
- use new howto-utils

* Wed Feb 05 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.2mdk
- fix menu entry
- rebuild for latest makehowtoindex %%lang %%language > index.html)

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.1mdk
- new snapshot

* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.0-0.1mdk
- new snapshot
- add real url
- sanitize menu entry (fix menu-command-not-in-package)

* Thu Jan 29 2002 Adrien DEMAREZ <ademarez@mandrakesoft.com> 8.2-2mdk
- updated howtos

* Thu Jan 17 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-1mdk
- Fix menu entry (icon)

* Fri Sep 07 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-2mdk
- Modified menu entry so that it works with KDE and gnome

* Thu Aug 30 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Automatically updated

* Tue Mar 13 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 8.0-1mdk
- bump release number
- fix tmppath
- build with new howto-utils ... and use it
- add language name

* Fri Mar  2 2001 Etienne Faure  <etienne@mandrakesoft.com> 7.1-4mdk
- rebuild with new howto-utils

* Sat Jan 13 2001 Etienne Faure  <etienne@mandrakesoft.com> 7.1-3mdk
- modified menu entry

* Fri Dec 15 2000 Etienne Faure  <etienne@mandraksoft.com> 7.1-2mdk
- added icons

* Thu Nov 09 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.1-1mdk
- used srpm from Andras TIMAR <timar@linux-mandrake.com> :
	- first Mandrake RPM
