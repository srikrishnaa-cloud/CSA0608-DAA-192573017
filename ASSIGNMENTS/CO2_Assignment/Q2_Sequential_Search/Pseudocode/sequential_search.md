# Q2: Sequential Search Pseudocode

```text
Algorithm SequentialSearch(tools[0..n-1], target_id)
Begin
    for i <- 0 to n - 1 do
        if tools[i].tool_id = target_id then
            return tools[i]
    return NOT_FOUND
End
```

## Engineering Boundary & 20 Hangar Expansion
* **Small Hangar (n <= 200, low query rate):** Sequential search is ideal because it requires 0 preprocessing and permits O(1) tool check-in/checkout.
* **Expanded (20 Hangar, n >= 20,000, frequent concurrent requests):** Sequential search degrades (avg 10,000 comparisons). We must transition to an in-memory Hash Table Index (O(1) lookup) or B-Tree to preserve sub-millisecond response.
