"""
CSA0608 - Design and Analysis of Algorithms
Assignment 2 - CO2: Comprehensive Benchmark & Experiment Suite
Questions Q1 through Q7
"""

import csv
import math
import os
import random
import sys
import time
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import List, Tuple, Optional, Dict
import matplotlib.pyplot as plt

# ==========================================
# Q1: SORTING ALGORITHMS
# ==========================================

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

def run_q1():
    print("=" * 60)
    print(" Q1: SORTING ALGORITHMS BENCHMARK")
    print("=" * 60)
    sizes = [100, 500, 1000]
    results = []
    
    for n in sizes:
        # 1. Random
        rng = random.Random(42)
        rand_data = [rng.randint(1, 10000) for _ in range(n)]
        
        # 2. 95% Nearly Sorted (sorted array with 5% swapped)
        nearly_data = sorted(rand_data)
        swap_count = max(1, int(n * 0.05))
        for _ in range(swap_count):
            i1, i2 = rng.randint(0, n - 1), rng.randint(0, n - 1)
            nearly_data[i1], nearly_data[i2] = nearly_data[i2], nearly_data[i1]
            
        # 3. Reverse Sorted (Worst Case)
        rev_data = sorted(rand_data, reverse=True)
        
        # 4. Edge Case: Identical Elements
        ident_data = [42] * n
        
        datasets = {
            "Random": rand_data,
            "Nearly_Sorted_95%": nearly_data,
            "Reverse_Sorted": rev_data,
            "Identical_Keys": ident_data
        }
        
        for d_name, d_val in datasets.items():
            for alg_name, fn in [("Selection Sort", selection_sort), ("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort)]:
                t0 = time.perf_counter()
                _, comps, moves = fn(d_val)
                t_ms = (time.perf_counter() - t0) * 1000.0
                results.append({
                    "N": n, "Dataset": d_name, "Algorithm": alg_name,
                    "Comparisons": comps, "Swaps_or_Shifts": moves, "Time_ms": round(t_ms, 4)
                })
                print(f"N={n:<5} | {d_name:<18} | {alg_name:<15} | Comp: {comps:<8} | Moves: {moves:<8} | Time: {t_ms:.4f} ms")
    return results

# ==========================================
# Q2: SEQUENTIAL SEARCH
# ==========================================

@dataclass
class ToolRecord:
    tool_id: str
    tech_id: str
    issue_time: str
    work_bay: str

def sequential_search(tools: List[ToolRecord], target_id: str) -> Tuple[Optional[ToolRecord], int]:
    comparisons = 0
    for t in tools:
        comparisons += 1
        if t.tool_id == target_id:
            return t, comparisons
    return None, comparisons

def run_q2():
    print("\n" + "=" * 60)
    print(" Q2: SEQUENTIAL SEARCH (TOOL TRACKING)")
    print("=" * 60)
    sizes = [50, 200, 500, 1000, 5000, 20000]
    results = []
    
    for n in sizes:
        tools = [ToolRecord(f"T-{i:05d}", f"TECH-{i%15:03d}", "08:30", f"BAY-{i%8+1}") for i in range(n)]
        
        # Test positions
        best_target = tools[0].tool_id
        mid_target = tools[n // 2].tool_id
        worst_target = tools[-1].tool_id
        miss_target = "T-999999"
        
        cases = [
            ("Successful_Beginning", best_target, 1),
            ("Successful_Middle", mid_target, n // 2 + 1),
            ("Successful_End", worst_target, n),
            ("Unsuccessful_Search", miss_target, n)
        ]
        
        for c_name, tgt, expected_comp in cases:
            t0 = time.perf_counter()
            rec, comps = sequential_search(tools, tgt)
            t_ms = (time.perf_counter() - t0) * 1000.0
            results.append({
                "N": n, "Search_Case": c_name, "Target": tgt,
                "Comparisons": comps, "Time_ms": round(t_ms, 5)
            })
            print(f"N={n:<6} | {c_name:<22} | Comp: {comps:<6} | Time: {t_ms:.5f} ms")
    return results

# ==========================================
# Q3: BRUTE-FORCE STRING MATCHING
# ==========================================

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

def run_q3():
    print("\n" + "=" * 60)
    print(" Q3: BRUTE-FORCE STRING MATCHING")
    print("=" * 60)
    
    # 1. Best Case (First char mismatch almost everywhere)
    text_best = "XYZ" * 2000 + "TARGET"
    pattern_best = "TARGET"
    
    # 2. Worst Case (Repeated matching prefix followed by mismatch)
    text_worst = ("A" * 99 + "B") * 50
    pattern_worst = "A" * 50 + "B"
    
    # 3. Real-World Log Search
    text_log = "[2026-11-20 08:30:15] INFO: User login accepted. [2026-11-20 08:31:02] WARN: Multiple failed logins. [2026-11-20 08:32:00] ERROR: SQL_INJECTION_ATTEMPT detected from 192.168.1.45"
    pattern_log = "SQL_INJECTION_ATTEMPT"
    
    tests = [
        ("Best_Case_Immediate_Mismatch", text_best, pattern_best),
        ("Worst_Case_Pathological_Repeats", text_worst, pattern_worst),
        ("RealWorld_Log_Signature", text_log, pattern_log)
    ]
    
    results = []
    for name, txt, pat in tests:
        t0 = time.perf_counter()
        idx, comps = brute_force_string_match(txt, pat)
        t_ms = (time.perf_counter() - t0) * 1000.0
        results.append({
            "Scenario": name, "Text_Length": len(txt), "Pattern_Length": len(pat),
            "Match_Index": idx, "Comparisons": comps, "Time_ms": round(t_ms, 5)
        })
        print(f"{name:<32} | Text: {len(txt):<5} | Pat: {len(pat):<3} | Comps: {comps:<7} | Found: {idx} | Time: {t_ms:.5f} ms")
    return results

# ==========================================
# Q4: BRUTE-FORCE CLOSEST PAIR
# ==========================================

def brute_force_closest_pair(points: List[Tuple[float, float]]) -> Tuple[Tuple[Tuple[float, float], Tuple[float, float]], float, int, int]:
    n = len(points)
    min_dist_sq = float('inf')
    closest = (points[0], points[1])
    pairs_examined = 0
    dist_calcs = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            pairs_examined += 1
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            dist_sq = dx * dx + dy * dy
            dist_calcs += 1
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                closest = (points[i], points[j])
                
    return closest, math.sqrt(min_dist_sq), pairs_examined, dist_calcs

def run_q4():
    print("\n" + "=" * 60)
    print(" Q4: BRUTE-FORCE CLOSEST PAIR (DRONE MONITORING)")
    print("=" * 60)
    sizes = [100, 250, 500, 1000, 2000]
    results = []
    
    for n in sizes:
        rng = random.Random(42)
        points = [(rng.uniform(0, 1000), rng.uniform(0, 1000)) for _ in range(n)]
        
        t0 = time.perf_counter()
        _, min_d, pairs, dists = brute_force_closest_pair(points)
        t_ms = (time.perf_counter() - t0) * 1000.0
        theoretical_pairs = n * (n - 1) // 2
        results.append({
            "N": n, "Theoretical_Pairs": theoretical_pairs, "Pairs_Examined": pairs,
            "Distance_Calculations": dists, "Min_Distance": round(min_d, 3), "Time_ms": round(t_ms, 4)
        })
        print(f"N={n:<5} | Pairs: {pairs:<8} (n(n-1)/2={theoretical_pairs:<8}) | MinDist: {min_d:<6.2f} | Time: {t_ms:.4f} ms")
    return results

# ==========================================
# Q5: BRUTE-FORCE CONVEX HULL
# ==========================================

def orientation(p1: Tuple[float, float], p2: Tuple[float, float], p3: Tuple[float, float]) -> float:
    # 2D cross product: (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def brute_force_convex_hull(points: List[Tuple[float, float]]) -> Tuple[List[Tuple[Tuple[float, float], Tuple[float, float]]], int]:
    n = len(points)
    hull_edges = []
    tests_performed = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            p1, p2 = points[i], points[j]
            valid_edge = True
            first_sign = None
            
            for k in range(n):
                if k == i or k == j:
                    continue
                tests_performed += 1
                cross = orientation(p1, p2, points[k])
                
                # Check sign
                if abs(cross) < 1e-9:
                    continue # collinear
                sign = 1 if cross > 0 else -1
                if first_sign is None:
                    first_sign = sign
                elif sign != first_sign:
                    valid_edge = False
                    break
                    
            if valid_edge and first_sign is not None:
                hull_edges.append((p1, p2))
                
    return hull_edges, tests_performed

def run_q5():
    print("\n" + "=" * 60)
    print(" Q5: BRUTE-FORCE CONVEX HULL")
    print("=" * 60)
    
    # Dataset 1: Standard square with interior points
    pts_std = [
        (0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0), # boundary
        (5.0, 5.0), (3.0, 7.0), (2.0, 4.0), (8.0, 2.0)      # interior
    ]
    
    # Dataset 2: Collinear edge challenge
    pts_challenge = [
        (0.0, 0.0), (5.0, 0.0), (10.0, 0.0), # collinear on bottom
        (10.0, 10.0), (0.0, 10.0), (2.0, 5.0), (7.0, 6.0)
    ]
    
    results = []
    for name, pts in [("Standard_Interior_Points", pts_std), ("Challenge_Collinear_Points", pts_challenge)]:
        t0 = time.perf_counter()
        edges, tests = brute_force_convex_hull(pts)
        t_ms = (time.perf_counter() - t0) * 1000.0
        results.append({
            "Dataset": name, "Num_Points": len(pts), "Hull_Edges_Found": len(edges),
            "Side_Tests": tests, "Time_ms": round(t_ms, 4)
        })
        print(f"{name:<28} | Points: {len(pts):<3} | Edges: {len(edges):<3} | Tests: {tests:<5} | Time: {t_ms:.4f} ms")
        
    return results

# ==========================================
# Q6: EXHAUSTIVE SEARCH (0/1 KNAPSACK)
# ==========================================

@dataclass
class Package:
    pkg_id: str
    weight: float
    value: float

def exhaustive_knapsack(packages: List[Package], max_weight: float) -> Tuple[List[Package], float, float, int]:
    n = len(packages)
    best_value = 0.0
    best_combination = []
    subsets_evaluated = 0
    
    # 2^n subsets
    for r in range(n + 1):
        for combo in combinations(packages, r):
            subsets_evaluated += 1
            tot_w = sum(p.weight for p in combo)
            if tot_w <= max_weight:
                tot_v = sum(p.value for p in combo)
                if tot_v > best_value:
                    best_value = tot_v
                    best_combination = list(combo)
                    
    best_weight = sum(p.weight for p in best_combination)
    return best_combination, best_weight, best_value, subsets_evaluated

def run_q6():
    print("\n" + "=" * 60)
    print(" Q6: EXHAUSTIVE SEARCH (HUMANITARIAN AIRLIFT)")
    print("=" * 60)
    
    # Verified small instance (n = 4)
    small_pkgs = [
        Package("P1", 20, 60),
        Package("P2", 30, 90),
        Package("P3", 40, 100),
        Package("P4", 50, 120),
    ]
    cap_small = 70 # Optimal: P2 + P3 = 30 + 40 = 70kg, value = 190, or P1 + P4 = 70kg, value = 180 -> P2+P3=190
    
    best_combo, w, v, subs = exhaustive_knapsack(small_pkgs, cap_small)
    print(f"Verified Instance (N=4): Best Value = {v}, Weight = {w}, Subsets = {subs} (2^4 = 16)")
    
    # Scaling sizes
    sizes = [4, 8, 12, 16, 20]
    results = []
    rng = random.Random(42)
    
    for n in sizes:
        pkgs = [Package(f"PKG-{i}", rng.randint(5, 50), rng.randint(20, 150)) for i in range(n)]
        cap = sum(p.weight for p in pkgs) * 0.4
        
        t0 = time.perf_counter()
        best_c, bw, bv, count = exhaustive_knapsack(pkgs, cap)
        t_ms = (time.perf_counter() - t0) * 1000.0
        results.append({
            "N": n, "Total_Subsets_2^N": 2**n, "Subsets_Evaluated": count,
            "Best_Value": bv, "Best_Weight": round(bw, 1), "Time_ms": round(t_ms, 3)
        })
        print(f"N={n:<3} | 2^n: {2**n:<10} | Subsets: {count:<10} | BestVal: {bv:<6} | Time: {t_ms:<9.3f} ms")
    return results

# ==========================================
# Q7: DAY-4 DESIGN CHALLENGE (CLOSEST PAIR REDESIGN)
# ==========================================

def closest_pair_redesign_divide_conquer(points: List[Tuple[float, float]]) -> Tuple[Tuple[Tuple[float, float], Tuple[float, float]], float, int]:
    """Presorted Sweep-Line / Divide-and-Conquer Closest Pair O(n log n)."""
    calcs = [0]
    
    def dist(p1, p2):
        calcs[0] += 1
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])
        
    def recurse(px, py):
        n = len(px)
        if n <= 3:
            min_d = float('inf')
            pair = (px[0], px[1])
            for i in range(n - 1):
                for j in range(i + 1, n):
                    d = dist(px[i], px[j])
                    if d < min_d:
                        min_d = d
                        pair = (px[i], px[j])
            return pair, min_d
            
        mid = n // 2
        mid_x = px[mid][0]
        
        left_px = px[:mid]
        right_px = px[mid:]
        
        mid_point_set = set(left_px)
        left_py = [p for p in py if p in mid_point_set]
        right_py = [p for p in py if p not in mid_point_set]
        
        p1, d1 = recurse(left_px, left_py)
        p2, d2 = recurse(right_px, right_py)
        
        if d1 < d2:
            min_pair, delta = p1, d1
        else:
            min_pair, delta = p2, d2
            
        # Strip within delta of mid_x
        strip = [p for p in py if abs(p[0] - mid_x) < delta]
        for i in range(len(strip)):
            # Check at most next 7 points in sorted y strip
            for j in range(i + 1, min(i + 8, len(strip))):
                d = dist(strip[i], strip[j])
                if d < delta:
                    delta = d
                    min_pair = (strip[i], strip[j])
                    
        return min_pair, delta

    pts_x = sorted(points, key=lambda p: p[0])
    pts_y = sorted(points, key=lambda p: p[1])
    pair, min_d = recurse(pts_x, pts_y)
    return pair, min_d, calcs[0]

def run_q7():
    print("\n" + "=" * 60)
    print(" Q7: DAY-4 DESIGN CHALLENGE - CLOSEST PAIR REDESIGN")
    print("=" * 60)
    sizes = [100, 250, 500, 1000, 2000, 5000]
    results = []
    
    for n in sizes:
        rng = random.Random(42)
        points = [(rng.uniform(0, 5000), rng.uniform(0, 5000)) for _ in range(n)]
        
        # Original Brute Force O(n^2)
        t0 = time.perf_counter()
        _, d_orig, pairs_orig, dists_orig = brute_force_closest_pair(points)
        t_orig = (time.perf_counter() - t0) * 1000.0
        
        # Redesigned O(n log n)
        t0 = time.perf_counter()
        _, d_redesign, dists_redesign = closest_pair_redesign_divide_conquer(points)
        t_redesign = (time.perf_counter() - t0) * 1000.0
        
        reduction = (1.0 - (dists_redesign / dists_orig)) * 100.0
        results.append({
            "N": n, "Original_Calcs": dists_orig, "Redesigned_Calcs": dists_redesign,
            "Reduction_Pct": round(reduction, 2), "Original_Time_ms": round(t_orig, 3),
            "Redesigned_Time_ms": round(t_redesign, 3)
        })
        print(f"N={n:<5} | Orig Calcs: {dists_orig:<10} | Redesigned Calcs: {dists_redesign:<6} | Reduction: {reduction:<5.1f}% | Orig Time: {t_orig:<7.2f}ms | New Time: {t_redesign:<6.2f}ms")
        
    return results

def main():
    out_dir = Path(r"C:\Users\USER\.gemini\antigravity\scratch\CO2_Assignment\Supporting_Files\results")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    # Run and write CSVs
    q1_data = run_q1()
    with open(out_dir / "q1_sorting_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q1_data[0].keys())
        writer.writeheader()
        writer.writerows(q1_data)
        
    q2_data = run_q2()
    with open(out_dir / "q2_sequential_search_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q2_data[0].keys())
        writer.writeheader()
        writer.writerows(q2_data)

    q3_data = run_q3()
    with open(out_dir / "q3_string_matching_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q3_data[0].keys())
        writer.writeheader()
        writer.writerows(q3_data)

    q4_data = run_q4()
    with open(out_dir / "q4_brute_closest_pair_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q4_data[0].keys())
        writer.writeheader()
        writer.writerows(q4_data)

    q5_data = run_q5()
    with open(out_dir / "q5_convex_hull_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q5_data[0].keys())
        writer.writeheader()
        writer.writerows(q5_data)

    q6_data = run_q6()
    with open(out_dir / "q6_exhaustive_search_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q6_data[0].keys())
        writer.writeheader()
        writer.writerows(q6_data)

    q7_data = run_q7()
    with open(out_dir / "q7_redesign_comparison.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=q7_data[0].keys())
        writer.writeheader()
        writer.writerows(q7_data)

    # Plot 1: Q1 Sorting comparisons on 95% nearly sorted data
    nearly_q1 = [r for r in q1_data if r["Dataset"] == "Nearly_Sorted_95%"]
    sizes_q1 = sorted(list(set(r["N"] for r in nearly_q1)))
    sel_comps = [r["Comparisons"] for r in nearly_q1 if r["Algorithm"] == "Selection Sort"]
    bub_comps = [r["Comparisons"] for r in nearly_q1 if r["Algorithm"] == "Bubble Sort"]
    ins_comps = [r["Comparisons"] for r in nearly_q1 if r["Algorithm"] == "Insertion Sort"]
    
    plt.figure(figsize=(8, 5), dpi=300)
    plt.plot(sizes_q1, sel_comps, marker='o', label="Selection Sort (n(n-1)/2)")
    plt.plot(sizes_q1, bub_comps, marker='s', label="Bubble Sort")
    plt.plot(sizes_q1, ins_comps, marker='^', label="Insertion Sort (O(n) nearly sorted)")
    plt.title("Q1: Sorting Comparisons on 95% Nearly Sorted E-Commerce Orders", fontsize=12, fontweight='bold')
    plt.xlabel("Number of Orders N", fontsize=11)
    plt.ylabel("Comparisons", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "q1_sorting_comparisons.png")
    plt.close()

    # Plot 2: Q4 vs Q7 Closest Pair distance calculations
    sizes_q7 = [r["N"] for r in q7_data]
    orig_calcs = [r["Original_Calcs"] for r in q7_data]
    redes_calcs = [r["Redesigned_Calcs"] for r in q7_data]
    
    plt.figure(figsize=(8, 5), dpi=300)
    plt.plot(sizes_q7, orig_calcs, marker='o', color='red', label="Original Brute-Force O(n²)")
    plt.plot(sizes_q7, redes_calcs, marker='^', color='green', label="Redesigned Divide & Conquer O(n log n)")
    plt.title("Q7 vs Q4: Distance Calculations Comparison", fontsize=12, fontweight='bold')
    plt.xlabel("Number of Drones N", fontsize=11)
    plt.ylabel("Distance Calculations (Linear Scale)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "q4_q7_distance_calculations.png")
    plt.close()

    # Plot 3: Q6 Combinatorial explosion
    sizes_q6 = [r["N"] for r in q6_data]
    subsets_q6 = [r["Total_Subsets_2^N"] for r in q6_data]
    
    plt.figure(figsize=(8, 5), dpi=300)
    plt.plot(sizes_q6, subsets_q6, marker='s', color='purple', label="Candidate Subsets 2^n")
    plt.yscale('log')
    plt.title("Q6: Combinatorial Growth in Humanitarian Airlift Planning", fontsize=12, fontweight='bold')
    plt.xlabel("Number of Packages N", fontsize=11)
    plt.ylabel("Subsets Examined (Log Scale)", fontsize=11)
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "q6_subset_growth.png")
    plt.close()

    print("\n[✓] All experiments executed, CSVs written, and plots generated successfully.")

if __name__ == "__main__":
    main()
