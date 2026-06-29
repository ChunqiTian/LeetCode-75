# 374. Guess Number Higher or Lower
def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    
    while left <=right:
        mid = (left + right) // 2
        num = guess(mid)
        if num == 0: return mid
        elif num == 1: 
            left = mid + 1
        else:
            right = mid - 1


# 2300. Successful Pairs of Spells and Potions
def successfulPairs(self, spells, potions, success):
    potions.sort()
    n = len(potions)

    def lower_bound(target): # find the first idx where value >= target
        left = 0
        right = n - 1
        while left <= right:
            mid = (right + left) // 2
           
            if potions[mid] >= target: 
                ans = mid
                right = mid - 1
            else: left = mid + 1
        return ans
    
    res = []

    for spell in range(spells):
        need = (success + spell - 1) // spell

        idx = lower_bound(need)
        res.append(n-idx)

    return res

# 162. Find Peak Element
# Ask for any peak
def findPeakElement(self, nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left+right) // 2
        if nums[mid] < nums[mid+1]: # going up, highly likely going down on the right side
            left = mid + 1
        else: right = mid 

    return left # where left == right


# 875. Koko Eating Bananas
def minEatingSpeed(self, piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid

        if hours <= h: right = mid
        else: left = mid + 1
    return left # left == right




