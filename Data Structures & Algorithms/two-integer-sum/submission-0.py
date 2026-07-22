class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_l = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    new_l.append(i)
                    new_l.append(j)
                    break
        return new_l