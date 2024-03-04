#include<bits/stdc++.h>

using namespace std;

bool comp(const pair<long long, long long> &a, const pair<long long, long long> &b){
    if (a.first==b.first) return a.second>b.second;
    return a.first<b.first;
}

int main(){
    freopen("mountains.in", "r", stdin);
    freopen("mountains.out", "w", stdout);
    int n;
    scanf("%d",&n);
    
    pair<long long, long long> mountains[n];
    long long x, y;
    for(int i=0;i<n;i++){
        scanf("%lld %lld",&x, &y);
        mountains[i].first = x-y;
        mountains[i].second = x+y;
    }
    sort(mountains,mountains+n,comp);

    int result = n;
    int i=0,j=1;
    while(i<n && j<n){
        if(i==j) j++;
        else if(mountains[i].first<=mountains[j].first && mountains[i].second>=mountains[j].second){
            result-=1;
            j++;
        }
        else i++;
    }

    printf("%d\n",result);
    return 0;
}