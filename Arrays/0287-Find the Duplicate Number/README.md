# LeetCode 287 - Find the Duplicate Number

## Problem
Given an array containing n + 1 integers where each integer is between 1 and n, find the duplicate number.

## Approach
Use Floyd's Cycle Detection algorithm.
Treat the array values as pointers and find the cycle.
The entrance of the cycle is the duplicate number.
# Learning
Learned how Floyd's Cycle Detection algorithm can be used to find a duplicate number without extra space.

## Complexity
Time: O(n)
Space: O(1)

