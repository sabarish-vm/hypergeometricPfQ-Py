.. image:: https://github.com/sabarish-vm/hypergeometricPfQ-Py/actions/workflows/test.yml/badge.svg?branch=main
  :target: https://github.com/sabarish-vm/hypergeometricPfQ-Py/actions

============
Installation
============

The wrapper needs the `BOOST <https://www.boost.org/>`_ library in the system, and ``Python.h`` file for compilation. 
Depending on the shell-setup the paths to these libraries may already be known to the compiler. 
It is most often easier to install BOOST using `conda-forge <https://anaconda.org/conda-forge/boost>`_. 
``Python.h`` is available by default if you have python installed.
``setup.py`` will try to localte this file during the compilation.


.. code-block:: shell

    pip install -e .

If the installation fails, you can debug it by running, this shows the compilation output

.. code-block:: shell

       python setup.py build_ext --inplace -v -f

In case the compilation throws an error saying that ``Python.h`` or ``boost/math/special_functions/hypergeometric_pFq.hpp``
is not found. There are two ways of handling this,

#. Add the paths to these libraries to the variables ``PYTHON_INCLUDE`` or ``BOOST_INCLUDE`` in the ``setup.py`` file.
#. Add the paths to the env variable CPLUS_INCLUDE_PATH

================
Installing Boost
================
Boost can be installed system wide using the OS's package management system. An OS-independent solution is to install it via `homebrew <https://formulae.brew.sh/formula/boost>`_ 

.. code-block:: shell

       brew install boost

or `conda-forge <https://anaconda.org/conda-forge/boost>`_. 

.. code-block:: shell

       conda install -c conda-forge boost
