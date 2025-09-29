class Solution {
    public boolean containsDuplicate(int[] nums) {
         Map<Integer, Integer> m = new HashMap<>();
        for (int num : nums) {
            if (m.containsKey(num)) {
                return true;
            }
            m.put(num, 1);
        }
        return false;
    }
}