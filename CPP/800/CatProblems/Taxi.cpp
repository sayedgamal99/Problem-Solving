#include <bits/stdc++.h>

using namespace std;
void start()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int main()
{
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n, answer = 0;
    cin >> n;
    int arr[n], fr[5] = {0};
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        fr[arr[i]]++;
    }
    // for (int i = 0; i < 5; i++)
    // {
    //     cout<<fr[i]<<" ";
    // }
    
    while (fr[3])
    {
        if (fr[1])
        {
            fr[3]--;
            fr[1]--;
            answer += 1;
        }
        else
        {
            fr[3]--;
            answer += 1;
        }
    }
    // cout<<answer<<endl;
    int twos = fr[2] / 2;
    // cout<<twos<<endl;
    answer += twos;
    if (fr[2] % 2 != 0)
        fr[1]+=2;
    int ones = fr[1]/4;
    answer+= ones;
    if(fr[1]%4!=0)
        answer+=1;
    answer+=fr[4];
    cout << answer;

    return 0;
}
