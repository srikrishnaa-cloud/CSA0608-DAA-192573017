# Q1: Sorting Algorithms Pseudocode

## 1. Selection Sort
```text
Algorithm SelectionSort(A[0..n-1])
Begin
    for i <- 0 to n - 2 do
        min_idx <- i
        for j <- i + 1 to n - 1 do
            if A[j] < A[min_idx] then
                min_idx <- j
        if min_idx != i then
            swap(A[i], A[min_idx])
End
```

## 2. Bubble Sort (Early Exit)
```text
Algorithm BubbleSort(A[0..n-1])
Begin
    for i <- 0 to n - 1 do
        swapped <- false
        for j <- 0 to n - i - 2 do
            if A[j] > A[j + 1] then
                swap(A[j], A[j + 1])
                swapped <- true
        if not swapped then
            break
End
```

## 3. Insertion Sort
```text
Algorithm InsertionSort(A[0..n-1])
Begin
    for i <- 1 to n - 1 do
        key <- A[i]
        j <- i - 1
        while j >= 0 and A[j] > key do
            A[j + 1] <- A[j]
            j <- j - 1
        A[j + 1] <- key
End
```

## Recommendation for 95% Nearly Sorted E-Commerce Orders
* **Recommended Algorithm:** **Insertion Sort**
* **Justification:** When data is 95% ordered, Insertion Sort requires only O(n) comparisons because the inner while loop terminates on the very first comparison for items already in place. Selection Sort unconditionally incurs n(n-1)/2 = O(n^2) comparisons regardless of input ordering.
