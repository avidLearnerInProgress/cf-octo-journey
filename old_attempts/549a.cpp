#include<bits/stdc++.h>
using namespace std;
 
int main(){
    
    int i, j, n, m;
    cin>>n>>m;
    char vec[n][m];
    
    for(i=0; i<n; i++){
            cin>>vec[i];
    }
    int res = 0;
    for(int i=0; i<n-1; i++){
        for(int j=0; j<m-1; j++){
            string test = "";
            test += vec[i][j];
            test += vec[i+1][j+1];
            test += vec[i][j+1];
            test += vec[i+1][j];
            sort(test.begin(), test.end());
            if(test == "acef")
                res++;
        }
    }
    cout<<res<<"\n";
}