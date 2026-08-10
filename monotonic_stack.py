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


# Method 2
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

# 901. Online Stock Span

class StockSpanner:

    def __init__(self):
        # The stack will store tuples of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Each day initially has a span of at least 1 (itself)
        span = 1
        
        # Pop elements from the stack while the top price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        # Push the current price and its calculated span onto the stack
        self.stack.append((price, span))
        
        return span

