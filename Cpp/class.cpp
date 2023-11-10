#include <iostream>
#include <string>

using namespace std;

class Car {
    public:
        string brand;
        string model;
        int year;
        Car(string x,string y,int z){ //constructor 
            brand=x;
            model=y;
            year=z;
        }
};
class Animal {
    public:
    string animal;
    string name;
    int age;
    Animal(string x, string y, int z);

};

Animal::Animal(string x, string y, int z){
    animal=x;
    name=y;
    age=z;
}

int main()
{
    Car xuv("tesla","x",2020);
    Car sedan("jeep","y",2021);
    cout<<xuv.brand<<" "<<xuv.model<<" "<<xuv.year<<endl;
    cout<<sedan.brand<<" "<<sedan.model<<" "<<sedan.year<<endl;
    
    Animal cat("cat","Panki",3);
    Animal dog("dog","tippu",4);
    cout<<cat.animal<<" "<<cat.name<<" "<<cat.age<<endl;
    cout<<dog.animal<<" "<<dog.name<<" "<<dog.age<<endl;

    return 0;
}