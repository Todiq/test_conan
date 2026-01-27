#include <alpha/alpha.hpp>

#include <functional>

struct same : std::binary_function<int, int, bool>
{
    bool operator()(int a, int b) const { return a == b; }
};

int main(int argc, char* argv[])
{
    return 0;
}