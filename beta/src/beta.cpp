#include <alpha/talk.hpp>
#include <iostream>

#if (MSCV)
__declspec(dllimport) char const* greet();
#endif

int	main()
{
	std::cout << greet() << std::endl;

	return 0;
}