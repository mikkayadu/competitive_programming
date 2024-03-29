class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        max_Area = 0
        while l<r:
            width = r - l
            myheight = min(height[l], height[r])
            area = width * myheight
            max_Area = area if area > max_Area else max_Area

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_Area