#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n ;
        cin>>n;
        int x;
        map<int,int>themap;
        for (int i = 0; i < n; i++)
        {
            cin>>x;
            themap[x]++;
        }
        int most_common=0 ;
        for(auto &[x,y]:themap){
            most_common=max(most_common,y);
        }
        int ans = 0,d = 0;
        while(most_common<n){
            d = min(most_common,n-most_common);
            ans += d + 1;
            most_common+=d;
        }

        cout<<ans<<"\n";
        
    }
}