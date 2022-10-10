#include<iostream>
using namespace std;
int main(){

    string first = "Ritul";
    string last = "Singh";
    string fullname;
    // concatenation
    fullname = first + last;
    cout<<fullname<<endl;

    // reverse
    for(int i=first.size(); i>=0; i--){
        cout<<first[i]<<" ";
    }
    return 0;
}