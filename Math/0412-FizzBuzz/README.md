# LeetCode 412 - Fizz Buzz

## Problem
Given an integer n, return a string array containing the numbers from 1 to n.
For multiples of 3, return "Fizz".
For multiples of 5, return "Buzz".
For multiples of both 3 and 5, return "FizzBuzz".

## Approach
Loop from 1 to n.
Check divisibility by both 3 and 5 first, then check 3 and 5 separately.
Otherwise, add the number as a string.

## Complexity
Time: O(n)
Space: O(n)
