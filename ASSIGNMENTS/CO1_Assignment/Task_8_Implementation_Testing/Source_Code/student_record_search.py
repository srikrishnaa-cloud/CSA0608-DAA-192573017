"""
CSA0608 - Design and Analysis of Algorithms
Assignment 1 - CO1: Large-Scale Student Record Search System
Author: DHILIP N (Reg No: 192573017)

This module implements, tests, and benchmarks three distinct algorithmic strategies
for searching student records by Registration Number:
  1. Iterative Linear Search (Unsorted array, Brute Force)
  2. Recursive Binary Search (Sorted array, Divide and Conquer)
  3. Hash Table Direct Lookup (Chained/Direct Hashing, Constant Expected Time)
"""

from __future__ import annotations

import argparse
import csv
import gc
import os
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Set recursion depth high enough for binary search (log2(10^6) ~ 20, but safe margin)
sys.setrecursionlimit(50000)


@dataclass(slots=True)
class StudentRecord:
    """Represents a student record in the university database."""
    reg_no: str
    student_id: int
    name: str
    dept: str
    cgpa: float


class ComparisonCounter:
    """Tracks basic operations (comparisons) explicitly."""
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0


# ==========================================
# 1. ALGORITHM IMPLEMENTATIONS
# ==========================================

def linear_search(records: List[StudentRecord], target: str) -> Tuple[Optional[StudentRecord], int]:
    """
    Iterative Sequential Search (Brute Force).
    Basic operation: Key equality comparison (records[i].reg_no == target).
    Time Complexity: O(n) worst/avg, O(1) best. Space: O(1).
    """
    comparisons = 0
    for record in records:
        comparisons += 1
        if record.reg_no == target:
            return record, comparisons
    return None, comparisons


def recursive_binary_search(
    sorted_records: List[StudentRecord],
    target: str,
    low: int,
    high: int,
    counter: ComparisonCounter
) -> Optional[StudentRecord]:
    """
    Recursive Binary Search (Divide and Conquer).
    Basic operation: Three-way key comparison at midpoint.
    Recurrence: T(n) = T(n/2) + c.
    Time Complexity: O(log n) worst/avg, O(1) best. Space: O(log n) auxiliary stack.
    """
    if low > high:
        return None

    mid = low + (high - low) // 2
    counter.increment()

    if sorted_records[mid].reg_no == target:
        return sorted_records[mid]
    elif sorted_records[mid].reg_no > target:
        return recursive_binary_search(sorted_records, target, low, mid - 1, counter)
    else:
        return recursive_binary_search(sorted_records, target, mid + 1, high, counter)


def binary_search_wrapper(sorted_records: List[StudentRecord], target: str) -> Tuple[Optional[StudentRecord], int]:
    """Wrapper to initiate recursive binary search and capture comparison counts."""
    counter = ComparisonCounter()
    result = recursive_binary_search(sorted_records, target, 0, len(sorted_records) - 1, counter)
    return result, counter.count


class StudentHashTable:
    """
    Hash Table with separate chaining / bucket indexing for O(1) expected retrieval.
    Basic operation: Key equality comparison during bucket collision inspection.
    """
    def __init__(self, capacity: int):
        self.capacity = max(capacity, 1024)
        self.buckets: List[List[StudentRecord]] = [[] for _ in range(self.capacity)]
        self.size = 0

    def _hash(self, key: str) -> int:
        # Polynomial rolling hash / built-in hash modulo capacity
        return hash(key) % self.capacity

    def insert(self, record: StudentRecord) -> None:
        idx = self._hash(record.reg_no)
        self.buckets[idx].append(record)
        self.size += 1

    def search(self, target: str) -> Tuple[Optional[StudentRecord], int]:
        idx = self._hash(target)
        comparisons = 0
        for rec in self.buckets[idx]:
            comparisons += 1
            if rec.reg_no == target:
                return rec, comparisons
        return None, comparisons


# ==========================================
# 2. DATA GENERATION
# ==========================================

