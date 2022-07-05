class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> check = new HashSet<Integer>();
        for (int num : nums) {
            check.add(num);
        }

        int longestStreak = 0;

        for (int num : check) {
            if (!check.contains(num-1)) {
                int currentNum = num;
                int currentStreak = 1;
                while (check.contains(currentNum+1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}