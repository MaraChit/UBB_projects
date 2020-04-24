#include<iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

int main()
{
	testAll();
	std::cout << "Short test passed!";
	std::cout << std::endl;
	testAllExtended();
	std::cout << "Extended test passed!" << std::endl;
	//system("pause");
	return 0;
	

}