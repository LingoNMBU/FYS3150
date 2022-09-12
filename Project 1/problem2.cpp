#include <vector>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <armadillo>


double eval_u(double x)
{
   return 1. - (1. - std::exp(-10.)) * x - std::exp(-10. * x);
}

int main ()
{
// declarations
arma::vec x;
arma::vec u;
double step;
double end;
double start;
int npoints;
int i;
double eval_u(double x);
std::ofstream ofile;
int precision;
std::string filename = "function_values";


ofile.open(filename);

start = 0.;
end = 1.;
npoints = 100;
step = (end-start)/npoints;
precision = 6;
x = arma::vec(npoints);
u = arma::vec(npoints);


for (int i = 0; i < npoints; i++){
    x(i) = start + i*step;
    u(i) = eval_u(x(i));
    std::cout << x(i);
    std::cout << u(i);
}

ofile << std::setprecision(precision) << std::scientific << x;
ofile << std::setprecision(precision) << std::scientific << u;

return 0;
}