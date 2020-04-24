#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"
int main() {
    testAll();
    std::cout<<"Short test passed"<<std::endl;
    testAllExtended();
    std::cout << "Passed extended test" << std::endl;
    return 0;
}