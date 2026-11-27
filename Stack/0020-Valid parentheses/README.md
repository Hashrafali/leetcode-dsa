# LeetCode 20 - Valid Parentheses

## Problem
Given a string containing parentheses, determine if the brackets are valid.

A valid string must have matching opening and closing brackets in the correct order.

## Approach
Use a stack to store opening brackets.
When a closing bracket appears, check whether it matches the most recent opening bracket.
If it does not match, return False.
At the end, the stack must be empty.

## Complexity
Time: O(n)
Space: O(n)
