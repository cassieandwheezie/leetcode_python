'''LeetCode 88 - Merge Sorted Array
 Difficulty: Easy
 Hint- Use 3 pointers

Compare last valid elements of nums1 and nums2

Put the larger one at the end

Move pointers

Stop when nums2 finishes

If nums2 still has elements → copy them

Important - indexing start with 0.So. pointer 1 is initialised as m-1 as m is the total length.
Similarly check the initializations of the other poiters two 

'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pointer1 = m - 1
        pointer2 = n - 1
        pointer3 = m + n - 1

        while pointer2 >= 0:
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[pointer3] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
            pointer3 -= 1
