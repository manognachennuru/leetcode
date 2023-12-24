class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        res = new ArrayList<>();
        res.add(new ArrayList<>());
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: nums) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        for(int key : map.keySet()) {
            add(key, map.get(key));
        }
        return res;
    }
    
    public void add(int n, int count) {
        int size = res.size();
        for(int i=0; i<size; i++) {
            List<Integer> curr = res.get(i);
            List<Integer> temp = new ArrayList<>(curr);
            for(int j=0; j<count; j++) {
                temp.add(n);
                List<Integer> next = new ArrayList<>(temp);
                res.add(next);
            }
        }
    }
}