DEPARTMENTS = ["CSE", "ECE", "MECH", "CIVIL", "BIOTECH", "IT", "AI_DS", "EEE"]
FIRST_NAMES = ["Aarav", "Ananya", "Diya", "Kabir", "Meera", "Rohan", "Siddharth", "Zoya", "Krishna", "Priya"]
LAST_NAMES = ["Sharma", "Verma", "Iyer", "Reddy", "Patel", "Singh", "Nair", "Kulkarni", "Das", "Menon"]


def generate_synthetic_records(size: int, seed: int = 42) -> List[StudentRecord]:
    """Generates synthetic student records with unique registration numbers."""
    rng = random.Random(seed)
    digits = max(6, len(str(size - 1)))
    
    # Generate unique IDs and shuffle to simulate raw unsorted database
    ids = list(range(1, size + 1))
    rng.shuffle(ids)

    records = []
    for sid in ids:
        reg_no = f"REG{sid:0{digits}d}"
        name = f"{rng.choice(FIRST_NAMES)} {rng.choice(LAST_NAMES)}"
        dept = rng.choice(DEPARTMENTS)
        cgpa = round(rng.uniform(6.0, 10.0), 2)
        records.append(StudentRecord(reg_no, sid, name, dept, cgpa))
    return records


# ==========================================
# 3. BENCHMARK SUITE
# ==========================================

