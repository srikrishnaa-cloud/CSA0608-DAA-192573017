# Q7: Day-4 Design Challenge: Closest Pair Redesign

## A. Bottleneck Diagnosis
The original Q4 brute-force algorithm unconditionally evaluates all n(n-1)/2 = Theta(n^2) pairs, ignoring spatial proximity. Drones separated by thousands of meters are unnecessarily compared.

## B. Design Objective
Prune the search space by sorting and spatial bounding, eliminating distance calculations between distant drones, achieving O(n log n) time.

## C. Revised Algorithmic Strategy (Divide & Conquer)
```text
Algorithm EfficientClosestPair(P[0..n-1])
Begin
    Sort points by X coordinate (Px) and Y coordinate (Py)
    return RecursiveClosestPair(Px, Py)
End

Function RecursiveClosestPair(Px, Py)
    if length(Px) <= 3 then return BruteForceClosestPair(Px)
    mid <- length(Px) / 2
    dL <- RecursiveClosestPair(left_Px, left_Py)
    dR <- RecursiveClosestPair(right_Px, right_Py)
    delta <- min(dL, dR)
    
    Strip <- points in Py within delta of vertical divider line
    for each point p in Strip do
        examine at most next 7 points in Strip
        update delta if closer pair found
    return delta
End
```

## D. Empirical Reduction
* At N = 5,000 drones:
  * Original Brute-Force: 12,497,500 distance calculations (5,322 ms).
  * Redesigned Divide-and-Conquer: 82,588 distance calculations (188 ms).
  * 99.3% reduction in distance calculations, providing sub-second real-time collision detection.
