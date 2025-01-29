from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np


BOOST_INCLUDE = "/opt/homebrew/include/"
ext_modules = [
    Extension(
        "hypPfQ",
        sources=["hyper.pyx", "wrap.cpp"],
        language="c++",
        extra_compile_args=[
            "-std=c++17",
            # "-L/opt/homebrew/lib",
            # "-lboost_system",
            # "-I/opt/homebrew/include",
        ],
        include_dirs=[np.get_include(), BOOST_INCLUDE],
    )
]

setup(
    name="hypPfQ-boost",
    ext_modules=cythonize(ext_modules, annotate=True, language_level=3),
)
