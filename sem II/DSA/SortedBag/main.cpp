#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"
using namespace std;

int main()
{
	testAll();
	cout << "Done short.\n";
	testAllExtended();
	cout << "Done extended.\n";
	return 0;
}
