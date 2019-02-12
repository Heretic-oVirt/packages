Name:             glusterfs-gnfs
Version:          3.12.2
Release:          40%{?dist}
License:          GPLv2 or LGPLv3+
URL:              http://gluster.readthedocs.io/en/latest/
Summary:          GlusterFS gNFS server
Group:            System Environment/Daemons
Requires:         glusterfs-server%{?_isa} = %{version}-%{release}

%description
GlusterFS is a distributed file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file
system. GlusterFS is one of the most sophisticated file systems in
terms of features and extensibility.  It borrows a powerful concept
called Translators from GNU Hurd kernel. Much of the code in GlusterFS
is in user space and easily manageable.

This package provides the glusterfs gNFS server subpackage to satisfy explicit
dependencies while using RHGS version of GlusterFS (where gNFS is included in
server subpackage).

%files

%changelog
* Tue Feb 12 2019 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 3.12.2-40
- Updated package release to latest RHGS 3.4.x

* Sat Jan 12 2019 Giuseppe Ragusa <giuseppe.ragusa@fastmail.fm> - 3.12.2-32
- Created package to satisfy dependencies while using RHGS 3.4
