#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);

    long long x,n;
    cin>>x>>n;
    
    multiset<long long> parts;
    parts.insert(x);

    set<long long> lights;
    lights.insert(x);
    lights.insert(0);
    
    long long l,left,right;
    
    for(int i=0;i<n;i++){
        cin>>l;
        
        auto it = lights.lower_bound(l);
        right = *(it);
        left = *(--it);
        
        parts.erase(parts.find(right-left));
        parts.insert(right-l);
        parts.insert(l-left);
        
        cout<<*(--parts.end())<<" ";
        lights.insert(l);
    }

    cout<<"\n";


    return 0;
}