# Problem 15:Game of Thrones - I
# HackerRank Link:https://www.hackerrank.com/challenges/game-of-thrones/problem

#include <bits/stdc++.h>
using namespace std;

string gameOfThrones(string s) {
int freq[26] = {0};


for (char c : s) {
    freq[c - 'a']++;
}

int odd_count = 0;

for (int i = 0; i < 26; i++) {
    if (freq[i] % 2 != 0) {
        odd_count++;
    }
}

if (odd_count <= 1) {
    return "YES";
}

return "NO";


}

int main() {
string s;
cin >> s;


cout << gameOfThrones(s) << endl;

return 0;


}
