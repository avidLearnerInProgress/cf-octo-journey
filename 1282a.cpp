    #include<bits/stdc++.h>
    using namespace std;
     
    int main(){
        int T;
        cin>>T;
        while(T--){
        int start, end, c, r;
        cin>>start>>end>>c>>r;
        int L = max(min(start, end), c-r);
        int R = min(max(start, end), c+r);
        cout<<max(start,end) - min(start,end) - max(0, R-L)<<"\n";
        }
        return 0;
    }   