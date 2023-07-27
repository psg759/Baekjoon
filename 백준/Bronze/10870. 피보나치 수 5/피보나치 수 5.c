#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int fibonaci(int a, int b, int c) {
    int d;
    if(c == 1){
        return b;
    }else if (c == 0){
        return 0;
    }
    
    d = a + b;
    
    
    return fibonaci(b, d, c-1);
}

int main()
{
    int n;
    long long int res;
    
    scanf("%d", &n);
    
    res = fibonaci(0, 1, n);
    printf("%lld", res);
    
}
