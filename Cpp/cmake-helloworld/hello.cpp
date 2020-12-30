#include <iostream>

template <class T>
class Interface; //prototype

template <class T, bool isExtended = std::is_base_of<Interface<T>, T>::value>
class Printer
{
    static_assert(isExtended, "T is not extended interface class");
};

class myclass1
{
  public:
    void print() { std::cout << "myclass1" << std::endl; }
};

class myclass2
{
  public:
    void print() { std::cout << "myclass2" << std::endl; }
};

template <typename T>
class Printer2
{
    T obj;

  public:
    void print()
    {
        obj.print();
    }
};

template <typename T, int num>
struct Point3d
{
    T x, y, z;
};

void printArray()
{
    Point3d<int, 3> points[]{
        {2, 3, -1},
        {2, 1, -4},
        {0, 2, 4},
    }; // 配列のリスト初期化
    //Point3d point = {2.5, 0.0, -1.0}; // 集成体クラスのリスト初期化

    for (auto p : points)
    {
        std::cout << p.x << std::endl;
    }
    //std::cout << point.x << ", " << point.y << ", " << point.z << std::endl;
}

int main()
{
    printArray();
}