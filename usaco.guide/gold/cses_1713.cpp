#include<bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
	cin.tie(NULL);

    int x,n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>x;
        int j;
        int result = 1;
        for(j=2;j*j<=x;j++){
            int temp = 1;
            while(x%j==0){
                x/=j;
                temp+=1;
            }
            result*=temp;
        }
        if(x>1) result*=2;
        cout<<result<<"\n";
    }
    

    return 0;
}