#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
    public:
    string brand="Ford";
    void horn()
    {
        cout<<"Pee..pee\n";
    }
};

class Car : public Vehicle{
    public:
        string model="Mustang";
};

int main()
{
    Car abc;
    abc.horn();
    cout<<abc.brand<<" "<<abc.model<<endl;
    return 0;
}