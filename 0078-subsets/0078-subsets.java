class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        res = new ArrayList<>();
        res.add(new ArrayList<>());
        for(int i=0; i<n; i++) {
            addNumToList(nums[i]);
        }
        return res;
    }
    
    public void addNumToList(int n) {
        int size = res.size();
        for(int i=0; i<size; i++) {
            List<Integer> temp = new ArrayList<>(res.get(i));
            temp.add(n);
            res.add(temp);
        }
    }
}