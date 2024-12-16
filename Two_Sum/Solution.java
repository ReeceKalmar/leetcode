import java.util.HashMap;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    int[] result = new int[2];
    var numMap = new HashMap<Integer, Integer>();
    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      if (numMap.containsKey(target - num)) {
        result[0] = numMap.get(target - num);
        result[1] = i;
      }
      numMap.put(num, i);
    }
    return result;
  }
}
