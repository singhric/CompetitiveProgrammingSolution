#include <iostream>

using namespace std;

class complex
{
    int r, i;
public:
    void setdata();
    void putdata();
    complex sum(complex, complex);
};
void complex::setdata()
{
    cout << "Enter real & imaginary:" << endl;
    cin >> r >> i;
}
void complex::putdata()
{
    cout<<"Real part "<<r<<endl;
    cout<<"Imaginary part "<<i;
}
complex complex::sum(complex c1, complex c2)
{
	complex c3;
    c3.r=c1.r+c2.r;
    c3.i=c1.i+c2.i;
    return c3;
}

int main()
{
    complex c1, c2, c3;
    c1.setdata();
    c2.setdata();
    c3=c3.sum(c1, c2);
    c3.putdata();
}
