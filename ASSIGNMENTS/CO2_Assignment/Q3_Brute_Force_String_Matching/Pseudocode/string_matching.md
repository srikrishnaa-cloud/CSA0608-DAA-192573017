# Q3: Brute-Force String Matching Pseudocode

```text
Algorithm BruteForceStringMatch(T[0..n-1], P[0..m-1])
Begin
    for i <- 0 to n - m do
        j <- 0
        while j < m and T[i + j] = P[j] do
            j <- j + 1
        if j = m then
            return i
    return -1
End
```

## Work Analysis:
* **Best Case (Minimal Effort):** Characters mismatch on the first letter (P[0]). Comparisons <= n - m + 1 = O(n).
* **Worst Case (Pathological Repeats):** Text consists of repeated prefix characters (e.g. AAAA...B with pattern AAAB). Each shift compares almost all m characters before failing, reaching O(m * n) comparisons.
