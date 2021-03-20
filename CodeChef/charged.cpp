#include<iostream>
#include<conio.h>
using namespace std;
class electricity {
char name[20];
int unit;
float Rs;
public:
void get() {
cout<<"\nEnter the Name & Unit's of Electricity user: \n";
cin>>name>>unit;
}
void check() {
if(unit<=100) {
Rs=unit*0.40;
Rs=Rs+150;
}
else if(unit<=200||unit>100) {
Rs=unit*0.50;
Rs=Rs+150;
}
else if(unit<=300||unit>200) {
Rs=unit*0.60;
Rs=Rs+150;
}
}
void disp() {
if(Rs>=250) {
Rs=Rs+0.15;
}
cout<<name<<" \t"<<Rs<<endl;
}
};
int main() {
int n,i;
electricity e[10];
cout<<"\nHow many electricity User: \n";
cin>>n;
for(i=0;i<n;i++) {
e[i].get();
e[i].check();
}
cout<<"\nElectricity User's: \n";
cout<<"\nName\t Total cost(Rs)\n";
cout<<"=================================\n";
for(i=0;i<n;i++) {
e[i].disp();
}
getch();
}
