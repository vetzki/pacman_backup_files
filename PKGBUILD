pkgver=1
pkgrel=1
pkgname="pacman_backup_files"
pkgdesc="show pacnew and pacsave files"
depends=('python')
makedepends=('cython')
optdepends=('kate: default editor'
            'xterm: default terminal')
url="https://github.com/vetzki/pacman_backup_files"
source=('setup.py'
        'pacman_backup_files.sh'
        'py_pbf_main.py'
        'py_pbf_helper.py'
        'py_pbf_gui_sub.py'
        'py_pbf_gui.py'
        'py_pbf_defconf_json.py'
        'pacman_backup_files.desktop'
        'pacman-icon-symbolic.svg'
        'pacman-icon.png')
sha256sums=('282f3de7b12b7e5c5cd63e537678bd36f8d5bff7b49c0ed59aa61eff3d7f0f96'
            '26a2d40be81f84bf7ac2f6322f2eaa1f2b735e963a4d293fbdbb3594f5538e56'
            '4dd3dbe92cb762ca2212c7caab8293b2c92303c5dc5bfa2029ad44f051c46b37'
            'e814aa790dbe21b4924a48ddac95b58540ff593d1231020e783d18a30f9a027c'
            'cd092c71dee9553d75ae3d809f28004f6e9e6b904eea56b9fdeaee3b02e80fc7'
            '0641e9717a1a2a8c8e787fa311fc788d7629282d0293d5455f822dbbdb82500a'
            '97d920ebc556d9bed5828bd7c75df34aac122166b5e389f7a59fc5cb0dad8269'
            '353aae7cd9257a3528242e34ac4c7a69ea28de9116d6ce2f96891b0439efd0bc'
            '9fefd6fffc4e83540585b549a3a2ed3a44f571f06917dc85a5ee8ccdab97ceb3'
            '311c378658010bc1be94ce4a218a4cc0829782fe33a5085fc378599c601137b1')
arch=(any)
license=('GPL3')
_prefix="/usr"

prepare() {
# create c file for main
cython py_pbf_main.py --embed
}

build() {
_pyvers="$(python -V|awk '{print $2}'|cut -d "." -f 1-2)"
python setup.py build_ext --inplace
# maybe better add main also to setup.py
gcc -O2 -I/usr/include/python${_pyvers}m -o py_pbf_main py_pbf_main.c -lpython${_pyvers}m -lpthread -lm -lutil -ldl
}

package() {
_pyvers=$(python -V|awk '{print $2}' | awk -F "." '{print $1 $2}')
cd $srcdir
_arch=$(uname -m) # e.g. x86_64
_libc=$(gcc -dumpmachine | awk -F - '{print $(NF-1)"-"$(NF)}') # e.g. linux-gnu

_end="cpython-${_pyvers}m-$_arch-$_libc.so"
_files="py_pbf_gui_sub py_pbf_gui py_pbf_helper"

_libdir="$pkgdir/$_prefix/lib/${pkgname}"

for _file in $_files
  do
    install -D "${_file}"."${_end}" $_libdir/"${_file}"."${_end}"
done

# TODO: adjust path in .desktop and .sh file

install -D py_pbf_main $_libdir/py_pbf_main
install -D py_pbf_defconf_json.py $_libdir/py_pbf_defconf_json.py
install -Dm755 pacman_backup_files.sh $pkgdir/$_prefix/bin/pacman_backup_files

# .desktop and icons
install -Dm644 pacman_backup_files.desktop $pkgdir/usr/share/applications/pacman_backup_files.desktop
install -Dm644 pacman-icon-symbolic.svg $pkgdir/$_prefix/share/icons/pacman_backup_files/pacman-icon-symbolic.svg
install -Dm644 pacman-icon.png $pkgdir/$_prefix/share/icons/pacman_backup_files/pacman-icon.png

}
