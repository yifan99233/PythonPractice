class Solution:
    def fact(self, n):
        if n == 1:
            return 1
        else:
            return n * self.fact(n - 1)

    def trailingZeros(self, n):
        _fact = self.fact(n)
        print(_fact)
        _count = 0
        tmp_str = str(_fact)
        for i in reversed(tmp_str):
            if i == '0':
                _count += 1
            else:
                break
        return _count


if __name__ == '__main__':
    _sol = Solution()
    num = _sol.trailingZeros(105)
    print(num)