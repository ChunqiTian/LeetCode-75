# 2215. Find the Difference of Two Arrays
class Solution(object):
    def findDifference(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1-s2), list(s2-s1)]

# 1207. Unique Number of Occurrences
# method 1
class Solution(object):
    def uniqueOccurrences(self, arr):
        dict = {}
        for i in arr:
            dict[i] = dict.get(i, 0) + 1
        seen = set()
        for value in dict.values():
            if value in seen:
                return False
            else:
                seen.add(value)
        return True
# method 2
class Solution(object):
    def uniqueOccurrences(self, arr):
        dict = {}
        for a in arr:
            dict[a] = dict.get(a, 0) + 1
        unique = set(list(dict.values()))
        return len(dict) == len(unique)
    
# 1657. Determine if Two Strings Are Close
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1)!=set(word2): return False
        dict1 = {}
        dict2 = {}
        for i in word1:
            dict1[i] = dict1.get(i, 0) + 1
        for i in word2:
            dict2[i] = dict2.get(i, 0) + 1
        lst1 = sorted(dict1.values())
        lst2 = sorted(dict2.values())
        return lst1 == lst2

# 2352. Equal Row and Column Pairs
class Solution(object):
    def equalPairs(self, grid):
        res = 0
        row_count = {}
        for row in grid:
            key = tuple(row)
            row_count[key] = row_count.get(key, 0) + 1
        for j in range(len(grid)):
            col = tuple(grid[i][j] for i in range(len(grid)))
            if col in row_count:
                res += row_count[col]
        return res


