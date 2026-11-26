# LeetCode 3360 - Stone Removal Game

## Problem
Alice starts with n stones.
On the first turn, Alice removes 10 stones.
On each following turn, the number of stones removed decreases by 1.
The player who cannot make a valid move loses.
Return true if Alice wins.

## Approach
Start with 10 stones to remove.
Keep increasing the required removal count while enough stones remain.
If a player cannot make the required move, that player loses.
Return whether Alice wins.

## Complexity
Time: O(√n)
Space: O(1)
