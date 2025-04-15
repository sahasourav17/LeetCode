class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        arr_len = len(arr)
        ans = 0
        for i in range(0, arr_len - 1, 1):
            for j in range(i + 1, arr_len, 1):
                for k in range(j + 1, arr_len, 1):
                    # print(f"i => {i}: j => {j} : k => {k}")
                    if (
                        abs(arr[i] - arr[j]) <= a
                        and abs(arr[j] - arr[k]) <= b
                        and abs(arr[k] - arr[i]) <= c
                    ):
                        ans += 1
        return ans
