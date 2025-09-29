import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict); // để tra cứu nhanh
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true; // chuỗi rỗng
        
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break; // tìm được rồi, không cần kiểm tra nữa
                }
            }
        }
        
        return dp[s.length()];
    }
}
