#include <stdio.h>
#include <string.h>
#include <math.h>
int main()
{
    int t, i, x, y;
    char s1[102], s2[102];
    scanf("%d", &t);
    while (t--)
    {
        i = 0;
        x = 0;
        y = 0;
        scanf("%s", &s1);
        scanf("%s", &s2);
        while (s1[i]){
            if(s1[i]=='?' || s2[i]=='?')
            x++;
            else if (s1[i] != s2[i])
            y++;
            i++;
        }
        printf("%d %d\n", y, x + y);
    }
    return 0;
}
