# LeetCode 14 - Longest Common Prefix

## Problem
Find the longest common prefix shared by all strings in the array.

## Approach
Take the first string as the initial prefix.
Compare it with each remaining string and shorten the prefix until it matches the beginning of the current string.

## Complexity
Time: O(n × m)
Space: O(1)
