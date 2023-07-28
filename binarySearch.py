class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        for n in nums:
            mid = floor((high+low)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid
            elif target < nums[mid]:
                high = mid
        return -1
