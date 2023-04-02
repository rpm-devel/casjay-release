Summary: Casjays repos release file
Name: casjay-release
Version: 1.5
Release: %{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://rpm.casjaysdev.com/

%if 0%{?rhel} == 9
Source0: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh9.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} == 8
Source0: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh8.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?rhel} <= 7
Source0: https://github.com/rpm-devel/casjay-release/raw/main/casjay.rh.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/keys/RPM-GPG-KEY-casjay
%endif
%if 0%{?fedora}
Source0: https://github.com/rpm-devel/casjay-release/raw/main/casjay.fc.repo
Source1: https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/Fedora/keys/RPM-GPG-KEY-casjay
%endif
SOURCE2: mock

%description
This package contains yum configuration for the casjaysdev.com Linux Repository, as well as the public GPG keys used to sign packages.

%package devel
Requires: mock
Summary: development packages
%description devel
contains custom mock files.

%prep
%setup -c -T
%{__cp} -a %{SOURCE1} .

%prep devel
%setup -c -T
%{__cp} -a %{SOURCE2} .

# %build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dpm 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/casjay.repo
%{__install} -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%install devel
%{__rm} -rf %{buildroot}
%{__install} -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}

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

%files
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/yum.repos.d/casjay.repo
%pubkey %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-casjay

%files devel
%{_sysconfdir}/mock/casjay-8-x86_64.cfg
%{_sysconfdir}/mock/casjay-8-aarch64.cfg
%{_sysconfdir}/mock/templates/casjay-8.tpl


%changelog
* Thu Apr 01 2023 CasjaysDev <rpm-devel@casjaysdev.com> - 1.5
- Moved to almalinux repos

* Thu Nov 04 2021 CasjaysDev <rpm-devel@casjaysdev.com> - 1.4
- Added rockylinux repos

* Sat Jun 01 2019 CasjaysDev <rpm-devel@casjaysdev.com> - 0.3
- Fixes for fedora

* Thu Feb 22 2018 CasjaysDev <rpm-devel@casjaysdev.com> - 0.2
- Fixes for OS Specific rpm repos

* Thu Feb 22 2018 CasjaysDev <rpm-devel@casjaysdev.com> - 0.1
- initial release
