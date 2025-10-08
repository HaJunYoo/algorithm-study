import java.util.*;

import java.util.ArrayList;
import java.util.List;

public class Combination {
    public static void main(String[] args) {
        Solution sol = new Solution();
        // Test cases here
        System.out.println(sol.combine(4, 2));
    }
}

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        backtrack(n, k, 1, path, result);
        return result;
    }

    private void backtrack(int n, int k, int start, List<Integer> path, List<List<Integer>> result) {
        if (path.size() == k) {
            result.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i <= n; i++) {
            path.add(i);
            backtrack(n, k, i + 1, path, result);
            path.remove(path.size() - 1);
        }
    }

}
