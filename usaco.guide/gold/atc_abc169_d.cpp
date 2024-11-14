#include<bits/stdc++.h>

using namespace std;

void solve(){
    int n, k;
    cin>>n>>k;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int result = 0;
    for(int i=0;i<n-1;i++){
        int num = a[i];
        for(int j=2;j*j<=num;j++){
            
            while(num%j==0){
                num/=j;
            }
            a[i]=a[i]%((long long)(pow(j,k)));
        }
    }
    sort(a.begin(),a.end());
    
    for(int i=0;i<n-1;i++){
        int needed = 1;
        int current = 0;
        int num = a[i];
        for(int j=2;j*j<=num;j++){
            
            while(num%j==0){
                num/=j;
            }
            a[i]=a[i]%((long long)(pow(j,k)));
        }
    }

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