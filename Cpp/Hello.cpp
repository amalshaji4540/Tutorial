#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
    string fname="Amal";
    string lname=" Shaji";
    string full_name;
    string full_n=fname+lname;

    full_name=fname.append(lname);
    cout<<full_n<<endl<<full_name;
    cout<<"\nlength of full name using size() function is "<<size(full_name);
    cout<<"\nLength of full name using length() function is "<<size(full_n)<<endl;

    cout<<full_name[0]<<endl;
    full_name[0]='B';
    cout<<full_name;
    cout<<max(10,29)<<endl;
    cout<<sqrt(64)<<endl;

    string result=(10<39)?"10 is less than 39":"10 is not less than 39";
    cout<<result;
    int a=0;
    while(a<5)
    {
        cout<<a;
        a++;
    }

    return 0;
}
