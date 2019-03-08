#### pacman_backup_files
##### Small utitlity to show pacnew and pacsave files

first download PKGBUILD from repository, e.g.
```
wget https://raw.githubusercontent.com/vetzki/pacman_backup_files/master/PKGBUILD
```
then, build and install pkg with:
```
makepkg -ci
```
Arguments:
```
-h, --help            show this help message and exit
-c filename, --config-file filename     specify config file to use
-t themename, --theme themename     use this theme
-d, --dump-config     dump default config to stdout
--skip-root-check     skip root check, not recommended
--list-themes         list available themes
```
<details><summary>default config file in json format:</summary>
<pre>
{
    "path": "/etc",
    "editor": "kate",
    "terminal": "xterm",
    "terminal_execute_flag": "-e",
    "terminal_edit_cmd": "sudoedit",
    "gui": {
        "#_comment_sizes": "sizes are always [width, height]",
        "window_icon": "/usr/share/icons/pacman_backup_files/pacman-icon.png",
        "path_line_width": 20,
        "editor_line_width": 10,
        "file_line_width": 18,
        "#_comment_styles": "always use same ids for different themes (e.g. 'dark' in tk_styles and 'dark' in ttk_styles)",
        "tk_styles": {
            "default": {
                "text": {
                    "font": ["DejaVu Sans", 11],
                    "background": "#ffffff",
                    "foreground": "#000000",
                    "text_sizes": [80, 28],
                    "selectbackground": "#ff0033",
                    "selectforeground": "#ffffff"
                },
                "listbox": {
                    "font": ["DejaVu Sans", 12],
                    "background": "#ffffff",
                    "foreground": "#000000",
                    "listbox_sizes": [60, 10],
                    "padx": 5,
                    "pady": 5,
                    "selectbackground": "#ff0033",
                    "selectforeground": "#ffffff"
                }
            },
            "dark": {
                "text": {
                    "font": ["DejaVu Sans", 11],
                    "background": "#000000",
                    "foreground": "#ffffff",
                    "text_sizes": [80, 28],
                    "selectbackground": "#ff0033",
                    "selectforeground": "#000000"
                },
                "listbox": {
                    "font": ["DejaVu Sans", 12],
                    "background": "#000000",
                    "foreground": "#ffffff",
                    "listbox_sizes": [60, 10],
                    "padx": 5,
                    "pady": 5,
                    "selectbackground": "#ff0033",
                    "selectforeground": "#000000"
                }
            }
        },
        "ttk_styles": {
            "default": {
                ".": {
                    "configure": {
                        "font": ["TkDefaultFont", 12],
                        "background": "#d9d9d9",
                        "foreground": "#000000",
                        "selectbackground": "#ff0033",
                        "selectforeground": "#ffffff",
                        "focuscolor": "#ff0033",
                        "indicatordiameter": "10",
                        "troughcolor": "#999999",
                        "insertwidth": 1,
                        "selectborderwidth": 1,
                        "borderwidth": 1
                    }
                },
                "mainframe.TFrame": {
                    "configure": {
                        "background": "#ffffff",
                        "padding": [0, 0],
                        "relief": "flat"
                    }
                },
                "TFrame": {
                    "configure": {
                        "background": "#ffffff",
                        "padding": [0, 0],
                        "relief": "flat"
                    }
                },
                "TButton": {
                    "configure": {
                        "font": ["DejaVu Sans", 13],
                        "background": "#ffffff",
                        "foreground": "#000000",
                        "padding": [5, 5],
                        "relief": "flat"
                    },
                    "map": {
                        "foreground": [
                            ["pressed", "#ffffff"],
                            ["active", "#000000"],
                            ["selected", "#ffffff"]
                        ],
                        "background": [
                            ["pressed", "focus", "#ff0033"],
                            ["active", "#ff0033"]
                        ]
                    }
                },
                "TEntry": {
                    "configure": {
                        "font": ["DejaVu Sans", 11],
                        "background": "#ffffff",
                        "foreground": "#000000",
                        "padding": [5, 5],
                        "relief": "flat"
                    }
                },
                "TLabel": {
                    "configure": {
                        "font": ["DejaVu Sans", 11, "bold"],
                        "background": "#ffffff",
                        "foreground": "#000000",
                        "padding": [10, 10],
                        "relief": "flat"
                    }
                },
                "TScrollbar": {
                    "configure": {
                        "background": "#ffffff",
                        "foreground": "#000000",
                        "arrowcolor": "#000000",
                        "padding": [0, 0],
                        "relief": "flat"
                    },
                    "map": {
                        "background": [
                            ["disabled", "#ffffff"]
                        ],
                        "arrowcolor": [
                            ["disabled", "#c9c9c9"]
                        ]
                    }
                },
                "Horizontal.TProgressbar": {
                    "configure": {
                        "background": "#ff0033",
                        "troughcolor": "#000000",
                        "bordercolor": "#ff0033",
                        "padding": [2, 2],
                        "relief": "flat"
                    }
                },
                "TCheckbutton": {
                    "configure": {
                        "font": ["DejaVu Sans", 12],
                        "background": "#ffffff",
                        "foreground": "#000000",
                        "padding": [2, 2],
                        "relief": "flat"
                    },
                    "map": {
                        "foreground": [
                            ["pressed", "#ffffff"],
                            ["active", "#000000"],
                            ["selected", "#ff0033"]
                        ],
                        "background": [
                            ["pressed", "focus", "#ff0033"],
                            ["active", "#ff0033"]
                        ],
                        "indicatorcolor": [
                            ["selected", "#ff0033"],
                            ["pressed", "#000000"]
                        ]
                    }
                },
                "progress.TLabel": {
                    "configure": {
                        "font": ["DejaVu Sans", 11],
                        "background": "#ffffff",
                        "foreground": "#000000",
                        "padding": [2, 2],
                        "relief": "flat"
                    }
                }
            },
            "dark": {
                ".": {
                    "configure": {
                        "font": ["TkDefaultFont", 12],
                        "background": "#d9d9d9",
                        "foreground": "#ffffff",
                        "selectbackground": "#ff0033",
                        "selectforeground": "#000000",
                        "focuscolor": "#ff0033",
                        "indicatordiameter": "10",
                        "troughcolor": "#d9d9d9",
                        "insertwidth": 1,
                        "selectborderwidth": 1,
                        "borderwidth": 1
                    }
                },
                "mainframe.TFrame": {
                    "configure": {
                        "background": "#000000",
                        "padding": [0, 0],
                        "relief": "flat"
                    }
                },
                "TFrame": {
                    "configure": {
                        "background": "#000000",
                        "padding": [0, 0],
                        "relief": "flat"
                    }
                },
                "TButton": {
                    "configure": {
                        "font": ["DejaVu Sans", 13],
                        "background": "#000000",
                        "foreground": "#ffffff",
                        "padding": [5, 5],
                        "relief": "flat"
                    },
                    "map": {
                        "foreground": [
                            ["pressed", "#000000"],
                            ["active", "#ffffff"],
                            ["selected", "#000000"]
                        ],
                        "background": [
                            ["pressed", "focus", "#ff0033"],
                            ["active", "#ff0033"]
                        ]
                    }
                },
                "TEntry": {
                    "configure": {
                        "font": ["DejaVu Sans", 11],
                        "background": "#000000",
                        "foreground": "#ffffff",
                        "fieldbackground": "#000000",
                        "insertcolor": "#ffffff",
                        "padding": [5, 5],
                        "relief": "flat"
                    }
                },
                "TLabel": {
                    "configure": {
                        "font": ["DejaVu Sans", 11, "bold"],
                        "background": "#000000",
                        "foreground": "#ffffff",
                        "padding": [10, 10],
                        "relief": "flat"
                    }
                },
                "TScrollbar": {
                    "configure": {
                        "background": "#000000",
                        "foreground": "#ffffff",
                        "arrowcolor": "#ffffff",
                        "padding": [0, 0],
                        "relief": "flat"
                    },
                    "map": {
                        "background": [
                            ["disabled", "#000000"]
                        ],
                        "arrowcolor": [
                            ["disabled", "#adadad"]
                        ]
                    }
                },
                "Horizontal.TProgressbar": {
                    "configure": {
                        "background": "#ff0033",
                        "troughcolor": "#ffffff",
                        "bordercolor": "#ff0033",
                        "padding": [2, 2],
                        "relief": "flat"
                    }
                },
                "TCheckbutton": {
                    "configure": {
                        "font": ["DejaVu Sans", 12],
                        "background": "#000000",
                        "foreground": "#ffffff",
                        "padding": [2, 2],
                        "relief": "flat"
                    },
                    "map": {
                        "foreground": [
                            ["pressed", "#000000"],
                            ["active", "#ffffff"],
                            ["selected", "#ff0033"]
                        ],
                        "background": [
                            ["pressed", "focus", "#ff0033"],
                            ["active", "#ff0033"]
                        ],
                        "indicatorcolor": [
                            ["selected", "#ff0033"],
                            ["pressed", "#ffffff"]
                        ]
                    }
                },
                "progress.TLabel": {
                    "configure": {
                        "font": ["DejaVu Sans", 11],
                        "background": "#000000",
                        "foreground": "#ffffff",
                        "padding": [2, 2],
                        "relief": "flat"
                    }
                }
            }
        }
    }
}
</pre>
</details>

<details><summary>PKGBUILD</summary><pre>
pkgver=1
pkgrel=1
pkgname="pacman_backup_files"
pkgdesc="show pacnew and pacsave files"
depends=('python')
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
install -D py_pbf/py_pbf_defconf_json.py $_libdir/py_pbf_defconf_json.py

# resources
# TODO: adjust path in .desktop and .sh file
install -Dm755 resources/pacman_backup_files.sh $pkgdir/$_prefix/bin/pacman_backup_files
# .desktop and icons
install -Dm644 resources/pacman_backup_files.desktop $pkgdir/usr/share/applications/pacman_backup_files.desktop
install -Dm644 resources/pacman-icon-symbolic.svg $pkgdir/$_prefix/share/icons/pacman_backup_files/pacman-icon-symbolic.svg
install -Dm644 resources/pacman-icon.png $pkgdir/$_prefix/share/icons/pacman_backup_files/pacman-icon.png

}
</pre></details>

#### Credits
<div>Icons made by <a href="https://www.flaticon.com/authors/icomoon" title="Icomoon">Icomoon</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

#### License

pacman_backup_files: show pacnew and pacsave files
Copyright (C) 2019 Vetter Michael

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
