# leet22-dp — Generate Parentheses

Solution to [LeetCode 22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/): return every well-formed combination of `n` pairs of parentheses.

## Approach

Despite the repo name, the current code is **brute force, not DP**:

1. Treat each `2n`-bit number as a string, `0 → (` and `1 → )`.
2. Enumerate every number from `0…01…1` (`(((…)))`) to `1…10…0`.
3. Keep the strings that pass `legality()`: a running balance that never goes negative and ends at 0.

Complexity: about O(4^n · n). This passes LeetCode's limit (`n ≤ 8`) but does not scale.

Faster alternatives to try:
- **Backtracking**: add `(` while `open < n`, add `)` while `close < open`.
- **DP**: `f(n) = { "(" + a + ")" + b : a ∈ f(i), b ∈ f(n-1-i) }`.

## Usage

Written for the LeetCode editor, which pre-imports `List`. To run locally, add:

```python
from typing import List
print(Solution().generateParenthesis(3))
```
