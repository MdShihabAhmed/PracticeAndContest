#include<bits/stdc++.h>

using namespace std;
const int N = 100000+10;
int a[N+10];
void solve(){
    int n, k;
    cin>>n>>k;
    // vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n-1;i++){
        int num = a[i];
        int current = 0;
        for(int j=2;j*j<=num;j++){
            while(num%j==0){
                num/=j;
                current++;
            }
            // num*=(long long)(pow(j,max(0,k-current)));
            
            if(current>=k) a[i]=a[i]%((long long)(pow(j,k)));
            current = 0;
        }
    }
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
    sort(a,a+n);
    long long result = 0;
    for(int i=0;i<n-1;i++){
        long long needed = 1;
        int current = 0;
        int num = a[i];
        for(int j=2;j*j<=num;j++){
            while(num%j==0){
                num/=j;
                current++;
            }
            needed*=((long long)(pow(j,max(0,k-current))));
            current=0;
        }
        result+=(upper_bound(a+i,a+n,needed)-lower_bound(a+i,a+n,needed));
    }
    cout<<result<<"\n";
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