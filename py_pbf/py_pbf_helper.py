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

import os
import subprocess
import threading
import re
import ctypes
import functools

def is_readable(f):
    try:
        return(os.access(f,os.R_OK))
    except Exception as e:
        return(str(e))

def get_current_environment():
    '''
    return current environemnt
    '''
    libc = ctypes.CDLL(None)
    environ = ctypes.POINTER(ctypes.c_char_p).in_dll(libc, 'environ')
    return(
        {i[0]:i[1] for i in (i.decode().split("=") for i in iter(functools.partial(next, iter(environ)), None))}
    )

class Match:
    '''
    either checks for number in ending (return True of False) or strips number and . from file ending
    @params: string, string 
    '''
    def __init__(self,f,ending):
        self.f = f
        self.ending = ending
        return

    def check_ending(self):
        return(True if re.search(self.ending+"\.[$\d].*?",self.f) else False)

    def strip_ending(self):
        return(re.sub(self.ending+".[$\d].*","",self.f))

class GetFiles(threading.Thread):
    '''
    search directory and return files with given ending
    @params: string, string, bool
    '''
    files = None
    def setup(self,directory,ending,gen):
        self.d = directory
        self.e = ending
        self.gen = gen

    def run(self):
        if self.gen:
            self.files = (dirpath+"/"+i for dirpath,dirnames,filenames in os.walk(self.d,self.e) for i in filenames if self.e in i)
        else:
            self.files = [dirpath+"/"+i for dirpath,dirnames,filenames in os.walk(self.d,self.e) for i in filenames if self.e in i]

    def get_files(self):
        return(self.run())

    def get_result(self):
        return(self.files)

    def stop(self):
        del self

    def __exit__(self,t,val,tb):
        #del self.d, self.e, self.files, self.gen
        return(self.stop())

class RunCmdSimple:
    '''
    run simple shell command
    @params: list or string, bool
    '''
    def __init__(self,cmd,piped=False):
        if isinstance(cmd,list):
            self.cmd = cmd
        elif isinstance(cmd,str):
            self.cmd = cmd.split(" ")
        else:
            print("%s neither string nor list" %(type(self.cmd)))
            raise(ValueError)
        self.piped = piped

    def __enter__(self):
        self.res = subprocess.run(self.cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE) if self.piped else subprocess.run(self.cmd)
        return(self)

    def __exit__(self,t,val,tb):
        del self.cmd, self.res

class RunThCmdSimple(threading.Thread):
    '''
    run simple shell command threaded
    @params: list or string, bool
    '''
    res = None
    def setup(self,cmd,piped=False):
        if isinstance(cmd,list):
            self.cmd = cmd
        elif isinstance(cmd,str):
            self.cmd = cmd.split(" ")
        else:
            print("%s neither string nor list" %(type(self.cmd)))
            raise(ValueError)
        self.piped = piped

    def run(self):
        self.res = subprocess.run(self.cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE) if self.piped else subprocess.run(self.cmd)

    def get_result(self):
        return(self.res)

    def stop(self):
        del self

    def __exit__(self,t,val,tb):
        return(self.stop())
