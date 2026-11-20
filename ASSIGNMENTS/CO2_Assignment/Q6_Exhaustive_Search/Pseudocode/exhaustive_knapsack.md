# Q6: Exhaustive Search Knapsack Pseudocode

```text
Algorithm ExhaustiveKnapsack(Packages[0..n-1], W_max)
Begin
    best_val <- 0
    best_subset <- empty
    for each subset S in Packages do
        if weight(S) <= W_max then
            if value(S) > best_val then
                best_val <- value(S)
                best_subset <- S
    return best_subset, best_val
End
```

## Combinatorial Explosion:
The solution space contains exactly 2^n subsets. For n = 20, 2^20 = 1,048,576 subsets; for n = 30, 2^30 approx 1.07 * 10^9 subsets. Beyond n approx 22, exhaustive search becomes intractable under real-time response constraints.
