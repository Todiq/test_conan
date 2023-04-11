#include <alpha.hpp>

void alpha()
{
	typedef std::istream_iterator<int> in;

	std::cout << "Type in any number: ";
	std::for_each(
		in(std::cin), in(), std::cout
		<< (boost::lambda::_1 * 10)
		<< "\nType in another number: ");
	std::cout << "alpha" << std::endl;
}