class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n < 3:
            return []
        
        nums.sort()  # 排序是双指针和去重的前提
        res = []
        for i in range(0,n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 去重：右指针向左跳过重复元素
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else: left += 1
        return res

if __name__ == '__main__':
    data = input().split()
    nums = list(map(int,data))
    sol = Solution()
    print(sol.threeSum(nums))
