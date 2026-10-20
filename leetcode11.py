class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height) - 1
        left = 0
        right = n
        band = 0
        max_area = 0
        while left < right:
            if height[left] >= height[right]:
                band = right - left
                max_area = max(max_area, min(height[right],height[left])*band)
                right -= 1
            else:
                band = right - left
                max_area = max(max_area, min(height[right],height[left])*band)
                left += 1
        return max_area

if __name__ == '__main__':
    try:
        user_input = input().split()
        height = list(map(int,user_input))
        sol = Solution()
        print(sol.maxArea(height))
    except: print("输入错误")



