============
Installation
============

The wrapper needs the `BOOST <https://www.boost.org/>`_ library in the system, and ``Python.h`` file for compilation. 
Depending on the shell-setup the paths to these libraries may already be known to the compiler. 

.. code-block:: shell

       python setup.py build_ext --inplace -v -f

If the compilation is successfull you can proceed to installing the package using,

.. code-block:: shell

    pip install -e .

In case the compilation throws an error saying that ``Python.h`` or ``boost/math/special_functions/hypergeometric_pFq.hpp``
is not found. There are two ways of handling this,

#. Add the paths to these libraries to the variables ``PYTHON_INCLUDE`` or ``BOOST_INCLUDE`` in the ``setup.py`` file.
#. Add the paths to the env variable CPLUS_INCLUDE_PATH
