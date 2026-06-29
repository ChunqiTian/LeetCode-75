# 739. Daily Temperatures
def dailyTemperatures(self, t):
    res = []
    for i in range(len(t)):
        cnt = 0
        found = False
        for j in range(i+1, len(t)):
            cnt += 1
            if t[i] < t[j]:
               res.append(cnt)
               break
        if not found: res.append(0)
            
    return res


# 739. Daily Temperatures
def dailyTemperatures(self, temperatures):
    n = len(temperatures)

    res = [0] * n
    stack = []

    for i in range(n):

        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev

        stack.append(i)

    return res


