# Problem 12:Making Anagrams
# HackerRank Link:https://www.hackerrank.com/challenges/making-anagrams/problem

#include <bits/stdc++.h>

using namespace std;

int makingAnagrams(string s1, string s2) {
    int freq[26] = {0}; 
    for (char c : s1) { 
        freq[c - 'a']++; } 
        for (char c : s2) {
             freq[c - 'a']--; 
        } 
        int deletions = 0; 
        for (int i = 0; i < 26; i++) { 
            deletions += abs(freq[i]); 
        
        } 
        
        return deletions;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = makingAnagrams(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
