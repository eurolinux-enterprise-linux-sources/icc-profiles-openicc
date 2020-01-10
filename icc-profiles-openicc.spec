Name:           icc-profiles-openicc
Version:        1.3.1
Release:        4%{?dist}
Summary:        The OpenICC profiles

Group:          User Interface/X
License:        zlib
URL:            http://www.freedesktop.org/wiki/OpenIcc
Source0:        http://downloads.sourceforge.net/project/openicc/OpenICC-Profiles/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  color-filesystem
Requires:       color-filesystem

#Old names of the package
#Introduced in Fedora 16 - Can be dropped by F-18
Provides:       openicc-data = %{version}-%{release}
Obsoletes:      openicc-data < %{version}-%{release}



%description
The OpenICC profiles are provided to serve color managed
applications and services.


%prep
%setup -q


%build
%configure --enable-verbose
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/{pixmaps,mime/packages}

install -pm 0644 *.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages
install -pm 0644 *.png $RPM_BUILD_ROOT%{_datadir}/pixmaps


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
fi
/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%doc default_profiles/base/LICENSE-ZLIB
%doc default_profiles/base/LICENSE-ZLIB-LSTAR
%dir %{_icccolordir}/OpenICC
%{_icccolordir}/OpenICC/compatibleWithAdobeRGB1998.icc
%{_icccolordir}/OpenICC/sRGB.icc
%{_icccolordir}/OpenICC/ProPhoto-RGB.icc
%dir %{_icccolordir}/Oyranos
%{_icccolordir}/Oyranos/Gray-CIE_L.icc
%{_icccolordir}/Oyranos/Gray_linear.icc
%{_icccolordir}/Oyranos/ITULab.icc
%dir %{_icccolordir}/basICColor
%{_icccolordir}/basICColor/LStar-RGB.icc
%dir %{_icccolordir}/lcms
%{_icccolordir}/lcms/LCMSLABI.ICM
%{_icccolordir}/lcms/LCMSXYZI.ICM
%{_icccolordir}/lcms/Lab.icc
%{_icccolordir}/lcms/XYZ.icc
%dir %{_colordir}/target
%dir %{_colordir}/target/NPES
%{_colordir}/target/NPES/TR002.ti3
%{_colordir}/target/NPES/TR003.ti3
%{_colordir}/target/NPES/TR005.ti3
%{_colordir}/target/NPES/TR006.ti3
%dir %{_colordir}/target/fogra
%{_colordir}/target/fogra/FOGRA28L.ti3
%{_colordir}/target/fogra/FOGRA29L.ti3
%{_colordir}/target/fogra/FOGRA30L.ti3
%{_colordir}/target/fogra/FOGRA39L.ti3
%{_colordir}/target/fogra/FOGRA40L.ti3
%{_datadir}/icons/application-vnd.iccprofile.png
%{_datadir}/icons/text-vnd.cgats.png
%{_datadir}/mime/packages/x-color-cgats.xml
%{_datadir}/mime/packages/x-color-icc.xml
%{_datadir}/pixmaps/application-vnd.iccprofile.png
%{_datadir}/pixmaps/%{name}_logo.png
%{_datadir}/pixmaps/text-vnd.cgats.png


%changelog
* Thu Jul 25 2013 Michal Srb <msrb@redhat.com> - 1.3.1-4
- Fix license tag

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Sat Jan 21 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1.1
- Drop wrong obsoletes

* Sat Aug 20 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.3.0-1
- Rename to icc-profiles-openicc
- Add scriptlet for icons directory
- Use absolute path for update-mime-database
- Drop README
- Add directory ownership

* Thu Jul 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Tue Jan 25 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jan 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.0.1-1
- Spec file rewrite

* Mon Dec 27 2010 - Kai-Uwe Behrmann <ku.b at gmx.de>
- split out a directory package from the mime types

* Fri Aug 28 2010 - Kai-Uwe Behrmann <ku.b at gmx.de>
- new package naming scheme for Oyranos independent installations
