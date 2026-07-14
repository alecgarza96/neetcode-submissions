class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i in range(len(nums)):
            difference = target-nums[i]
            print(difference)
            if difference in sums:
                print("difference found")
                return [sums[target-nums[i]], i]
            
            sums[nums[i]] = i

            print(sums)
        
        return []
        