# Q4: Brute-Force Closest Pair Pseudocode

```text
Algorithm BruteForceClosestPair(P[0..n-1])
Begin
    min_dist <- inf
    closest_pair <- (P[0], P[1])
    for i <- 0 to n - 2 do
        for j <- i + 1 to n - 1 do
            d <- distance(P[i], P[j])
            if d < min_dist then
                min_dist <- d
                closest_pair <- (P[i], P[j])
    return closest_pair, min_dist
End
```

## Mathematical Derivation of Unique Pairs
The algorithm avoids duplicate comparisons by constraining j > i.
Total pairs examined:
n(n - 1) / 2 = Theta(n^2)
