#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long int factorial(long long int a) {
    if(a == 1 || a == 0){
        return 1;
    }
    else {
        return a * factorial(a-1);
    }
    
}

int main() {
    long long int n;
    
    long long int res;
    
    scanf("%lld", &n);
    
    res = factorial(n);
    printf("%lld", res);
    
}