# 283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0: nums[i]=nums[j]
            i += 1
        nums[i:] = [0] * (len(nums)-i)

# 392. Is Subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: i += 1
            j += 1
        return i == len(s)

# 11. Container With most Water
class Solution(object):
    def maxArea(self, height):
        res = 0
        for i in range(len(height)-1):
            j = i+1
            while j < len(height):
                area = (j-i) * min(height[i], height[j])
                res = max(res, area)
                j += 1
        return res

# Method 2: Optimal solution
class Solution(object):
    def maxArea(self, height):
        res = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the current container area
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)
            
            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return res


# 1679. Max Number of K-Sum Pairs
# Method1 - My version: O(n^2), O(1)
class Solution(object):
    def maxOperations(self, nums, k):
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i] == None: continue
            j = i+1
            while j < len(nums):
                if nums[j]==None: 
                    j += 1
                    continue
                if nums[i] + nums[j] == k: 
                    cnt += 1
                    nums[i] = None
                    nums[j] = None
                    break
                j += 1
        return cnt
    
# Method2 - Two pointer - O(nlogn); O(1)
class Solution(object):
    def maxOperations(self, nums, k):
        cnt = 0
        i = 0
        j = len(nums)-1 
        nums.sort()
        while i < j:
            s = nums[i] + nums[j]
            if s == k: 
                cnt += 1
                i += 1
                j -= 1
            elif s < k:
                i += 1
            else: j -= 1
        return cnt

# Method3 - Hash map - O(n); O(n)
from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        dict = Counter(nums)
        cnt = 0
        for x in nums:
            y = k - x
            if dict[x] > 0 and dict[y] > 0:
                if x == y and dict(x) < 2: continue
                cnt += 1
                cnt[x] -= 1
                cnt[y] -= 1
        return cnt
                







