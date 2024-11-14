#include<bits/stdc++.h>

int main(){
    
    long long result = 0;
    int n;
    std::cin>>n;
    while(n){
        result = 0;
        for(int i=1;i<=n;i++){
            result+=(i*i);
        }
        std::cout<<result<<"\n";
        std::cin>>n;

    }   
    return 0;
}