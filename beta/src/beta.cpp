#include <alpha/alpha.hpp>
#include <zlib.h>
#include <stdio.h>
#include <string.h>

// #if _MSC_VER
// 	__declspec(dllimport) void test();
// #endif

int	main()
{
	test();
	const unsigned char pData[] = { "test2" };
	unsigned long nDataSize = 100;

	printf("Initial size: %d\n", nDataSize);

	unsigned long nCompressedDataSize = nDataSize;
	unsigned char * pCompressedData = new unsigned char[nCompressedDataSize];

	int nResult = compress2(pCompressedData, &nCompressedDataSize, pData, nDataSize, 9);
	return 0;
}