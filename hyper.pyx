# cimport numpy
# import numpy
# cimport cython
#

# cdef extern from "wrap.cpp" nogil:
#        double hypergeometric_pFq_w(const double* a, size_t na,
#                                  const double* b, size_t nb, double z)

cdef extern from "wrap.cpp" nogil:
    double hypergeometric_pFq_array(const double* a, size_t na,
                                    const double* b, size_t nb, const double* z, size_t nz,
                                    const double* res)

cpdef hypPfQ_np(double[:] a,
                double[:] b,
                double[:] z,
                double[:] r):
    cdef size_t na, nb, nz
    cdef const double* a_ptr
    cdef const double* b_ptr
    cdef double* r_ptr
    cdef const double* z_ptr

    # Initialize pointers and sizes
    na = a.shape[0]
    nb = b.shape[0]
    nz = z.shape[0]
    a_ptr = &a[0]
    b_ptr = &b[0]
    z_ptr = &z[0]
    r_ptr = &r[0]
    hypergeometric_pFq_w_array(a_ptr, na, b_ptr, nb, z_ptr,nz,r_ptr)

# def compute_hypergeometric_pFq(np.ndarray[np.double_t, ndim=1] a,
#                                np.ndarray[np.double_t, ndim=1] b,
#                                double z):
#
#         cdef const double* a_ptr = &a[0]
#         cdef const double* b_ptr = &b[0]
#         cdef size_t na = a.shape[0]
#         cdef size_t nb = b.shape[0]
#         return hypergeometric_pFq_w(a_ptr, na, b_ptr, nb, z)
#
# def compute_hypergeometric_pFq_loop(np.ndarray[np.float64_t, ndim=1] a,
#                                     np.ndarray[np.float64_t, ndim=1] b,
#                                     np.ndarray[np.float64_t, ndim=1] z,
#                                     np.ndarray[np.float64_t, ndim=1] r):
#     # Declare C-typed variables
#     cdef size_t i, na, nb, nz
#     cdef const double* a_ptr
#     cdef const double* b_ptr
#     cdef double elem_z
#
#     # Initialize pointers and sizes
#     na = a.shape[0]
#     nb = b.shape[0]
#     nz = z.shape[0]
#     a_ptr = &a[0]
#     b_ptr = &b[0]
#
#     # Ensure array contiguity and type correctness
#     # assert a.flags['C_CONTIGUOUS'] and a.dtype == np.float64
#     # assert b.flags['C_CONTIGUOUS'] and b.dtype == np.float64
#     # assert z.flags['C_CONTIGUOUS'] and z.dtype == np.float64
#
#     # Loop over z using Cython's nogil for efficiency
#     with nogil :
#         for i in range(nz):
#                 elem_z = z[i]
#                 r[i] =  hypergeometric_pFq_w(a_ptr, na, b_ptr, nb, elem_z)



