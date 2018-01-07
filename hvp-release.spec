Name:           hvp-release
Version:        7
Release:        2
Summary:        Heretic oVirt Project repository configuration

Group:          System Environment/Base
License:        GPLv2

URL:            http://dangerous.ovirt.life/
Source0:        http://dangerous.ovirt.life/hvp-repos/RPM-GPG-KEY-hvp
Source1:        GPL
Source2:        HVP.repo

BuildArch:     noarch
Requires:      redhat-release >=  %{version}
# hvp-release is only for enterprise linux, not fedora
Conflicts:     fedora-release

%description
This package contains the Heretic oVirt Project (HVP) repository
GPG key and Yum files.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-hvp

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Fri Jan 05 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 7-2
- Updated HVP.repo to use $releasever

* Sun Dec 24 2017 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 7-1
- Initial release, borrowing spec from EPEL release package
