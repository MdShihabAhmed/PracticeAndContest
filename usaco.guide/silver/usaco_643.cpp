#include<bits/stdc++.h>

using namespace std;

int main(){
    freopen("diamond.in", "r", stdin);
    freopen("diamond.out", "w", stdout);
    int n, k;
    scanf("%d %d",&n,&k);
    
    int diamonds[n];
    for(int i=0;i<n;i++){
        scanf("%d",&diamonds[i]);
    }
    sort(diamonds,diamonds+n);
    
    int i=0,j=0;
    vector<int> results;
    results.push_back(0);
    results.push_back(0);
    int result = 0;
    int temp = 0;
    while(i<=j && j<n){
        if(diamonds[j]-diamonds[i]<=k){
            temp = j-i+1;
            j++;
        }
        else{
            results.push_back(temp);
            while(i<j && diamonds[j]-diamonds[i]>k){
                i++;
            }
        }
    }
    results.push_back(temp);
    sort(results.begin(),results.end(),greater<int>());
    result+=results[0];
    result+=results[1];
    printf("%d\n",result);
    return 0;
}