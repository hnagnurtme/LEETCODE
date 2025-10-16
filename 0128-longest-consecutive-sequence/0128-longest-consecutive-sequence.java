import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Map<Integer, Boolean> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, false);
        }

        int result = 0;

        for (int num : nums) {
            if (map.get(num)) continue; 
            map.put(num, true);

            int val = 1;
            int next = num + 1;
            while (map.containsKey(next)) {
                map.put(next, true);
                val++;
                next++;
            }

            int prev = num - 1;
            while (map.containsKey(prev)) {
                map.put(prev, true);
                val++;
                prev--;
            }

            result = Math.max(result, val);
        }

        return result;
    }
}
