#include<bits/stdc++.h>

using namespace std;

const int MAX_N=1e6+5;

int prime[MAX_N];
void seive(){
    for(int i=0;i<MAX_N;i++) prime[i]=i;
    for(int i=2;i<MAX_N;i++){
        if(prime[i]==i){
            for(int j=i;j<MAX_N;j+=i) prime[j]=i;
        }
    }
    
}


void solve(){
    int n,x;
    cin>>n;
    map<int,multiset<int>> track;
    for(int i=0;i<n;i++){
        cin>>x;
        while(x>1){
            int temp = prime[x];
            track[temp].insert(0);
            track[temp].insert(0);
            int count = 0;
            while(x%temp==0){
                x/=temp;
                count++;
            }
            track[temp].insert(count);
        }
    }
    int result = 1;
    int temp1, temp2;
    for(auto &it:track){
        // cout<<it.first<<"\n";
        // for(auto x:it.second) cout<<x<<" ";
        // cout<<endl;
        auto last =(--it.second.end());
        temp1 = *last;
        temp2 = *(--last);
        // cout<<temp1<<" "<<temp2<<endl;
        result = max(result, (int)pow(it.first,min(temp1,temp2)));
    }
    cout<<result<<"\n";
    
}

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    seive();
    int t=1;
    // cin>>t;
    while(t--){
        solve();
    }
    

    return 0;
}