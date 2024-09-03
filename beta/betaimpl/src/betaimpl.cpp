#include <alpha/alpha.hpp>
#include <iostream>

// #if _MSC_VER
// 	__declspec(dllimport) void test();
// #endif

void	test()
{
	std::cout << greet() << std::endl;
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(hi)
{
    using namespace boost::python;
    def("hi", greet);
}