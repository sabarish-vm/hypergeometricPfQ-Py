#include <boost/math/special_functions/hypergeometric_pFq.hpp>
#include <vector>
#include <initializer_list>

inline void hypergeometric_pFq_array(const double* a, size_t na,
                                  const double* b, size_t nb, const double* z, size_t nz,
                                         double* res) {

    std::vector<double> aj,bj;
    if (na>0 && nb >0) {
       aj.assign(a, a + na);
       bj.assign(b, b + nb);
    }
    else if (na>0 && nb ==0) {
        aj.assign(a,a+na);
    }
    else if (na==0 && nb >0) {
        bj.assign(b,b+nb);
    }
    else if (na == 0 && nb ==0) {
    }
    for (size_t i=0; i<nz; i++) {
        *res = boost::math::hypergeometric_pFq(aj, bj, *z);
        res++;
        z++;
    }
}

inline double hypergeometric_pFq_double(const double* a, size_t na,
                                  const double* b, size_t nb, double z) {
    std::vector<double> aj(a, a + na);
    std::vector<double> bj(b, b + nb);

    // Call the Boost hypergeometric function with optional error as nullptr
    return boost::math::hypergeometric_pFq(aj, bj, z);
}
