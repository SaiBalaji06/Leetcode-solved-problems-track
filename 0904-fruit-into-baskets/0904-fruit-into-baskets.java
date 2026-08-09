class Solution {
    public int totalFruit(int[] fruits) {
        int n = fruits.length;
        Map<Integer, Integer> hm = new HashMap<>();
        int uni = 0;

        int i = 0;
        int j = 0;
        int mx = 0;
        while (j < n) {
            if (uni <= 2) {
                if (!hm.containsKey(fruits[j])) {
                    hm.put(fruits[j], 1);
                    uni += 1;
                } else {
                    hm.put(fruits[j], hm.get(fruits[j]) + 1);
                }
                if (uni <= 2) {
                    mx = Math.max(mx, j - i + 1);
                }
                j += 1;
            } else {
                hm.put(fruits[i], hm.get(fruits[i]) - 1);
                if (hm.get(fruits[i]) == 0) {
                    hm.remove(fruits[i]);
                    uni -= 1;
                }
                i += 1;
            }
        }
        return mx;
    }
}