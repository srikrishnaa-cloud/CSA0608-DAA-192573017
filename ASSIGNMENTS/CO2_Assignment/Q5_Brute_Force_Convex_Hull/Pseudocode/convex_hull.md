# Q5: Brute-Force Convex Hull Pseudocode

```text
Algorithm BruteForceConvexHull(P[0..n-1])
Begin
    hull_edges <- empty list
    for i <- 0 to n - 1 do
        for j <- 0 to n - 1 (j != i) do
            p1 <- P[i], p2 <- P[j]
            valid_edge <- true
            first_sign <- null
            for k <- 0 to n - 1 (k != i, k != j) do
                cross <- (p2.x - p1.x)*(P[k].y - p1.y) - (p2.y - p1.y)*(P[k].x - p1.x)
                sign <- sign(cross)
                if first_sign is null then
                    first_sign <- sign
                else if sign != first_sign then
                    valid_edge <- false
                    break
            if valid_edge then
                hull_edges.append((p1, p2))
    return hull_edges
End
```

## Geometric Decision Rule:
Two points Pi, Pj form an outer convex boundary edge if and only if every other point Pk lies entirely to one side of the directed line Pi -> Pj, mathematically validated by the 2D cross product having a uniform sign for all k.
