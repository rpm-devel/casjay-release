Summary: Casjays repos release file
Name: casjay-release
Version: 1.8
Release: 1%{?dist}
License: GPL-2.0-only
URL: http://rpm.casjaysdev.pro/
ExclusiveArch: x86_64 aarch64

Source0: mock-files.tar.gz

%if 0%{?rhel} >= 10
%ifnarch x86_64 aarch64
%define  repo_replace false
%endif
%if 0%{?oraclelinux}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/oraclelinux.10.repo
%elif 0%{?rocky}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/rockylinux.10.repo
%else
Source1: https://github.com/rpm-devel/casjay-release/raw/main/almalinux.10.repo
%endif
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/EL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} == 9
%ifnarch x86_64 aarch64
%define  repo_replace false
%endif
%if 0%{?oraclelinux}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/oraclelinux.9.repo
%elif 0%{?rocky}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/rockylinux.9.repo
%else
Source1: https://github.com/rpm-devel/casjay-release/raw/main/almalinux.9.repo
%endif
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/EL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} == 8
%ifnarch %{x86_64}
%define  repo_replace true
%endif
%if 0%{?oraclelinux}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/oraclelinux.8.repo
%elif 0%{?rocky}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/rockylinux.8.repo
%else
Source1: https://github.com/rpm-devel/casjay-release/raw/main/almalinux.8.repo
%endif
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/EL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} == 7
%ifnarch %{x86_64}
%define  repo_replace true
%endif
Source1: https://github.com/rpm-devel/casjay-release/raw/main/centos.7.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/EL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} < 7
%ifnarch %{x86_64}
%define  repo_replace true
%endif
Source1: https://github.com/rpm-devel/casjay-release/raw/main/centos.6.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/EL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?fedora}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/fedora.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/Fedora/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?suse_version}
%ifnarch x86_64 aarch64
%define  repo_replace false
%endif
%if 0%{?suse_version} >= 1599
Source1: https://github.com/rpm-devel/casjay-release/raw/main/opensuse.tumbleweed.repo
%else
Source1: https://github.com/rpm-devel/casjay-release/raw/main/opensuse.leap15.repo
%endif
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/EL/keys/RPM-GPG-KEY-casjay
%endif

%description
This package contains yum configuration for the casjaysdev.pro Linux Repository, as well as the public GPG keys used to sign packages.

%package devel
Requires: mock
Summary: development packages
%description devel
contains custom mock files.

%prep
%setup -c -T
%{__cp} -a %{SOURCE1} .
%{__cp} -a %{SOURCE2} .

%install
%{__mkdir} -p %{buildroot}%{_sysconfdir}
%{__tar} xfvz %{SOURCE0} -C %{buildroot}%{_sysconfdir}
%if 0%{?suse_version}
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/zypp/repos.d/casjay.repo
%else
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/casjay.repo
%endif
%{__install} -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay
%if "%{repo_replace}" == "true"
sed -i 's|.*http://mirrors.elrepo.org/mirrors-elrepo.*|baseurl=https://rpm-devel.sourceforge.io/repo/EL/$releasever/$basearch/empty|g' %{buildroot}%{_sysconfdir}/yum.repos.d/casjay.repo
sed -i 's|.*https://mirror.usi.edu/pub/remi/enterprise/.*|baseurl=https://rpm-devel.sourceforge.io/repo/EL/$releasever/$basearch/empty|g' %{buildroot}%{_sysconfdir}/etc/yum.repos.d/casjay.repo
%endif

%post
%if 0%{?rhel} >= 8
if grep -qs 'skip_if_unavailable=' "/etc/yum.conf"; then 
  sed -i 's|skip_if_unavailable=.*|skip_if_unavailable=True|g' "/etc/yum.conf" &>/dev/null 
else
  sed -i '/^\[main\]/a skip_if_unavailable=True' "/etc/yum.conf" &>/dev/null
fi
if grep -qs 'best=' "/etc/yum.conf"; then 
  sed -i 's|best=.*|best=True|g' "/etc/yum.conf" &>/dev/null 
else
  sed -i '/^\[main\]/a best=True' "/etc/yum.conf" &>/dev/null
fi
%endif
%if 0%{?suse_version}
zypper refresh >/dev/null 2>&1 || true
%else
yum makecache -qy >/dev/null
%endif

%files
%if 0%{?suse_version}
%config %{_sysconfdir}/zypp/repos.d/casjay.repo
%else
%config %{_sysconfdir}/yum.repos.d/casjay.repo
%endif
%pubkey %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%files devel
%{_sysconfdir}/mock/casjay-10-x86_64.cfg
%{_sysconfdir}/mock/casjay-10-aarch64.cfg
%{_sysconfdir}/mock/casjay-9-x86_64.cfg
%{_sysconfdir}/mock/casjay-9-aarch64.cfg
%{_sysconfdir}/mock/casjay-8-x86_64.cfg
%{_sysconfdir}/mock/casjay-8-aarch64.cfg
%{_sysconfdir}/mock/templates/casjay-10.tpl
%{_sysconfdir}/mock/templates/casjay-9.tpl
%{_sysconfdir}/mock/templates/casjay-8.tpl

%changelog
* Tue Sep 02 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.8-1
- Add openSUSE Leap 15 and Tumbleweed repo files from scratch
- Detect %%{?suse_version} >= 1599 for Tumbleweed vs Leap 15.x
- Install to /etc/zypp/repos.d/casjay.repo on SUSE platforms
- Run zypper refresh in %%post on SUSE; yum makecache elsewhere

* Tue Sep 02 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.7-1
- Add Rocky Linux and Oracle Linux per-distro repo files (EL8/9/10)
- Detect %%{?oraclelinux} and %%{?rocky} within each %%if rhel block
- Keep casjay.rh9.repo as compat copy for scripts that curl it by old name
- Installed repo file is always casjay.repo for all distros

* Thu Jul 03 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.6-1
- SPDX: GPLv2 -> GPL-2.0-only; fix SOURCE0 case; add ExclusiveArch; drop rm -rf %%{buildroot}

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.6-1
- Add EL 10 / AlmaLinux 10 support
- Add EL10 repo file and mock configs
- Fix %if condition syntax
- Remove deprecated Group, %clean, %defattr

* Thu Apr 01 2023 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.5
- Moved to almalinux repos

* Thu Nov 04 2021 CasjaysDev <rpm-devel@casjaysdev.pro> - 1.4
- Added rockylinux repos

* Sat Jun 01 2019 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.3
- Fixes for fedora

* Thu Feb 22 2018 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.2
- Fixes for OS Specific rpm repos

* Thu Feb 22 2018 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.1
- initial release
