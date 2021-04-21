#include<stdio.h>
void swap(int*,int*);
int main()
{
	int a=10,b=20;
	printf("a = %d and b = %d\n",a,b);
	swap(&a,&b);	
}
	void swap(int *x,int *y)
{
int temp;
temp=*x;
*x=*y;
*y=temp;
printf("a = %d and b = %d\n",x,y);
}

