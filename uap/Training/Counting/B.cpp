#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    int n;
    scanf("%d",&n);
    long long group1 = 1;
    for(int i=n;i>n/2;i--){
        group1*=i;//first permutation
    }
    group1/=(n/2);//for the rounds

    long long group2 = 1;
    for(int i=n/2;i>1;i--){
        group2*=i;//second permutation
    }
    group2/=(n/2);//for the rounds
    long long result = (group1*group2)/2;//removes the double repetition
    printf("%lld",result);
    
}