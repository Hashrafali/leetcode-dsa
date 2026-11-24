# LeetCode 3411 - Maximum Subarray With Equal Products

## Problem
Find the longest subarray whose product of all elements is equal to the LCM multiplied by the GCD of all elements.

## Approach
Check every possible subarray.
For each subarray, calculate the product, GCD, and LCM.
If product == GCD * LCM, update the maximum length.

## Complexity
Time: O(n²)
Space: O(1)
