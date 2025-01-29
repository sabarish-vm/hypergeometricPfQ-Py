from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np


BOOST_INCLUDE = ""
PYTHON_INCLUDE = ""
ext_modules = [
    Extension(
        "hypPfQ",
        sources=["hyper.pyx", "wrap.cpp"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        include_dirs=[np.get_include(), BOOST_INCLUDE, PYTHON_INCLUDE],
    )
]

setup(
    name="hypPfQ-boost",
    ext_modules=cythonize(ext_modules, annotate=True, language_level=3),
)
