#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    string s = "hello", ss;
    cin >> ss;
    string res = "";
    for (int i = 0; i < 5; i++)
    {
        for (int ii = i; ii < ss.size(); ii++)
        {
            if (ss[ii] == s[i])
            {
                res += ss[ii];
                i++;
            }
        }
    }
    (res == s) ? cout << "YES" << endl : cout << "NO" << endl;
    return 0;
}
