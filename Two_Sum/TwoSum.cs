public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        int[] result = new int[2];
        var numMap = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int num = nums[i];
            if (numMap.ContainsKey(target - num))
            {
                result[0] = numMap[target - num];
                result[1] = i;
                return result;
            }
            numMap[num] = i;
        }
        return result;
    }
}
