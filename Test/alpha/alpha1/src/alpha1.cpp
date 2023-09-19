#include <Alpha/alpha1/alpha1.hpp>
#include <Alpha/alpha.hpp>
#include <cstring>
#include <zlib.h>

void	alpha1()
{
	const unsigned char pData[] = { "Hello" };
	unsigned long nDataSize = 100;

	printf("Initial size: %d\n", nDataSize);

	unsigned long nCompressedDataSize = nDataSize;
	unsigned char * pCompressedData = new unsigned char[nCompressedDataSize];

	int nResult = compress2(pCompressedData, &nCompressedDataSize, pData, nDataSize, 9);

	if (nResult == Z_OK)
	{
		printf("Compressed size: %d\n", nCompressedDataSize);

		unsigned char * pUncompressedData = new unsigned char[nDataSize];
		nResult = uncompress(pUncompressedData, &nDataSize, pCompressedData, nCompressedDataSize);
		if (nResult == Z_OK)
		{
			printf("Uncompressed size: %d\n", nDataSize);
			if (memcmp(pUncompressedData, pData, nDataSize) == 0)
				printf("Great Success\n");
		}
		delete [] pUncompressedData;
	}
	delete [] pCompressedData;
	std::cout << "alpha1" << std::endl;
}