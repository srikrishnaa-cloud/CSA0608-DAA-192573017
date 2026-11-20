from typing import Tuple

def brute_force_string_match(text: str, pattern: str) -> Tuple[int, int]:
    n = len(text)
    m = len(pattern)
    comparisons = 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] == pattern[j]:
                j += 1
            else:
                break
        if j == m:
            return i, comparisons
    return -1, comparisons
