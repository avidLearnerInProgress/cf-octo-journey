#include <bits/stdc++.h>
using namespace std;
 
int main(){
    
    string s;
    cin>>s;
    set<string> st;
    
    for(int i=0; i<s.length(); i++){
        char x = s[s.length()-1];
        s.pop_back();
        string t = x + s;
        s = t;
        st.insert(s);
    }
    cout<<st.size();
}