config_opts['chroot_setup_cmd'] = 'install tar gcc-c++ redhat-rpm-config redhat-release which xz sed make bzip2 gzip gcc coreutils unzip shadow-utils diffutils cpio bash gawk rpm-build info patch util-linux findutils grep iproute net-tools'
config_opts['dist'] = 'el8.casjay'  # only useful for --resultdir variable subst
config_opts['releasever'] = '8'
config_opts['package_manager'] = 'dnf'
config_opts['extra_chroot_dirs'] = [ '/run/lock', ]
config_opts['bootstrap_image'] = 'quay.io/almalinuxorg/almalinux:8'


config_opts['dnf.conf'] = """
[main]
keepcache=1
debuglevel=2
reposdir=/dev/null
logfile=/var/log/yum.log
retries=20
obsoletes=1
gpgcheck=0
assumeyes=1
syslog_ident=mock
syslog_device=
metadata_expire=0
mdpolicy=group:primary
best=0
skip_if_unavailable=True
install_weak_deps=0
protected_packages=
module_platform_id=platform:el8
user_agent={{ user_agent }}


[baseos]
name=AlmaLinux $releasever - BaseOS
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/baseos
# baseurl=https://repo.almalinux.org/almalinux/$releasever/BaseOS/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8
skip_if_unavailable=False

[appstream]
name=AlmaLinux $releasever - AppStream
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/appstream
# baseurl=https://repo.almalinux.org/almalinux/$releasever/AppStream/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[powertools]
name=AlmaLinux $releasever - PowerTools
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/powertools
# baseurl=https://repo.almalinux.org/almalinux/$releasever/PowerTools/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[extras]
name=AlmaLinux $releasever - Extras
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/extras
# baseurl=https://repo.almalinux.org/almalinux/$releasever/extras/$basearch/os/
enabled=1
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[devel]
name=AlmaLinux $releasever - Devel (WARNING: UNSUPPORTED - FOR BUILDROOT USE ONLY!)
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/devel
# baseurl=https://repo.almalinux.org/almalinux/$releasever/devel/$basearch/os/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[casjay-rpms]
name=Casjays RPMs for server use - $releasever $basearch
mirrorlist=https://github.com/CasjaysDev/rpm-devel/raw/main/docs/ZREPO/RHEL/rhel/mirrors/rpms
gpgkey=https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/rhel/keys/RPM-GPG-KEY-casjay
module_hotfixes=1
enabled=1
gpgcheck=1

[casjay-addons]
name=Casjays Extras for server use - $releasever $basearch
mirrorlist=https://github.com/CasjaysDev/rpm-devel/raw/main/docs/ZREPO/RHEL/rhel/mirrors/addons
gpgkey=https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/rhel/keys/RPM-GPG-KEY-casjay
module_hotfixes=1
enabled=1
gpgcheck=1
# end casjaysdev repos

# begin epel repos
[casjay-epel]
name=Extra Packages for Enterprise Linux $releasever - $basearch
baseurl=https://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch
gpgkey=https://archive.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-$releasever
module_hotfixes=1
enabled=1
gpgcheck=1
# end epel repos

# begin rpmfusion repos
[casjay-rpmfusion-free-updates]
name=RPM Fusion for EL Free - $releasever $basearch
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=free-el-updates-released-$releasever&arch=$basearch
gpgkey=https://download1.rpmfusion.org/free/el/RPM-GPG-KEY-rpmfusion-free-el-$releasever
module_hotfixes=1
enabled=1
gpgcheck=1

[casjay-rpmfusion-nonfree-updates]
name=RPM Fusion for EL Non-Free - $releasever $basearch
mirrorlist=http://mirrors.rpmfusion.org/mirrorlist?repo=nonfree-el-updates-released-$releasever&arch=$basearch
gpgkey=https://download1.rpmfusion.org/nonfree/el/RPM-GPG-KEY-rpmfusion-nonfree-el-$releasever
module_hotfixes=1
enabled=1
gpgcheck=1
# end rpmfusion repos


# begin remi repos
[casjay-remi-safe]
name=Safe Remi's RPM repository for Enterprise Linux $releasever - $basearch
mirrorlist=https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/mirrors/remi
gpgkey=https://rpms.remirepo.net/RPM-GPG-KEY-remi2018
module_hotfixes=1
enabled=1
gpgcheck=1

[casjay-remi-php]
name=Remi's PHP 7.4 RPM repository for Enterprise Linux $releasever - $basearch
mirrorlist=https://github.com/rpm-devel/casjay-release/raw/main/ZREPO/RHEL/mirrors/remi
gpgkey=https://rpms.remirepo.net/RPM-GPG-KEY-remi2018
module_hotfixes=1
enabled=1
gpgcheck=1
# end remi repos

# begin elrepo repos
[casjay-elrepo]
name=ELRepo.org Community Enterprise Linux Repository - $releasever $basearch
mirrorlist=http://mirrors.elrepo.org/mirrors-elrepo.el$releasever
gpgkey=https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
module_hotfixes=1
enabled=0
gpgcheck=1

[casjay-elrepo-kernel]
name=ELRepo.org Community Enterprise Linux Kernel Repository - $releasever $basearch
mirrorlist=http://mirrors.elrepo.org/mirrors-elrepo-kernel.el$releasever
gpgkey=https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
module_hotfixes=1
enabled=0
gpgcheck=1

[casjay-elrepo-extras]
name=ELRepo.org Community Enterprise Linux Extras Repository - $releasever $basearch
mirrorlist=http://mirrors.elrepo.org/mirrors-elrepo-extras.el$releasever
gpgkey=https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
module_hotfixes=1
enabled=0
gpgcheck=1
# end elrepo repos

# begin mariadb repos
[casjay-mariadb]
name=MariaDB 10.10 for RHEL - $releasever $basearch
baseurl=http://yum.mariadb.org/10.10/rhel/$releasever/$basearch
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
module_hotfixes=1
enabled=1
gpgcheck=1
# end mariadb repos

# begin postfix repos
[casjay-postfix]
name=postfix for server use - $releasever $basearch
baseurl=https://repos.oostergo.net/$releasever/postfix-3.7
gpgkey=https://repos.oostergo.net/RPM-GPG-KEY
module_hotfixes=1
enabled=1
gpgcheck=1
# end postfix repos

[casjay-nodejs]
name=nodejs for server use - $releasever $basearch
baseurl=https://rpm.nodesource.com/pub_18.x/el/$releasever/$basearch
gpgkey=https://rpm.nodesource.com/pub/el/NODESOURCE-GPG-SIGNING-KEY-EL
module_hotfixes=1
enabled=1
gpgcheck=1

[casjay-yarn]
name=Yarn for server use - $releasever $basearch
baseurl=https://dl.yarnpkg.com/rpm/
gpgkey=https://dl.yarnpkg.com/rpm/pubkey.gpg
enabled=1
gpgcheck=1

[casjay-docker]
name=docker for server use - $releasever[I $basearch
baseurl=https://download.docker.com/linux/centos/$releasever/$basearch/stable
gpgkey=https://download.docker.com/linux/centos/gpg
module_hotfixes=1
enabled=1
gpgcheck=1

[baseos-debuginfo]
name=AlmaLinux $releasever - BaseOS debuginfo
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/baseos-debuginfo
# baseurl=https://repo.almalinux.org/almalinux/$releasever/BaseOS/debug/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[appstream-debuginfo]
name=AlmaLinux $releasever - AppStream debuginfo
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/appstream-debuginfo
# baseurl=https://repo.almalinux.org/almalinux/$releasever/AppStream/debug/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[powertools-debuginfo]
name=AlmaLinux $releasever - PowerTools debuginfo
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/powertools-debuginfo
# baseurl=https://repo.almalinux.org/almalinux/$releasever/PowerTools/debug/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[extras-debuginfo]
name=AlmaLinux $releasever - Extras debuginfo
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/extras-debuginfo
# baseurl=https://repo.almalinux.org/almalinux/$releasever/extras/debug/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[devel-debuginfo]
name=AlmaLinux $releasever - Devel debuginfo
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/devel-debuginfo
# baseurl=https://repo.almalinux.org/almalinux/$releasever/devel/debug/$basearch/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[baseos-source]
name=AlmaLinux $releasever - BaseOS Source
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/baseos-source
# baseurl=https://repo.almalinux.org/almalinux/$releasever/BaseOS/Source/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[appstream-source]
name=AlmaLinux $releasever - AppStream Source
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/appstream-source
# baseurl=https://repo.almalinux.org/almalinux/$releasever/AppStream/Source/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[powertools-source]
name=AlmaLinux $releasever - PowerTools Source
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/powertools-source
# baseurl=https://repo.almalinux.org/almalinux/$releasever/PowerTools/Source/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[extras-source]
name=AlmaLinux $releasever - Extras Source
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/extras-source
# baseurl=https://repo.almalinux.org/almalinux/$releasever/extras/Source/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

[devel-source]
name=AlmaLinux $releasever - Devel Source
mirrorlist=https://mirrors.almalinux.org/mirrorlist/$releasever/devel-source
# baseurl=https://repo.almalinux.org/almalinux/$releasever/devel/Source/
enabled=0
gpgcheck=1
gpgkey=file:///usr/share/distribution-gpg-keys/alma/RPM-GPG-KEY-AlmaLinux-8

"""
