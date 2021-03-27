#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int prime(int x)
{
    int n, i, flag = 0;
    for (i = 2; i <= sqrt(x); i++)
    {
        if (x % i == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        return (1);
    else
        return (-1);
}

int main()
{
    int i, j, sum, sum1, check;
    long long int t;
    scanf("%d", &t);
    long long int x[t], y[t];
    for (i = 0; i < t; i++)
        scanf("%lld%lld", &x[i], &y[i]);
    for (i = 0; i < t; i++)
    {
        sum = 0;
        sum = sum + x[i] + y[i];
        for (j = 1; j < 10; j++)
        {
            sum1 = 0;
            sum1 = sum + j;
            //printf("%d",sum1);
            check = prime(sum1);
            //printf("%d\n",check);
            if (check == 1)
            {
                printf("%d\n", j);
                break;
            }
            else
                continue;
        }
    }
    return 0;
}