from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
from sysconfig import get_paths

paths = get_paths()
PYTHON_INCLUDE = paths["include"]
BOOST_INCLUDE = "/opt/homebrew/include/"

ext_modules = [
    Extension(
        "hypPfQ",
        sources=["./src/hyper.pyx", "./src/wrap.cpp"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        include_dirs=[np.get_include(), BOOST_INCLUDE, PYTHON_INCLUDE],
    )
]

setup(
    name="hypPfQ-boost",
    ext_modules=cythonize(ext_modules, annotate=True, language_level=3),
)
