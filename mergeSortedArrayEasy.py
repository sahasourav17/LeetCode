class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Naive approach
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()


# Time complexity : O((M+N)log (M+N)), Space Complexity :O (1).


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Two pointer based solution
        """
        i, j, k = m-1, n-1, m+n-1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# Time complexity: O(m+n) , Space Complexity: O(1)
