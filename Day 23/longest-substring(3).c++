//https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char>se;
        int l=0,m=0;
        
        for(int i=0;i<s.length();i++){
            while(se.find(s[i])!=se.end()){
                se.erase(s[l]);
                l++;
            }
            se.insert(s[i]);
            m=max(m,i-l+1);
        }
        return m;
    }
};
