#include <iostream>

int f(int a)
{
    auto m = a + 3;
    return m;
}

int main()
{
    std::cout << "Hello m=" << f(20) << std::endl;
    return 0;
}
