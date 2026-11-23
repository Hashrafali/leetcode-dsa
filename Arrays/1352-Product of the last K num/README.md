# LeetCode 1352 - Product of the Last K Numbers

## Approach
Use a prefix product array to efficiently calculate the product of the last k numbers.
When a zero appears, reset the prefix products.

## Complexity
Time: O(1) for add and getProduct
Space: O(n)
