# 2390. Removing Stars From a String
class Solution(object):
    def removeStars(self, s):
        stk = []
        for i in range(len(s)):
            if s[i] == "*": stk.pop()
            else: stk.append(s[i])   
        return "".join(stk)

# 735. Asteroid Collision
class Solution(object):
    def asteroidCollision(self, asteroids):
        stk = []
        for a in asteroids:
            while stk and stk[-1]>0 and a<0:
                if abs(a) > stk[-1]:
                    stk.pop()
                    continue
                elif abs(a) == stk[-1]:
                    stk.pop()
                break
            else: stk.append(a) # while...else... works when did not break
        return stk

# 394. Decode String
class Solution(object):
    def decodeString(self, s):
        stk = []
        num = 0
        cur = ""
        for c in s:
            if c.isdigit(): num = num * 10 + int(c)
            elif c.isalpha(): cur += c
            elif c=="[": 
                stk.append((cur, num))
                cur=""
                num=0
            
            if stk and c=="]":
                prev, k = stk.pop()
                cur = prev + k * cur
        return cur
# Think: [ - to save states; ] - to build














