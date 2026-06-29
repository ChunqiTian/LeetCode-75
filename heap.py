# 215. Kth Largest Element in an Array
import heapq
def findKthLargest(self, nums, k):
    heap = nums[:k] # use as a slicing window
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]: heap.heappushpop(heap, num)
            # pushes a new element onto the heap and simultaneously removes and returns the smallest element
    return heap[0]

# 2336. Smallest Number in Infinite Set
# Heap only keeps the addBack numbers.
# The infinite set tracked by the pointer cur.
import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.cur = 1 # next smallest num 
        self.heap = [] # only for add back nums
        self.seen = set() # track what's inside the heap, so we don't insert duplicates
        
    def popSmallest(self):
        """
        :rtype: int
        """
        if self.heap and self.heap[0] < self.cur:
            res = heapq.heappop(self.heap)
            self.seen.remove(res)
            return res
        
        res = self.cur
        self.cur += 1
        return res
        
    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.cur and num not in self.seen: 
            self.seen.add(num)
            heapq.heappush(self.heap, num)
        
# 2542. Maximum Subsequence Score
import heapq
def maxScore(self, nums1, nums2, k):
    pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1]) # [(a1,b1), (a2,b2)...] sorted by nums2 descending order
    total = 0
    res = 0
    heap = []

    for n1, n2 in pairs:
        heapq.heappush(heap, n1)
        total += n1

        if len(heap) > k: total -= heapq.heappop(heap)
        if len(heap) == k: res = max(res, total * n2)
    return res


# 2462. Total Cost to Hire K Workers
import heapq

def totalCost(self, costs, k, candidates):
    
    if len(costs) <= 2 * candidates:
        heapq.heapify(costs)
        return sum(heapq.heappop(costs) for _ in range(k))
    
    n = len(costs)
    left = 0
    right = n - 1
    heap = []
    res = 0

    for _ in range(candidates):
        heapq.heappush(heap, (costs[left], 0)) # mark 0 for left
        left += 1

    for _ in range(candidates):
        heapq.heappush(heap, (costs[right], 1)) # mark 1 for right
        right -= 1

    for _ in range(k):
        cost, side = heapq.heappop(heap)
        res += cost

        if left <= right:
            if side == 0: 
                heapq.heappush(heap, (costs[left], 0))
                left += 1
            else:
                heapq.heappush(heap, (costs[right], 1))
                right -= 1
    return res



