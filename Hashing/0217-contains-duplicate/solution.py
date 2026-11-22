class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    duplicate = True
                    return True
        return duplicate
