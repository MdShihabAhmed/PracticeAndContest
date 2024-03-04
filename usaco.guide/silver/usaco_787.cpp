#include<bits/stdc++.h>

using namespace std;
bool comp(const pair<int,int> &a, const pair<int,int> &b){
    return (a.first>b.first);
}

int main(){
    freopen("rental.in", "r", stdin);
    freopen("rental.out", "w", stdout);
    int n, m, r;
    scanf("%d %d %d",&n,&m,&r);
    
    int cow[n];
    for(int i=0;i<n;i++){
        scanf("%d",&cow[i]);
    }
    sort(cow,cow+n,greater<int>());

    pair<int, int> store[m+1];
    for(int i=0;i<m;i++){
        scanf("%d %d",&store[i].second, &store[i].first);
    }
    sort(store,store+m,greater<pair<int,int>>());

    int neighbors[r];
    for(int i=0;i<r;i++){
        scanf("%d",&neighbors[i]);
    }
    sort(neighbors,neighbors+r,greater<int>());

    long long result = 0;
    int i=0,j=0,k=0;
    for(i=0;i<n;){
        long long temp = 0;
        int tempJ = 0,tempMilk = cow[i];
        while(j+tempJ<m){
            if(tempMilk>=store[j+tempJ].second){
                temp += (store[j+tempJ].second)*store[j+tempJ].first;
                tempMilk -= store[j+tempJ].second;
                tempJ++;
            }
            else{
                temp += (tempMilk)*store[j+tempJ].first;
                break;
            }
        }
        if(temp>=neighbors[k]){
            result+=temp;
            j+=tempJ;
            if (j<m) store[j].second-=tempMilk;
            i++;
        }
        else{
            result+=neighbors[k];
            k++;
            n--;
        }
    }

    printf("%lld\n",result);
    return 0;
}