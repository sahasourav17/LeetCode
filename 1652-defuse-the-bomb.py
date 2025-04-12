class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code_len = len(code)
        ans = [0] * code_len
        # when k = 0
        if k == 0:
            return ans
        for i in range(code_len):
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    ans[i] += code[j % code_len]
            else:
                for j in range(i - abs(k), i):
                    ans[i] += code[(j + code_len) % code_len]
        return ans
