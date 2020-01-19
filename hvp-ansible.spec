%global provider	github
%global provider_tld	com
%global project		Heretic-oVirt
%global repo		ansible
# https://github.com/Heretic-oVirt/ansible
%global provider_prefix	%{provider}.%{provider_tld}/%{project}/%{repo}
%global commit		a3b7239b6812f9e97f6d05389fff08e9de8c0636
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		hvp-ansible
Version:	0.2
Release:	3.git%{shortcommit}%{?dist}
Summary:	Playbooks, roles, variables and scripts for Heretic oVirt Project
Group:		Development/Libraries
License:	GPLv2
URL:		https://%{provider_prefix}
Source0:	https://%{provider_prefix}/tarball/%{shortcommit}/%{project}-%{repo}-%{shortcommit}.tar.gz

BuildArch:	noarch

Requires:   ansible >= 2.8
Requires:   python2-jmespath python-netaddr python-dns python-psycopg2 libselinux-python libsemanage-python NetworkManager-glib python-passlib
Requires:   gdeploy ovirt-engine-sdk-python ovirt-ansible-roles

%description
This package contains the Ansible files used for Heretic oVirt Project final configuration automation.

%prep
%setup -q -n %{project}-%{repo}-%{shortcommit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible
cp -a hvp* %{buildroot}%{_datadir}/ansible/%{name}

%files
%doc README.md LICENSE TODO.md
%{_datadir}/ansible/%{name}

%changelog
* Sun Jan 19 2020 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.2.0-3.gita3b7239b6812f9e97f6d05389fff08e9de8c0636
- Updated to latest commit

* Sat Jan 18 2020 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.2.0-2.git68fff6e36a9d68b2d4d17e78a47464aa166a5e6c
- Updated to latest commit

* Sun Sep 29 2019 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.2.0-1.git0f0cdc5d0df952ecc0b172a80e3cc2fd8f6fc573
- Updated to latest commit
- Updated minimum required Ansible version
- Generalized source URL to work also for non-master braches

* Thu Feb 14 2019 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.2.0-0.git3d35bbd8090e30bbafba1654328897e2fbdd1c79
- Updated to latest commit
- Updated minimum required Ansible version

* Sun Sep 30 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-9.git61e04a3752f76c523e552eb319e7ef5b57055293
- Updated to latest commit

* Fri Sep 21 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-8.git0e9585947b67accd0aaf8565fcd08b9d1e64dd1f
- Updated to latest commit

* Sat Sep 08 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-7.git667432a7bce801a6b0046cb97f07288cc3ea0eeb
- Updated to latest commit

* Sun Jun 17 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-6.giteb93975a795c1402f23aa729ab72b8cf4c30cca9
- Updated to latest commit
- Added TODO to docs

* Thu Jun 14 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-5.git35e5963529bb7265623762c6c6b928938c553570
- Updated package dependencies

* Sun Feb 25 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-4.git35e5963529bb7265623762c6c6b928938c553570
- Updated to latest commit

* Sat Feb 24 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-3.git8afb72b1004fe59e238d928c4ec58752e70aa6fd
- Updated to latest commit

* Sat Jan 27 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-2.git76fd0f13d1bb44a2c6378d074325ea925121b74d
- Updated to latest commit

* Fri Dec 29 2017 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-1.gitaf7af3311112d831103eb7fd679e25072c7a0373
- Initial package release (spec taken from kubernetes-ansible package)
