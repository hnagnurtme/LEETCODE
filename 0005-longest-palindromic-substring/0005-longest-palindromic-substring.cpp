class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        int start = 0, maxLen = 1;
        
        auto expand = [&](int left, int right) {
            while (left >= 0 && right < s.size() && s[left] == s[right]) {
                if (right - left + 1 > maxLen) {
                    start = left;
                    maxLen = right - left + 1;
                }
                left--;
                right++;
            }
        };
        
        for (int i = 0; i < s.size(); i++) {
            expand(i, i);     // palindrome lẻ
            expand(i, i + 1); // palindrome chẵn
        }
        
        return s.substr(start, maxLen);
    }
};
