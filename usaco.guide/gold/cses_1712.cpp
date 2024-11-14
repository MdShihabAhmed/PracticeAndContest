#include<bits/stdc++.h>

using namespace std;
long long MOD = 1000000000+7;

long long binpow(long long a, long long b, long long mod){
    long long result = 1;
    while(b>0){
        if (b&1) result=(result*a)%mod;
        a = (a*a)%mod;
        b>>=1;
    }
    return result;
}

void solve(){
    long long a,b,c;
    cin>>a>>b>>c;
    
    cout<<binpow(a,binpow(b,c,MOD-1),MOD)<<"\n";
    
}

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);

    int t=1;
    cin>>t;
    while(t--){
        solve();
    }
    

    return 0;
}