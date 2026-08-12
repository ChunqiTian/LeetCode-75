# 643. Maximum Average Subarray I
class Solution(object):
    def findMaxAverage(self, nums, k):
        res = float('-inf')
        for i in range(len(nums)-k+1):
            total = sum(nums[i:i+k])
            res = max(res, total)
        return float(res) / k

# Method 2 - Optimal
class Solution(object):
    def findMaxAverage(self, nums, k):
        # 1. Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # 2. Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Add the incoming element, subtract the outgoing element
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
            
        # 3. Divide by k at the very end to get the average
        return float(max_sum) / k

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

# Method 2 - Optimal
class Solution(object):
    def maxVowels(self, s, k):
        # Using a set for O(1) fast lookups
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # 1. Count vowels in the very first window
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
                
        max_vowels = current_vowels
        
        # 2. Slide the window across the rest of the string
        for i in range(k, len(s)):
            # Add the character entering the window
            if s[i] in vowels:
                current_vowels += 1
            # Subtract the character leaving the window
            if s[i - k] in vowels:
                current_vowels -= 1
                
            # Track the maximum found so far
            max_vowels = max(max_vowels, current_vowels)
            
            # Optimization: If we hit the maximum possible vowels, return early
            if max_vowels == k:
                return k
                
        return max_vowels

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








