#include <vector>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <armadillo>
#include<cmath>
#include <chrono>



double eval_u(double x);
double eval_f(double x);
arma::vec thomas_alg(arma::vec g, arma::vec a, arma::vec b, arma::vec c, int npoints);
arma::vec thomas_alg_specific(arma::vec g, double a, double b, double c, int npoints);


int main ()
{
    
    arma::vec a;
    arma::vec b;
    arma::vec bt;
    arma::vec c;
    arma::vec v;
    arma::vec g;
    arma::vec g2;
    arma::vec gt;
    arma::vec x;
    arma::vec u;
    

    double a_vals;
    double c_vals;
    double b_vals;
    double startpoint;
    double startvalue;
    double endpoint;
    double endvalue;
    int npoints;
    double h;
    int precision;
    //double s_t1;
    //double s_t2;
    //double g_t1;
    //double g_t2;

    npoints = 1000; //including endpoints
    startpoint = 0.;
    startvalue = 0.;
    endpoint = 1.;
    endvalue = 0.;
    precision = 12;


    h = (endpoint-startpoint)/(npoints-1);

    //Initialize 
    a_vals = -1.;
    b_vals = 2.;
    c_vals = -1.;
    a = arma::vec(npoints-3).fill(a_vals); // if 10 tot points, 7 points, last index 6
    b = arma::vec(npoints-2).fill(b_vals); // if 10 tot points, 8 points, last index 7
    c = arma::vec(npoints-3).fill(c_vals); // if 10 tot points, 7 points, last index 6
    g = arma::vec(npoints-2).fill(0.);
    x = arma::vec(npoints).fill(0.);
    u = arma::vec(npoints).fill(0.);
    v = arma::vec(npoints).fill(0.);

    for (int i = 1; i < npoints-1; i++){
        // skips first and last point, as are known
        //x(i) = i;  
        x(i) = startpoint + (h * i); 
        u(i) = eval_u(x(i));
        g(i-1) = eval_f(x(i)) * std::pow(h,2.); 
    }
    std::cout << std::setprecision (12) << std::fixed; 
    //x.raw_print(std::cout, "x:");
    

    //Setting boundary values
    x(npoints-1) = endpoint;
    v(0) = 0;
    v(npoints-1) = 0;

    //Since start and endpoint are known, they are added to the first and last g
    //Altough in this case it is 0, it does nothing
    g(0) = g(0) + startvalue;
    g(npoints-3) = g(npoints-3) + endvalue;

    // Start measuring time
    auto s_t1 = std::chrono::high_resolution_clock::now();
    arma::vec v_spec_vals = thomas_alg_specific(g,a_vals,b_vals,c_vals,npoints);
    auto s_t2 = std::chrono::high_resolution_clock::now();
    double duration_s_seconds = std::chrono::duration<double>(s_t2 - s_t1).count();

    auto g_t1 = std::chrono::high_resolution_clock::now();
    arma::vec v_gen_vals = thomas_alg(g,a,b,c,npoints);
    auto g_t2 = std::chrono::high_resolution_clock::now();
    double duration_g_seconds = std::chrono::duration<double>(g_t2 - g_t1).count();



    std::string filename = "Prob7_v_gen" + std::to_string(npoints);
    v_gen_vals.save(filename, arma::csv_ascii);

    std::string filename2 = "Prob7_v_spec" + std::to_string(npoints);
    v_spec_vals.save(filename2, arma::csv_ascii);

    std::string filename3 = "Prob7_u" + std::to_string(npoints);
    u.save(filename3, arma::csv_ascii);

    std::string filename4 = "Prob7_x" + std::to_string(npoints);
    x.save(filename4, arma::csv_ascii);



    std::ofstream ofile5;
    int width = 12;    
    std::string filename5 = "Prob7_time" + std::to_string(npoints);
    ofile5.open(filename5);    
    ofile5 << std::setw(width) << std::setprecision(precision) << std::scientific << duration_g_seconds;
    ofile5 << std::setw(width) << std::setprecision(precision) << std::scientific << duration_s_seconds;
    ofile5.close();

    std::ofstream ofile;
    ofile.open(filename);    
    ofile << std::setw(width) << std::fixed << std::setprecision(precision) << std::scientific << x;
    ofile << std::setw(width) << std::fixed << std::setprecision(precision) << std::scientific << v_gen_vals;
    ofile.close();

    std::ofstream ofile2;
    ofile2.open(filename2);    
    ofile2 << std::setw(width) <<  std::setprecision(precision) << std::scientific << x;
    ofile2 << std::setw(width) <<  std::setprecision(precision) << std::scientific << v_spec_vals;
    ofile2.close();

    std::ofstream ofile3;
    std::string filename3 = "Prob7_u" + std::to_string(npoints);
    ofile3.open(filename3);    
    ofile3 << std::setw(width) << std::setprecision(precision) << std::scientific << x;
    ofile3 << std::setw(width) << std::setprecision(precision) << std::scientific << u;
    ofile3.close();

    return 0;
}

