# Problem 13:Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#include <bits/stdc++.h>

using namespace std;

string isValid(string s) {
    int freq[26] = {0}; 
    for (char c : s) { 
        freq[c - 'a']++; 
    } 
    map<int, int> counts; 
    for (int i = 0; i < 26; i++) { 
        if (freq[i] > 0) { 
            counts[freq[i]]++; 
        } 
    } 
    if (counts.size() == 1) {
         return "YES"; 
    } 
    if (counts.size() != 2) { 
        return "NO"; 
    } 
    
    auto it = counts.begin(); 
    int f1 = it->first; 
    int c1 = it->second; 
    it++; int f2 = it->first; 
    int c2 = it->second; 
    if ((f1 == 1 && c1 == 1) || (f2 == 1 && c2 == 1)) { 
        return "YES"; 
    } 
    if (f2 == f1 + 1 && c2 == 1) { 
        return "YES"; 
    } 
        
    return "NO";

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = isValid(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
