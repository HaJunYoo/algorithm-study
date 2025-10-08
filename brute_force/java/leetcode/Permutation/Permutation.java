import java.util.*;

import java.util.List;
import java.util.ArrayList;

public class Permutation {
    public static void main(String[] args) {
        Solution sol = new Solution();
        // Test cases here
        System.out.println(sol.permute(new int[] { 1, 2, 3 }));
    }
}
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        backtrack(nums, path, result);
        return result;
    }
    private void backtrack(int[] nums, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }
        for (int num : nums) {
            if (path.contains(num)) {
                continue;
            }
            path.add(num);
            backtrack(nums, path, result);
            path.remove(path.size() - 1);
        }
    }

}
