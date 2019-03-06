from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["py_pbf_gui.py","py_pbf_helper.py","py_pbf_gui_sub.py"])
)    
