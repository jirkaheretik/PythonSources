"""
2461. Maximum Sum of Distinct Subarrays With Length K
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
"""

class Solution(object):
    # Copy of Java algorithm, used dictionary here to store frequencies.
    # runs 133ms, beats 55.2%
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxSum = 0
        frequencies = dict()
        kSum = 0
        kLength = 0
        numDuplicates = 0
        for idx in range(len(nums)):
            # add a new element:
            num = nums[idx]
            kSum += num
            kLength += 1
            freq = frequencies.get(num, 0)
            if freq == 1:
                numDuplicates += 1
            frequencies[num] = freq + 1
            # remove element (if needed):
            if kLength > k:
                # remove element at index-k
                num = nums[idx - k]
                kSum -= num
                kLength -= 1
                freq = frequencies[num] # should be there, no need for .get()
                if freq == 2:
                    numDuplicates -= 1
                frequencies[num] = freq - 1
            # check our sum and conditions:
            if kSum > maxSum and numDuplicates == 0 and kLength == k:
                maxSum = kSum
        return maxSum
