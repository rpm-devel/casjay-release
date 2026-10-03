# casjay-release

`casjay-release` provides RPM and Zypper repository configuration for CasjaysDev Linux repositories and third-party package sources on supported Enterprise Linux, Fedora, and openSUSE systems.

---

## 📦 Install

Install the `casjay-release` RPM package from a trusted package source that provides it. The package installs the repository configuration for the detected distribution and imports the CasjaysDev repository signing key.

On DNF-based systems, install a downloaded package with:

```bash
sudo dnf install ./casjay-release*.rpm
```

On openSUSE, install a downloaded package with:

```bash
sudo zypper install ./casjay-release*.rpm
```

The package refreshes repository metadata after installation. Repository availability depends on the distribution and release configured on the system.

---

## 🗂️ Supported repository configurations

The package selects a configuration for AlmaLinux, CentOS, Fedora, Oracle Linux, Rocky Linux, or openSUSE. It installs the selected file as `/etc/yum.repos.d/casjay.repo` on DNF/YUM systems or `/etc/zypp/repos.d/casjay.repo` on openSUSE.

Additional repository definitions are organized under `ZREPO/` by distribution family. Individual third-party repositories may be disabled in the configuration and can be enabled by editing the installed `casjay.repo` file.

## 🛠️ Development

The repository contains the RPM spec, distribution-specific `.repo` files, GPG public keys, and mock build configuration. Build the package in a compatible RPM build environment with `rpmbuild` and the dependencies declared by the spec file. The `mock-files.tar.gz` archive supplies the mock configuration files installed by the development subpackage.

## 📄 License

Do What The F*ck You Want To Public License (WTFPL) — see [LICENSE.md](LICENSE.md).