def run_benchmarks(sizes: List[int], num_queries: int = 50, output_dir: Path = Path(".")) -> List[dict]:
    """Runs systematic benchmarks across dataset sizes and logs time and comparison counts."""
    results = []
    print(f"{'Size (N)':<10} | {'Algorithm':<22} | {'Case':<8} | {'Avg Comp':<12} | {'Avg Time (ms)':<15} | {'Prep Time (ms)':<15}")
    print("-" * 95)

    for n in sizes:
        # 1. Generate data
        raw_records = generate_synthetic_records(n, seed=42)

        # 2. Preprocessing for Binary Search (Sorting)
        t0 = time.perf_counter()
        sorted_records = sorted(raw_records, key=lambda r: r.reg_no)
        t_sort = (time.perf_counter() - t0) * 1000.0  # ms

        # 3. Preprocessing for Hash Table
        t0 = time.perf_counter()
        hash_table = StudentHashTable(capacity=int(n * 1.3))
        for r in raw_records:
            hash_table.insert(r)
        t_hash_build = (time.perf_counter() - t0) * 1000.0  # ms

        # Sample query targets
        rng = random.Random(12345)
        # Existing targets for Average Case
        avg_sample_records = rng.sample(raw_records, min(num_queries, n))
        avg_targets = [r.reg_no for r in avg_sample_records]
        
        # Best cases
        linear_best_target = raw_records[0].reg_no
        binary_best_target = sorted_records[len(sorted_records) // 2].reg_no
        hash_best_target = avg_targets[0]

        # Worst cases (Not found)
        unsuccessful_target = "REG_NON_EXISTENT_999999"

        # --- A. LINEAR SEARCH ---
        # Best Case
        t0 = time.perf_counter()
        _, lin_best_comp = linear_search(raw_records, linear_best_target)
        t_lin_best = (time.perf_counter() - t0) * 1000.0

        # Worst Case
        t0 = time.perf_counter()
        _, lin_worst_comp = linear_search(raw_records, unsuccessful_target)
        t_lin_worst = (time.perf_counter() - t0) * 1000.0

        # Average Case
        lin_avg_comps = []
        t0 = time.perf_counter()
        for t in avg_targets:
            _, c = linear_search(raw_records, t)
            lin_avg_comps.append(c)
        t_lin_avg = ((time.perf_counter() - t0) / len(avg_targets)) * 1000.0
        lin_avg_comp = sum(lin_avg_comps) / len(lin_avg_comps)

        # --- B. BINARY SEARCH ---
        # Best Case
        t0 = time.perf_counter()
        _, bin_best_comp = binary_search_wrapper(sorted_records, binary_best_target)
        t_bin_best = (time.perf_counter() - t0) * 1000.0

        # Worst Case
        t0 = time.perf_counter()
        _, bin_worst_comp = binary_search_wrapper(sorted_records, unsuccessful_target)
        t_bin_worst = (time.perf_counter() - t0) * 1000.0

        # Average Case
        bin_avg_comps = []
        t0 = time.perf_counter()
        for t in avg_targets:
            _, c = binary_search_wrapper(sorted_records, t)
            bin_avg_comps.append(c)
        t_bin_avg = ((time.perf_counter() - t0) / len(avg_targets)) * 1000.0
        bin_avg_comp = sum(bin_avg_comps) / len(bin_avg_comps)

        # --- C. HASH TABLE SEARCH ---
        # Best Case
        t0 = time.perf_counter()
        _, hash_best_comp = hash_table.search(hash_best_target)
        t_hash_best = (time.perf_counter() - t0) * 1000.0

        # Worst Case (Miss)
        t0 = time.perf_counter()
        _, hash_worst_comp = hash_table.search(unsuccessful_target)
        t_hash_worst = (time.perf_counter() - t0) * 1000.0

        # Average Case
        hash_avg_comps = []
        t0 = time.perf_counter()
        for t in avg_targets:
            _, c = hash_table.search(t)
            hash_avg_comps.append(c)
        t_hash_avg = ((time.perf_counter() - t0) / len(avg_targets)) * 1000.0
        hash_avg_comp = sum(hash_avg_comps) / len(hash_avg_comps)

        # Record rows
        cases = [
            ("Linear Search", "Best", lin_best_comp, t_lin_best, 0.0),
            ("Linear Search", "Average", lin_avg_comp, t_lin_avg, 0.0),
            ("Linear Search", "Worst", lin_worst_comp, t_lin_worst, 0.0),
            ("Binary Search (Rec)", "Best", bin_best_comp, t_bin_best, t_sort),
            ("Binary Search (Rec)", "Average", bin_avg_comp, t_bin_avg, t_sort),
            ("Binary Search (Rec)", "Worst", bin_worst_comp, t_bin_worst, t_sort),
            ("Hash Table Search", "Best", hash_best_comp, t_hash_best, t_hash_build),
            ("Hash Table Search", "Average", hash_avg_comp, t_hash_avg, t_hash_build),
            ("Hash Table Search", "Worst", hash_worst_comp, t_hash_worst, t_hash_build),
        ]

        for alg, c_type, comp, t_query, t_prep in cases:
            results.append({
                "N": n,
                "Algorithm": alg,
                "Case": c_type,
                "Comparisons": comp,
                "QueryTime_ms": round(t_query, 6),
                "PreprocessingTime_ms": round(t_prep, 3)
            })
            if c_type == "Average":
                print(f"{n:<10} | {alg:<22} | {c_type:<8} | {comp:<12.1f} | {t_query:<15.6f} | {t_prep:<15.3f}")

        # Free memory
        del raw_records
        del sorted_records
        del hash_table
        gc.collect()

    return results


def export_results_and_plots(results: List[dict], output_dir: Path):
    """Exports benchmark CSV and generates comparison charts using matplotlib."""
    import matplotlib.pyplot as plt

    csv_path = output_dir / "benchmark_results.csv"
    keys = ["N", "Algorithm", "Case", "Comparisons", "QueryTime_ms", "PreprocessingTime_ms"]
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
    print(f"\n[+] Benchmark results saved to: {csv_path}")

    # Filter average case data for plotting
    avg_results = [r for r in results if r["Case"] == "Average"]
    sizes = sorted(list(set(r["N"] for r in avg_results)))

    lin_times = [r["QueryTime_ms"] for r in avg_results if r["Algorithm"] == "Linear Search"]
    bin_times = [r["QueryTime_ms"] for r in avg_results if r["Algorithm"] == "Binary Search (Rec)"]
    hash_times = [r["QueryTime_ms"] for r in avg_results if r["Algorithm"] == "Hash Table Search"]

    lin_comps = [r["Comparisons"] for r in avg_results if r["Algorithm"] == "Linear Search"]
    bin_comps = [r["Comparisons"] for r in avg_results if r["Algorithm"] == "Binary Search (Rec)"]
    hash_comps = [r["Comparisons"] for r in avg_results if r["Algorithm"] == "Hash Table Search"]

    # 1. Search Execution Time vs Input Size (Log-Log Scale)
    plt.figure(figsize=(9, 5.5), dpi=300)
    plt.plot(sizes, lin_times, marker='o', linewidth=2, color="#d9534f", label="Linear Search O(n)")
    plt.plot(sizes, bin_times, marker='s', linewidth=2, color="#0275d8", label="Recursive Binary Search O(log n)")
    plt.plot(sizes, hash_times, marker='^', linewidth=2, color="#5cb85c", label="Hash Table Search O(1)")
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Search Execution Time vs Dataset Size (Average Case)", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Dataset Size N (Number of Student Records)", fontsize=11)
    plt.ylabel("Execution Time per Query (Milliseconds, Log Scale)", fontsize=11)
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()
    chart1 = output_dir / "search_time_comparison.png"
    plt.savefig(chart1)
    plt.close()
    print(f"[+] Generated: {chart1}")

    # 2. Key Comparisons vs Input Size
    plt.figure(figsize=(9, 5.5), dpi=300)
    plt.plot(sizes, lin_comps, marker='o', linewidth=2, color="#d9534f", label="Linear Search (n/2)")
    plt.plot(sizes, bin_comps, marker='s', linewidth=2, color="#0275d8", label="Recursive Binary Search (log2 n)")
    plt.plot(sizes, hash_comps, marker='^', linewidth=2, color="#5cb85c", label="Hash Table Search (~1.0)")
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Dominant Basic Operations (Comparisons) vs Dataset Size", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Dataset Size N (Records)", fontsize=11)
    plt.ylabel("Number of Key Comparisons (Log Scale)", fontsize=11)
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()
    chart2 = output_dir / "comparisons_count.png"
    plt.savefig(chart2)
    plt.close()
    print(f"[+] Generated: {chart2}")

    # 3. Preprocessing Time vs Dataset Size
    bin_preps = [r["PreprocessingTime_ms"] for r in avg_results if r["Algorithm"] == "Binary Search (Rec)"]
    hash_preps = [r["PreprocessingTime_ms"] for r in avg_results if r["Algorithm"] == "Hash Table Search"]
    plt.figure(figsize=(9, 5.5), dpi=300)
    plt.plot(sizes, bin_preps, marker='s', linewidth=2, color="#0275d8", label="Sorting for Binary Search O(n log n)")
    plt.plot(sizes, hash_preps, marker='^', linewidth=2, color="#5cb85c", label="Table Construction O(n)")
    plt.xscale('log')
    plt.yscale('log')
    plt.title("One-Time Preprocessing Time vs Dataset Size", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Dataset Size N (Records)", fontsize=11)
    plt.ylabel("Preprocessing Time (Milliseconds, Log Scale)", fontsize=11)
    plt.grid(True, which="both", ls="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.tight_layout()
    chart3 = output_dir / "preprocessing_vs_size.png"
    plt.savefig(chart3)
    plt.close()
    print(f"[+] Generated: {chart3}")


def main():
    parser = argparse.ArgumentParser(description="DAA CO1 Search Benchmark")
    parser.add_argument("--sizes", nargs="+", type=int, default=[1000, 10000, 100000, 1000000],
                        help="List of input sizes to benchmark")
    parser.add_argument("--queries", type=int, default=30, help="Number of queries for averaging")
    parser.add_argument("--output", type=str, default=".", help="Output directory")
    args = parser.parse_args()

    out_path = Path(args.output)
    out_path.mkdir(parents=True, exist_ok=True)

    print("=" * 80)
    print(" CSA0608 - DESIGN AND ANALYSIS OF ALGORITHMS")
    print(" ASSIGNMENT 1 (CO1) - SEARCH STRATEGY BENCHMARK SUITE")
    print(f" Target Sizes: {args.sizes}")
    print(f" Queries per size: {args.queries}")
    print("=" * 80)

    results = run_benchmarks(args.sizes, args.queries, out_path)
    export_results_and_plots(results, out_path)
    print("\n[✓] Benchmark execution and visualization completed successfully.")


if __name__ == "__main__":
    main()
