from dataclasses import dataclass
from itertools import combinations
from typing import List, Tuple

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
