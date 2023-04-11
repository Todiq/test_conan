#include <beta/beta.hpp>
#include <beta1_1/beta1_1.hpp>

void beta1_1()
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
	alpha();
	std::cout << "beta1_1" << std::endl;
}