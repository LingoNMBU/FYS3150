#include <vector>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <armadillo>
#include<cmath> 



double eval_u(double x);
double eval_f(double x);
arma::vec thomas_alg(arma::vec g, arma::vec a, arma::vec b, arma::vec c, int npoints);


int main ()
{
    
arma::vec a;
arma::vec b;
arma::vec bt;
arma::vec c;
arma::vec v;
arma::vec g;
arma::vec gt;
arma::vec x;

double startpoint;
double startvalue;
double endpoint;
double endvalue;
int npoints;
double h;

npoints = 10;
startpoint = 0.;
startvalue = 0.;
endpoint = 1.;
endvalue = 0.;

h = (endpoint-startpoint)/npoints;

//Initialize 
a = arma::vec(npoints-3).fill(-1.);
b = arma::vec(npoints-2).fill(2);
bt = arma::vec(npoints-2).fill(2);
c = arma::vec(npoints-3).fill(-1.);
g = arma::vec(npoints-2);
gt = arma::vec(npoints-2);
x = arma::vec(npoints);
v = arma::vec(npoints);

for (int i = 0; i < npoints-2; i++){
    x(i) = startpoint + h * i;
    g(i) = eval_f(x(i)) * std::pow(h,2);
}

//Since start and endpoint are known, they are added to the first and last g
//Altough in this case it is 0, it does nothing
g(0) = g(0) + startvalue;
g(npoints-2) = g(npoints-2) + endvalue;

v = thomas_alg(g,a,b,c,npoints);

}


double eval_u(double x)
{
   return 1. - (1. - std::exp(-10.)) * x - std::exp(-10. * x);
}

double eval_f(double x)
{
    return 100* std::exp(-10. * x);
}

arma::vec thomas_alg(arma::vec g, arma::vec a, arma::vec b, arma::vec c, int npoints)
{
    //Initialization
    arma::vec bt = arma::vec(npoints - 2);
    arma::vec gt = arma::vec(npoints - 2);
    arma::vec v = arma::vec(npoints - 2);

    double bt_1 = b(1);
    double gt_1 = g(1);
    //Forward substitution
    for (int i = 2; i < npoints - 1; i++){
        bt(i) = (a(i) / bt(i-1)) * c(i - 1);
        gt(i) = (a(i) / g(i-1))  * c(i - 1);
    }
    //Backward substitution
    v(npoints-1) = g(npoints - 1) / bt(npoints - 1);
    for (int i = npoints - 2; i > 1; i--){
        v(i)= (gt(i) - c(i) * v(i + 1)) / (bt(i));
    }
    return v;

return 0;
}

