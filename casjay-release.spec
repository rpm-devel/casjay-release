
Summary: Casjays repos release file
Name: casjay-release
Version: 1.4
Release: 3%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://casjaysdev.com/

%if 0%{?rhel} >= 9
Source0: casjay.rh9.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/rhel/keys/RPM-GPG-KEY-casjay
%elseif 0%{?rhel} >= 8
Source0: casjay.rh8.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/rhel/keys/RPM-GPG-KEY-casjay
%elseif 0%{?rhel} < 8
Source0: casjay.rh.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/rhel/keys/RPM-GPG-KEY-casjay
%elseif 0%{?fedora}
Source0: casjay.fc.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/rhel/keys/RPM-GPG-KEY-casjay
%endif

%description
This package contains yum configuration for the casjaysdev.com Linux Repository, as well as the public GPG keys used to sign packages.

%prep
%setup -c -T
%{__cp} -a %{SOURCE1} .

# %build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/casjay.repo
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%clean
%{__rm} -rf %{buildroot}

%post
%if 0%{?rhel} >= 8
grep -q 'best=' /etc/yum.conf || sed -i '/^\[main\]/a best=False' /etc/yum.conf &>/dev/null

%endif

%files
%defattr(-, root, root, 0755)
%pubkey RPM-GPG-KEY-casjay
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/casjay.repo
%dir %{_sysconfdir}/pki/rpm-gpg/
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%changelog
* Thu Nov 04 2021 CasjaysDev <rpm-devel@casjaysdev.com> - 1.4
- Added rockylinux repos

* Sat Jun 01 2019 CasjaysDev <rpm-devel@casjaysdev.com> - 0.3
- Fixes for fedora

* Thu Feb 22 2018 CasjaysDev <rpm-devel@casjaysdev.com> - 0.2
- Fixes for OS Specific rpm repos

* Thu Feb 22 2018 CasjaysDev <rpm-devel@casjaysdev.com> - 0.1
- initial release
