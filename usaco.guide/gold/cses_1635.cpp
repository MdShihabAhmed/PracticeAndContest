#include<bits/stdc++.h>

using namespace std;

const int MOD=1e9+7;

void solve(){
    int n,x;
    cin>>n>>x;
    vector<int> c(n);
    for(int i=0;i<n;i++){
        cin>>c[i];
    }
    vector<long long> dp(x+1,0);
    dp[0] = 1;
    for(int i=1;i<=x;i++){
        for(int j=0;j<n;j++){
            if(i>=c[j]){
                dp[i]=(dp[i]+dp[i-c[j]])%MOD;
            }
        }
    }
    cout<<dp[x]<<"\n";
}

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    int t=1;
    // cin>>t;
    while(t--){
        solve();
    }
    

    return 0;
}