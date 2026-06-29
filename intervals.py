# 435. Non-overlapping Intervals
def eraseOverlapIntervals(self, intervals):
    intervals.sort()
    remove = 0
    prev_end = intervals[0][1] # 2nd digit in first item 

    for start, end in intervals[1:]:
        if start < prev_end: # overlap
            remove += 1
            prev_end = min(prev_end, end) # keep interval ending earlier
        else: prev_end = end
    return remove

# 452. Minimum Number of Arrows to Burst Balloons
    # arrow_pos in overlapped range
def findMinArrowShots(self, points):
    res = 0
    arrow_pos = float("-inf")

    for s, e in sorted(points):
        if arrow_pos < s: 
            res += 1
            arrow_pos = e
        else:
            arrow_pos = min(arrow_pos, e) #shrinks the valid shooting region.
    return res

