# CSA0608 – Design and Analysis of Algorithms
## Assignment 1: Course Outcome 1 (CO1)
**Title:** Design, Analyse and Validate an Efficient Search Strategy for a Large-Scale Student Record System  
**Course Code:** CSA0608  
**Department:** Computer Science and Engineering  
**Institution:** SIMATS Engineering, Saveetha Institute of Medical and Technical Sciences  
**Student Name:** DHILIP N  
**Student Register Number:** 192573017  

---

## 📌 Project Overview
This repository contains the complete theoretical, mathematical, asymptotic, and empirical investigation of search algorithms applied to an enterprise university student record retrieval system. The system evaluates databases scaling from $1,000$ to over $1,000,000$ student records.

Three distinct algorithmic paradigms are systematically designed, derived, implemented, benchmarked, and evaluated:
1. **Iterative Linear Search** (Brute-Force Paradigm) – $O(n)$
2. **Recursive Binary Search** (Divide-and-Conquer Paradigm) – $O(\log n)$
3. **Hash Table Direct Addressing / Chained Search** (Hashing Paradigm) – $O(1)$

---

## 🗂️ Repository Architecture

```
CO1_Assignment/
│
├── Task_1_Algorithm_Design/               # High-level architecture, flowcharts, and pseudocode
├── Task_2_Basic_Operation/                # Dominant operations identification & justification
├── Task_3_Mathematical_Complexity/        # Rigorous mathematical derivation of T(n)
├── Task_4_Case_Analysis/                  # Best-, Average-, and Worst-case derivations
├── Task_5_Asymptotic_Analysis/            # Big-O, Big-Omega, Big-Theta asymptotic bounds
├── Task_6_Recurrence_Formulation/         # Formal recurrence relation: T(n) = T(n/2) + c
├── Task_7_Recurrence_Solution/            # Solutions via Master Theorem, Iteration, Substitution
├── Task_8_Implementation_Testing/         # Testing protocol & source code
│   └── Source_Code/
│       └── student_record_search.py       # Full Python benchmarking & test harness
├── Task_9_Experimental_Performance/       # Benchmark tables and empirical metrics
│   └── benchmark_results.csv              # Exact CSV data for all test configurations
├── Task_10_Theory_vs_Experiment/          # Rigorous theoretical vs experimental correlation
├── Task_11_Final_Recommendation/          # Final architectural recommendation & justification
├── Task_12_Design_Challenge/              # Day-4 Design Challenge (50,000 req/hr on 10^6 records)
├── Report/                                # Complete consolidated report & visual artifacts
│   ├── Tables_and_Graphs/                 # High-resolution benchmark comparison plots
│   │   ├── search_time_comparison.png
│   │   ├── comparisons_count.png
│   │   └── preprocessing_vs_size.png
│   ├── Source_Code_Screenshots/
│   ├── Output_Screenshots/
│   ├── Analysis/
│   └── Documentation/
└── README.md                              # Top-level index and guide
```

---

## 🚀 Execution Instructions

### Prerequisites
* Python 3.10+ (Standard library only; `matplotlib` optional for generating plots).

### Running the Benchmark Suite
To execute the automated benchmark across $1,000$, $10,000$, $100,000$, and $1,000,000$ student records:

```bash
# Clone the repository
git clone https://github.com/srikrishnaa-cloud/CSA0608-DAA-192573017.git
cd CSA0608-DAA-192573017/ASSIGNMENTS/CO1_Assignment

# Run the test & benchmark suite
python Task_8_Implementation_Testing/Source_Code/student_record_search.py --sizes 1000 10000 100000 1000000 --queries 30 --output Report/Tables_and_Graphs
```

---

## 📊 Summary of Experimental Results (Average Case)

| Dataset Size ($N$) | Linear Search Time | Binary Search (Rec) Time | Hash Table Search Time | Hash Speedup vs Linear |
| :---: | :---: | :---: | :---: | :---: |
| **1,000** | 0.388 ms | 0.033 ms | 0.0038 ms | **$102\times$** |
| **10,000** | 7.222 ms | 0.182 ms | 0.0263 ms | **$275\times$** |
| **100,000** | 49.651 ms | 0.057 ms | 0.0082 ms | **$6,070\times$** |
| **1,000,000** | 391.122 ms | 0.110 ms | 0.0037 ms | **$104,662\times$** |

---

## 🏆 Key Findings and Final Recommendation
1. **Linear Search is Unviable at Scale:** At $N = 10^6$, linear search requires $\approx 391$ ms per query. Under a production load of $50,000$ searches/hour, it would require over $5.4$ hours of CPU execution time per hour, causing catastrophic server collapse.
2. **Recursive Binary Search is Logarithmic and Fast:** Consistently resolves within $18$ comparisons ($0.11$ ms), but incurs cache miss overheads and requires an expensive $O(n \log n)$ upfront sort.
3. **Hash Table is the Recommended Enterprise Solution:** Delivers predictable sub-microsecond query time ($3.7\,\mu\text{s}$) with $O(1)$ average complexity. The one-time build cost ($12.6$ s) is fully amortized in just $33$ queries.
4. **Day-4 Challenge Architecture:** An **In-Memory Hash Index with Nightly Shadow-Buffer Atomic Swapping** easily sustains $50,000$ searches/hour using only $0.005\%$ of a single CPU core, guaranteeing zero downtime and lock-free thread safety.
