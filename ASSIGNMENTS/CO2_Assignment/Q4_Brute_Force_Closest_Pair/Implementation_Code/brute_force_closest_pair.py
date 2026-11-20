import math
from typing import List, Tuple

def brute_force_closest_pair(points: List[Tuple[float, float]]):
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
