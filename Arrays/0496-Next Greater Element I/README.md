# LeetCode 496 - Next Greater Element I

## Problem
For each element in nums1, find the first greater element to its right in nums2.

## Approach
Use a monotonic stack to find the next greater element for each number in nums2.
Store the result in a dictionary and use it to answer nums1.

## Complexity
Time: O(n + m)
Space: O(m)
