function twoSum(nums: number[], target: number): number[] {
  const result: number[] = [0, 0];
  const numMap = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    let num: number = nums[i];
    if (numMap.has(target - num)) {
      result[0] = numMap.get(target - num)!;
      result[1] = i;
      return result;
    }
    numMap.set(num, i)
  }
  return result;
};
