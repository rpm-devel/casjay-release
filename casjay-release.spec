Summary: Casjays repos release file
Name: casjay-release
Version: 1.5
Release: %{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://rpm.casjaysdev.pro/

SOURCE0: mock-files.tar.gz

%if 0%{?rhel} == 9
%ifnarch %{x86_64}
%define  repo_replace false
%endif
Source1: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh9.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} == 8
%ifnarch %{x86_64}
%define  repo_replace true
%endif
Source1: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh8.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} == 7
%ifnarch %{x86_64}
%define  repo_replace true
%endif
Source1: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} < 7
%ifnarch %{x86_64}
%define  repo_replace true
%endif
Source1: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?fedora}
Source1: https://github.com/rpm-devel/casjay-release/raw/main/casjay.fc.repo
Source2: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/Fedora/keys/RPM-GPG-KEY-casjay
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
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_sysconfdir}
%{__tar} xfvz %{SOURCE0} -C %{buildroot}%{_sysconfdir}
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/casjay.repo
%{__install} -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay
%if "%{repo_replace}" = "true"
sed -i 's|http://mirrors.elrepo.org/mirrors-elrepo.*|https://rpm-devel.sourceforge.io/repo/RHEL/$releasever/$basearch/empty|g' /etc/yum.repos.d/casjay.repo
sed -i 's|https://mirror.usi.edu/pub/remi/enterprise/.*|https://rpm-devel.sourceforge.io/repo/RHEL/$releasever/$basearch/empty|g' /etc/yum.repos.d/casjay.repo
%endif

%clean
%{__rm} -rf %{buildroot}

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
yum makecache -q >/dev/null

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/yum.repos.d/casjay.repo
%pubkey %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%files devel
%{_sysconfdir}/mock/casjay-8-x86_64.cfg
%{_sysconfdir}/mock/casjay-8-aarch64.cfg
%{_sysconfdir}/mock/templates/casjay-8.tpl

%changelog
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
