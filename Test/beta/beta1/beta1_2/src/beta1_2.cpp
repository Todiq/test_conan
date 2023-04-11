#include <alpha/alpha_include/alpha.hpp>
#include <beta/beta.hpp>
#include <beta1_1/beta1_1.hpp>
#include <beta1_2/beta1_2.hpp>

void beta1_2()
{
	beta1_1();
	alpha();
	std::cout << "beta1_2" << std::endl;
}