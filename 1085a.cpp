#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    string s, dummy;
    cin >> s;
    int lim, len;
    if(s.size()%2==0)
    {
        len = s.size();
        lim = len/2;
        for(int i=0; i<lim; i++)
        {
            dummy += s[len-i-1];
            dummy += s[i];
        }
    }
    else
    {
        len = s.size();
        lim = len/2;
        for(int i=0; i<lim; i++)
        {
            dummy += s[i];
            dummy += s[len-i-1];
        }
        dummy += s[lim];
    }
    reverse(dummy.begin(), dummy.end());
    cout << dummy << "\n";
    return 0;
}