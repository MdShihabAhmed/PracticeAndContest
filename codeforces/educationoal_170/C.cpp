#include<bits/stdc++.h>

using namespace std;

void solve(){
    
    int n,k,temp;
    cin>>n>>k;

    map<int,int> a;
    for(int i=0;i<n;i++){
        cin>>temp;
        a[temp]+=1;
    }

    vector<int> arr;
    vector<int> value;
    int arrS = 0;
    for(auto it:a){
        arrS+=1;
        arr.push_back(it.first);
        value.push_back(it.second);
    }

    int result = 0;
    temp=0;
    int start = 0;
    for(int i=0;i<arrS;i++){
        temp+=(value[i]);
        if(i-start+1>k){
            temp-=value[start];
            start+=1;
        }
        if((i>0 && arr[i]-arr[i-1]!=1)){
            temp-=value[i];
            result = max(result, temp);
            temp = value[i];
            start = i;
        }
        result = max(result, temp);
        
    }
    result = max(result, temp);
   
    cout<<result<<"\n";
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