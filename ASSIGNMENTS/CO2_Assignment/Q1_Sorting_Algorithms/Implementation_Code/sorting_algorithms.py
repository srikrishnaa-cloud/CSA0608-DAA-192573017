from typing import List, Tuple

def selection_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps

def bubble_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps

def insertion_sort(arr: List[int]) -> Tuple[List[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons, shifts
