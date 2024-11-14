#include<bits/stdc++.h>

using namespace std;

void solve(){
    
    int n,q,temp,index,size;
    cin>>n>>q;
    set<int> p;
    int needed = 0;
    for(int i=0;i<n;i++){
        cin>>temp;
        auto it = p.lower_bound(temp);
        p.insert(temp);
        size = i;
        index = distance(p.begin(), it);
        cout<<index<<"\n";
        needed+=max(0,(size-max((index-1),0)));
    }
    string s;
    cin>>s;
    cout<<needed<<"\n";
    cout<<s;
    vector<int> arr(n);

    for(int i=0;i<n;i++){
        if(s[i]=='L') arr[i]-=1;
        else arr[i]+=1;
    }
    for(int i=1;i<n;i++){
        arr[i]+=arr[i-1];
        if(arr[i]<0){
            arr[i-1]+=(arr[i]*-1);
            arr[i]=0;
        }
    }
    cout<<arr.size();
    cout<<"\n";
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
    for(int i=0;i<q;i++){
        cin>>temp;
    }
    cout<<"\n";
}

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);

    int t;
    cin>>t;
    while(t--){
        solve();
    }
    

    return 0;
}