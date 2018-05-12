#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

// !!! Time Limit Exceeded
// class Solution {
// public:
//     bool isIsomorphic(string s, string t) {
//         vector<char> t_unique;
//         unique_copy(t.begin(), t.end(), back_inserter(t_unique));
//         for(auto c: t_unique){
//             vector<int> idx_t;
//             for(int i=0; i< int(t.size()); ++i){
//                 if(c == t[i])
//                     idx_t.push_back(i);
//             }

//             vector<int> idx_s;
//             char c_s = s[idx_t[0]];
//             for(int i=0; i< int(s.size()); ++i){
//                 if(c_s == s[i])
//                     idx_s.push_back(i);
//             }
//             if(idx_s.size() != idx_t.size() || idx_s != idx_t)
//                 return false;
//         }
//         return true;    
//     }
// };


// There are 256 ASCII characters. 
// This includes standard ASCII characters(0-127) and Extended ASCII characters(128-255)
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, vector<int>> d1;
        map<char, vector<int>> d2;
        for(int i=0; i<int(s.size()); ++i){
                d1[s[i]].push_back(i);
                d2[t[i]].push_back(i);   
        }
        vector<vector<int>> d1_vals;
        vector<vector<int>> d2_vals;
        for (auto const& element : d1) {
            d1_vals.push_back(element.second);
        }
        for (auto const& element : d2) {
            d2_vals.push_back(element.second);
        }
        sort(d1_vals.begin(), d1_vals.end());
        sort(d2_vals.begin(), d2_vals.end());
        return d1_vals == d2_vals;

    }
};


int main(){
    // string t("add");
    // vector<char> t_unique;
    // unique_copy(t.begin(), t.end(), back_inserter(t_unique));
    // cout << t << endl;
    // for(auto x: t_unique)
    //     cout << x << endl;

    Solution solver;
    cout << solver.isIsomorphic("egg", "add") << endl;
    cout << solver.isIsomorphic("foo", "bar") << endl;
    cout << solver.isIsomorphic("paper", "title") << endl;
    // map<char, vector<int>> d1;
    // d1['a'].push_back(1);
    // d1['a'].push_back(2);
    // cout << d1['a'][0] << endl;
    // cout << d1['a'].size() << endl;


}