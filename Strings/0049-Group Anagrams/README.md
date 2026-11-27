# LeetCode 49 - Group Anagrams

## Problem
Group strings that are anagrams of each other.

## Approach
Sort each string and use the sorted string as a key in a dictionary.
Strings with the same sorted characters belong to the same group.

## Complexity
Time: O(n × k log k)
Space: O(n × k)
