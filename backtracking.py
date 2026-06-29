# 17. Letter Combinations of a Phone Number

def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not digits: return []

    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    res = []

    def backtrack(comb, idx):
        if len(digits) == idx:
            res.append(comb)
            return
        for letter in phone_map[digits[idx]]:
            backtrack(comb+letter, idx+1)
    backtrack("", 0)
    return res


# 216. Combination Sum III
def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def bt(remaining, start, path):
            if remaining == 0 and len(path)==k: 
                res.append(path[:])
                return
            elif remaining < 0: return
            
            for i in range(start, 9):
                path.append(i+1)
                bt(remaining-i-1, i+1, path)
                path.pop()
        res = []
        bt(n, 0, [])
        return res       




















        