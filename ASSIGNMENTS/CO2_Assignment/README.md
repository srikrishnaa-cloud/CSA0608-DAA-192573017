# CSA0608 - Design and Analysis of Algorithms
## Assignment 2: Course Outcome 2 (CO2)
**Title:** Brute-Force and Exhaustive-Search Techniques: Sorting, Searching, Closest-Pair, Convex-Hull, and Knapsack Optimization
**Course Code:** CSA0608
**Department:** Computer Science and Engineering
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences
**Student Name:** DHILIP N  
**Student Register Number:** 192573017

---

## Assignment Architecture

```
CO2_Assignment/
|-- Q1_Sorting_Algorithms/
|   |-- Implementation_Code/sorting_algorithms.py
|   |-- Pseudocode/sorting.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
|-- Q2_Sequential_Search/
|   |-- Implementation_Code/sequential_search.py
|   |-- Pseudocode/sequential_search.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
|-- Q3_Brute_Force_String_Matching/
|   |-- Implementation_Code/brute_force_string_matching.py
|   |-- Pseudocode/string_matching.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
|-- Q4_Brute_Force_Closest_Pair/
|   |-- Implementation_Code/brute_force_closest_pair.py
|   |-- Pseudocode/closest_pair.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
|-- Q5_Brute_Force_Convex_Hull/
|   |-- Implementation_Code/brute_force_convex_hull.py
|   |-- Pseudocode/convex_hull.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
|-- Q6_Exhaustive_Search/
|   |-- Implementation_Code/exhaustive_search.py
|   |-- Pseudocode/exhaustive_knapsack.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
|-- Q7_Day4_Design_Challenge/
|   |-- Implementation_Code/closest_pair_redesign.py
|   |-- Pseudocode/closest_pair_redesign.md
|   |-- Prediction_Before_Run.md
|   `-- Output_Screenshots/RUN_OUTPUT.txt
`-- Supporting_Files/
    |-- results/
    `-- run_experiments.py
```

---

## Summary of Experimental Highlights

1. **Q1 Sorting:** For 95% nearly sorted orders (N = 1000), Insertion Sort performs only 35,909 comparisons (5.0 ms) vs 499,500 comparisons (40.9 ms) for Selection Sort.
2. **Q2 Sequential Search:** Linear search remains practical for single hangars (N <= 200), but expanding to 20 hangars (N = 20,000) requires 10,000 comparisons per search, necessitating a Hash Table index.
3. **Q3 String Matching:** Repetitive prefixes cause O(m * n) comparisons, demonstrating that input character distribution directly governs search work.
4. **Q4 vs Q7 Closest Pair:** For N = 5,000 drones, the redesigned Divide-and-Conquer algorithm reduced distance calculations from 12,497,500 down to 82,588 (99.3% reduction), cutting latency from 5.32 seconds to 0.18 seconds.
5. **Q6 Exhaustive Search:** Scaling from N = 4 to N = 20 packages increased subset evaluations from 16 to 1,048,576, illustrating combinatorial explosion and establishing N approx 20 as the strict operational boundary.
