# 933. Number of Recent Calls
from collections import deque
class RecentCounter(object):
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q and self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

# 649. Dota2 Senate
    # order matters, the first senate can ban the next opponent
class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        R = deque()
        D = deque()
        for i,c in enumerate(senate):
            if c=="R": R.append(i)
            else: D.append(i)
        while R and D:
            r = R.popleft()
            d = D.popleft()
            if r < d: R.append(r+n) # one senator is removed (loser), winner re-enters future rounds
            else: D.append(d+n)
        return "Radiant" if R else "Dire"





