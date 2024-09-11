#include<bits/stdc++.h>

using namespace std;

int main(){
    int n,w;
    scanf("%d %d",&n,&w);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }

    int minn=0,maxx=0,temp=0;
    for(int i=0;i<n;i++){
        temp+=a[i];
        minn = min(minn,temp);//minimum number of people present in the bus before start
        maxx = max(maxx,temp);//maximum number of people that can get in the bus until end
    }
    //total possible ways=w+1
    //minn is the lower range, maxx is the upper range
    //excluding that range is the possible result
    // if maxx and minn range overlaps, the result is 0
    printf("%d",max(((w+1)-(maxx+abs(minn))),0));
    return 0;
}