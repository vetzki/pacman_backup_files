pkgver=r3.2927b3d
pkgrel=1
pkgname="pacman_backup_files"
pkgdesc="show pacnew and pacsave files"
depends=('python' 'tk')
makedepends=('cython')
optdepends=('kate: default editor'
            'xterm: default terminal'
            'ttf-dejavu: default font')
url="https://github.com/vetzki/pacman_backup_files"
source=("git+$url")
sha256sums=('SKIP') # integrity checked in prepare
arch=(any)
license=('GPL3')
_prefix="/usr"

pkgver() {
cd $pkgname
printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
# create c file for main
cd $pkgname

sha256sum -c integrity

cython py_pbf/py_pbf_main.py --embed
}

build() {
cd $pkgname
_pyvers="$(python -V|awk '{print $2}'|cut -d "." -f 1-2)"
python setup.py build_ext --inplace
# maybe better add main also to setup.py
gcc -O2 -I/usr/include/python${_pyvers}m -o py_pbf_main py_pbf/py_pbf_main.c -lpython${_pyvers}m -lpthread -lm -lutil -ldl
}

package() {
cd $srcdir/$pkgname

_libdir="$pkgdir/$_prefix/lib/${pkgname}"

# src
find . -type f -name "*.so" -exec install -D "{}" $_libdir/"{}" \;
install -D py_pbf_main $_libdir/py_pbf_main
install -D py_pbf/py_pbf_defconf.py $_libdir/py_pbf_defconf.py

# resources
# TODO: adjust path in .desktop and .sh file
install -Dm755 resources/pacman_backup_files.sh $pkgdir/$_prefix/bin/pacman_backup_files
# .desktop and icons
install -Dm644 resources/pacman_backup_files.desktop $pkgdir/usr/share/applications/pacman_backup_files.desktop
install -Dm644 resources/pacman-icon-symbolic.svg $pkgdir/$_prefix/share/icons/pacman_backup_files/pacman-icon-symbolic.svg
install -Dm644 resources/pacman-icon.png $pkgdir/$_prefix/share/icons/pacman_backup_files/pacman-icon.png

}
