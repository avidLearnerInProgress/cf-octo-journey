#include<bits/stdc++.h>
using namespace std;

int main(){
	int i, j, k;
	int n,m;
	string s,t;
	map<string,string> mp;
	cin>>n>>m;

	for(i=0;i<n;i++){
        cin>>s>>t;
        t+=";";
        mp[t]=s;
    }
    for(i=0;i<m;i++){
        cin>>s>>t;
        cout<<s<<" "<<t<<" #"<<mp[t]<<endl;
    }
	return 0;
}