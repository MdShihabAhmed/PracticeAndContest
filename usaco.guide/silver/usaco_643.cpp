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
    
    int dia[n];
    int i=0,j=0;
    dia[j]=1;
    while(i<=j && j<n){


        if (j+1<n && diamonds[j+1]-diamonds[i]<=k){
            j+=1;
            dia[j]=(j-i+1);

        }
        else{
            i+=1;
            if(j<i){
                j=i;
                dia[j]=1;
            }
        }
    }

    i=1,j=i;
    int result= 0;
    int temp = dia[0];
    while(i<=j && j<n){
        if (j+1<n && diamonds[j+1]-diamonds[i]<=k){
            j+=1;
            result = max(result,temp+(j-i+1));
        }
        else{
            temp = max(temp,dia[i]);
            i+=1;
            if(j<i){
                j=i;
            }
        }
    }
    cout<< result <<"\n";
    return 0;
}