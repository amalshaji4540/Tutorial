#include <iostream>
#include <string>

using namespace std;

int main()
{
    int num_array[5]={1,2,3,4,5};
    for (int i:num_array)
    {
        if(i==3)
        {
            continue;;
        }
        cout<<i<<endl;
    }
    return 0;
}