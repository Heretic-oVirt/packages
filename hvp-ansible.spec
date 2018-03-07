%global provider	github
%global provider_tld	com
%global project		Heretic-oVirt
%global repo		ansible
# https://github.com/Heretic-oVirt/ansible
%global provider_prefix	%{provider}.%{provider_tld}/%{project}/%{repo}
%global commit		35e5963529bb7265623762c6c6b928938c553570
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		hvp-ansible
Version:	0.1
Release:	4.git%{shortcommit}%{?dist}
Summary:	Playbooks, roles, variables and scripts for Heretic oVirt Project
Group:		Development/Libraries
License:	GPLv2
URL:		https://%{provider_prefix}
Source0:	https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

BuildArch:	noarch

Requires:       ansible

%description
This package contains the Ansible files used for Heretic oVirt Project final configuration automation.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/ansible
cp -a hvp* %{buildroot}%{_datadir}/ansible/%{name}

%files
%doc README.md LICENSE
%{_datadir}/ansible/%{name}

%changelog
* Sun Feb 25 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-4.git35e5963529bb7265623762c6c6b928938c553570
- Updated to latest commit

* Sat Feb 24 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-3.git8afb72b1004fe59e238d928c4ec58752e70aa6fd
- Updated to latest commit

* Sat Jan 27 2018 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-2.git76fd0f13d1bb44a2c6378d074325ea925121b74d
- Updated to latest commit

* Fri Dec 29 2017 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 0.1.0-1.gitaf7af3311112d831103eb7fd679e25072c7a0373
- Initial package release (spec taken from kubernetes-ansible package)
