# 643. Maximum Average Subarray I
class Solution(object):
    def findMaxAverage(self, nums, k):
        res = float('-inf')
        for i in range(len(nums)-k+1):
            total = sum(nums[i:i+k])
            res = max(res, total)
        return float(res) / k

# 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution(object):
    def maxVowels(self, s, k):
        res = 0
        vowel = "aeiou"
        for i in range(len(s)-k+1):
            cnt = 0
            for j in range(i, i+k):
                if s[j] in vowel: cnt += 1
            res = max(res, cnt)
        return res

# 1004. Max Consecutive Ones III
class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        res = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0: zeros += 1
            while zeros > k:
                if nums[left] == 0: zeros -= 1
                left += 1
            res = max(res, right-left+1)
        return res
        
# 1493. Longest Subarray of 1's After Deleting One Element
class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        res = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0: zeros += 1
            while zeros > 1:
                if nums[left] == 0: zeros -= 1
                left += 1
            res = max(res, right-left)
        return res








