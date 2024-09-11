#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    scanf("%d",&t);
    long long n;
    while(t--){
        scanf("%lld",&n);
        long long temp = (1+sqrt(1+8*n))/2;
        
        printf("%lld\n",temp+(n-((temp*(temp-1))/2)));
    }
}