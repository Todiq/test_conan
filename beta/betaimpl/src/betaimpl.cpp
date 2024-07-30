#include <alpha/alpha.hpp>
#include <beta/betaimpl/betaimpl.hpp>
#include <iostream>

// #if _MSC_VER
// 	__declspec(dllimport) void test();
// #endif

void	test()
{
	traverse_dom_trees(nullptr);
	std::cout << "Testing" << std::endl;
}