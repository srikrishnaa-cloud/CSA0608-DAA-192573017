# Comprehensive Assignment Report - CO1

**Course:** CSA0608 – Design and Analysis of Algorithms  
**Assignment:** Assignment 1 – CO1: Search Strategy for Large-Scale Student Record System  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Student Register Number:** 192573017  

---

## Executive Summary
This report presents an in-depth mathematical, asymptotic, and empirical investigation into search strategies for large-scale university student record management. We evaluate:
1. **Iterative Linear Search** ($O(n)$)
2. **Recursive Binary Search** ($O(\log n)$)
3. **Hash Table Direct Search** ($O(1)$)

Across dataset sizes $N \in \{1\,000, 10\,000, 100\,000, 1\,000\,000\}$, we record execution times, operation counts, and asymptotic behavior, concluding with the Day-4 Design Challenge for processing 50,000 queries/hour.

---

## Mark Distribution Matrix

| Task | Description | Marks Assigned | Status |
| :--- | :--- | :---: | :---: |
| **Task 1** | Algorithm Design (3 meaningfully different approaches) | 5 | Completed |
| **Task 2** | Basic Operation Identification and Justification | 2 | Completed |
| **Task 3** | Mathematical Time-Complexity Derivations | 6 | Completed |
| **Task 4** | Best, Average, and Worst-Case Analysis | 4 | Completed |
| **Task 5** | Asymptotic Analysis and Notation ($O, \Omega, \Theta$) | 3 | Completed |
| **Task 6** | Recurrence Formulation for Recursive Binary Search | 3 | Completed |
| **Task 7** | Recurrence Solution (Master Theorem, Iteration, Substitution) | 4 | Completed |
| **Task 8** | Implementation & Testing ($10^3 \to 10^6$ records) | 4 | Completed |
| **Task 9** | Experimental Performance Recording (Tables & Plots) | 3 | Completed |
| **Task 10** | Theory vs. Experiment Comparison & Anomaly Analysis | 4 | Completed |
| **Task 11** | Final Algorithm Recommendation and Defense | 4 | Completed |
| **Subtotal** | | **42** | |
| **Task 12** | Day-4 Design Challenge (50,000 req/hr on 1,000,000 records) | 8 | Completed |
| **TOTAL** | | **50** | **100% Ready** |

---

## Navigation Links to All Tasks

* [Task 1: Algorithm Design](../Task_1_Algorithm_Design/README.md)
* [Task 2: Basic Operation Identification](../Task_2_Basic_Operation/README.md)
* [Task 3: Mathematical Complexity Derivation](../Task_3_Mathematical_Complexity/README.md)
* [Task 4: Case Analysis](../Task_4_Case_Analysis/README.md)
* [Task 5: Asymptotic Analysis](../Task_5_Asymptotic_Analysis/README.md)
* [Task 6: Recurrence Formulation](../Task_6_Recurrence_Formulation/README.md)
* [Task 7: Recurrence Solution](../Task_7_Recurrence_Solution/README.md)
* [Task 8: Source Code and Testing](../Task_8_Implementation_Testing/README.md)
* [Task 9: Experimental Performance & Tables](../Task_9_Experimental_Performance/README.md)
* [Task 10: Theory vs Experiment](../Task_10_Theory_vs_Experiment/README.md)
* [Task 11: Final Recommendation](../Task_11_Final_Recommendation/README.md)
* [Task 12: Day-4 Design Challenge](../Task_12_Design_Challenge/README.md)
