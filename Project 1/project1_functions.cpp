#include <vector>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <armadillo>


double eval_u(double x);

double eval_u(double x)
{
   return 1. - (1. - std::exp(-10.)) * x - std::exp(-10. * x);

}
