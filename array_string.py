# 1768. Merge Strings Alternately
class Solution(object):
    def mergeAlternatively(self, word1, word2):
        res = []
        minLen = min(len(word1), len(word2))

        for i in range(minLen):
            res.append(word1[i])
            res.append(word2[i])

        res.extend(word1[minLen:])
        res.extend(word2[minLen:])
        return "".join(res)
    

# 1071. Greatest Common Divisor of Strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1: return ""
        if str1 == str2: return str1
        if len(str1) > len(str2): return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])
    
# 1431. Kids With the Greatest Number of Candies
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies): res.append(True)
            else: res.append(False)
        return res

    # return [candy + extraCanadies >= max(candies) for candy in candies]


# 605. Can Place Flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        while n > 0:
            for i in range(len(flowerbed)):
                if flowerbed[i] == 0 and (flowerbed[i-1]==0 or i==0) and (flowerbed[i+1]==0 or i==len(flowerbed)-1): 
                    flowerbed[i]=1
                    n-=1
                    break
            else: return False # runs only if the loop did not break
            if n == 0: return True
        return True

# Method 2
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            left = (i == 0 or flowerbed[i-1] == 0)
            right = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return n <= 0


# 345. Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        v = []
        v_idx = []
        res = list(s)
        for i in range(len(s)):
            if s[i] in ["aeiouAEIOU"]:
                v.append(s[i])
                v_idx.append(i)
        for idx in v_idx: 
                res[idx]=v.pop()       
        return "".join(res)

# 151. Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        res = s.split()
        return " ".join(res[::-1])
            
# 238. Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j: continue
                prod = prod * nums[j]
            res.append(prod)
        return res

# 334. Increasing Triplet Subsequence
class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3: return False

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] < nums[k]: return True
        return False
                               
# 443. String Compression
class Solution(object):
    def compress(self, chars):
        write = 0
        i = 0 

        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            chars[write] = chars[i]
            write += 1

            if j - i > 1:
                for c in str(j-i):
                    chars[write] = c
                    write += 1
            i = j
        return write
    
