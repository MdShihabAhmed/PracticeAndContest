#include<bits/stdc++.h>
using namespace std;
// grid = [[0 for i in range(1000+5)] for j in range(1000+5)]
const int MAXN = 1000+5;
string grid[MAXN][MAXN];

void check(int i,int j,int n,int m,string s){

    if (i<0 || j<0 || i>=n || j>=m)
        return;
    if (grid[i][j]=="?" || grid[i][j]=="x")
        return;

    if (grid[i][j]==s){
        grid[i][j]="x";
        check(i+1,j,n,m,"U");
        check(i-1,j,n,m,"D");
        check(i,j+1,n,m,"L");
        check(i,j-1,n,m,"R");
    }
}

void solve(){
    int n,m;
    cin>>n>>m;
    string s;

    for(int i=0;i<n;i++){
        cin>>s;
        for(int j=0;j<m;j++){
            grid[i][j] = s[j];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if ((i==0 && grid[i][j]=="U") || (i==n-1 && grid[i][j]=="D") || (j==0 && grid[i][j]=="L") || (j==m-1 and grid[i][j]=="R")){
                grid[i][j]="x";
                check(i+1,j,n,m,"U");
                check(i-1,j,n,m,"D");
                check(i,j+1,n,m,"L");
                check(i,j-1,n,m,"R");
            }
        }
    }
    

    
    int result = 0;
    int temp = 0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            
            if (grid[i][j]=="x")
                continue;
            temp = 0;
            if (i<n-1 && grid[i+1][j]!="x")
                temp+=1;
            if (i>0 && grid[i-1][j]!="x")
                temp+=1;
            if (j<m-1 && grid[i][j+1]!="x")
                temp+=1;
            if (j>0 && grid[i][j-1]!="x")
                temp+=1;
            if (temp)
                result+=1;
        }
    }
            
    cout<<result<<"\n";
    
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