double eval_u(double x)
{
   return 1. - (1. - std::exp(-10.)) * x - std::exp(-10. * x);
}

double eval_f(double x)
{
    return 100 * std::exp((-10. * x));
}

arma::vec thomas_alg(arma::vec g, arma::vec a, arma::vec b, arma::vec c, int npoints)
{
    //Initialization
    arma::vec bt = arma::vec(npoints-2).fill(0.); 
    arma::vec gt = arma::vec(npoints-2).fill(0.); 
    arma::vec v = arma::vec(npoints).fill(0.); 

    bt(0) = b(0);
    gt(0) = g(0);
    //Forward substitution
    for (int i = 1; i < npoints - 2; i++){
        // if 10 tot, goes from 1 to 8

        //index a(i) as a(-i) since a(1) is the first value in vector
        bt(i) = b(i) - (a(i-1) * c(i - 1)/ bt(i-1)) ;
        gt(i) = g(i) - (a(i-1) / bt(i-1)) * gt(i - 1);
    }
    //Backward substitution
    v(npoints-2) = gt(npoints - 3) / bt(npoints - 3); // last unknown point
    
    for (int i = npoints - 3; i > 0; i--){
        // if 10 tot, goes from point 7 to 1
        v(i)= (gt(i-1) - c(i-1) * v(i + 1)) / (bt(i-1));

    }
    return v;
}

arma::vec thomas_alg_specific(arma::vec g, double a, double b, double c, int npoints)
{
    //Initialization
    arma::vec bt = arma::vec(npoints-2).fill(0.); 
    arma::vec gt = arma::vec(npoints-2).fill(0.); 
    arma::vec v = arma::vec(npoints).fill(0.); 

    bt(0) = b;
    gt(0) = g(0);
    double ac = a*c;
    //Forward substitution
    for (int i = 1; i < npoints - 2; i++){
        // if 10 tot, goes from 1 to 8

        //index a(i) as a(-i) since a(1) is the first value in vector
        bt(i) = b - ac / bt(i-1) ;
        gt(i) = g(i) - (a / bt(i-1)) * gt(i - 1);
    }
    //Backward substitution
    v(npoints-2) = gt(npoints - 3) / bt(npoints - 3); // last unknown point, if 10 tot, point 8
    //v(npoints-2) = 300;
    //std::cout << std::setprecision(12) << g;
    //std::cout << std::setprecision(12) << bt;
    
    for (int i = npoints - 3; i > 0; i--){
        // if 10 tot, goes from point 7 to 1
        v(i)= (gt(i-1) - c * v(i + 1)) / (bt(i-1));
        //std::cout << std::setprecision(12) << v;
        
    }
    //std::cout << std::setprecision(12) << v;
    return v;
}

