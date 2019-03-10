# cython: language_level=3

"""
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
"""

import py_pbf_gui
import argparse
import json
import py_pbf_defconf

def get_config(filename):
    '''
    load and return config
    @params: string
    '''
    try:
        with open(filename) as f:
            conf = json.loads(f.read())
        return(conf)
    except Exception as e:
        print(str(e))
        return(False)

def dump_config(config):
    '''
    print config
    @params: string
    '''
    try:
        print(json.dumps(config,indent=4,separators=(",",": ")))
    except Exception as e:
        print(str(e))

def create_args():
    parser = argparse.ArgumentParser()
    parser.prog = "pacman_backup_files" # set usage name to script wrapper
    parser.add_argument(
        "-c","--config-file",
        metavar="filename",
        help="specify config file to use")
    parser.add_argument(
        "-t", "--theme",
        metavar="themename",
        help="use this theme",
        default="default"
        )
    parser.add_argument(
        "-d", "--dump-config",
        metavar="filename",
        help="dump default config to stdout",
        const=True,
        action="store_const"
        )
    parser.add_argument(
        "--skip-root-check",
        help="skip root check, not recommended",
        const=True,
        action="store_const"
        )
    parser.add_argument(
        "--list-themes",
        help="list available themes",
        const=True,
        action="store_const"
        )

    return(parser.parse_args())

def main():
    args = create_args()    
    if args.skip_root_check != True and py_pbf_gui.os.getuid() == 0:
        print("dont start as root")
        exit(2)

    config = get_config(args.config_file) if args.config_file is not None else py_pbf_defconf.defconf
    if config is False:
        print("Error in config file %s" %args.config_file)
        exit(1)
    
    if args.dump_config is True: dump_config(config); exit(0)

    if args.list_themes is True :
        for i in config["gui"]["ttk_styles"].keys():
            print(i)
        exit(1)
    
    if args.theme != "default":
        tk_styles = [i for i in config["gui"]["tk_styles"].keys()]
        ttk_styles = [i for i in config["gui"]["ttk_styles"].keys()]
        if args.theme not in tk_styles or args.theme not in ttk_styles:
            print("%s not in 'tk_styles': %s and 'ttk_styles': %s" %(args.theme,tk_styles,ttk_styles) )
            exit(1)

    with py_pbf_gui.MainGui(config,args.theme) as main:
        main.run()

if __name__ == "__main__":
    main()
