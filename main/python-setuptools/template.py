pkgname = "python-setuptools"
pkgver = "70.1.0"
pkgrel = 0
hostmakedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "Easily build and distribute Python packages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pypa/setuptools"
source = f"$(PYPI_SITE)/s/setuptools/setuptools-{pkgver}.tar.gz"
sha256 = "01a1e793faa5bd89abc851fa15d0a0db26f160890c7102cd8dce643e886b47f5"
env = {
    "SETUPTOOLS_INSTALL_WINDOWS_SPECIFIC_FILES": "0",
    "SETUPTOOLS_DISABLE_VERSIONED_EASY_INSTALL_SCRIPT": "1",
}
# missing checkdepends
options = ["!check"]


def do_build(self):
    self.do(
        "python3",
        "setup.py",
        "build",
    )


def do_install(self):
    from cbuild.util import python

    self.do(
        "python3",
        "setup.py",
        "install",
        "--prefix=/usr",
        "--root=" + str(self.chroot_destdir),
    )
    python.precompile(self, "usr/lib")


def post_install(self):
    self.install_license("LICENSE")
