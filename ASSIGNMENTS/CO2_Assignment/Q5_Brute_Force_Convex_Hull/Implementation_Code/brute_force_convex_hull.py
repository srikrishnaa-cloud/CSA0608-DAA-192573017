from typing import List, Tuple

def orientation(p1, p2, p3) -> float:
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def brute_force_convex_hull(points: List[Tuple[float, float]]):
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
                if abs(cross) < 1e-9:
                    continue
                sign = 1 if cross > 0 else -1
                if first_sign is None:
                    first_sign = sign
                elif sign != first_sign:
                    valid_edge = False
                    break
                    
            if valid_edge and first_sign is not None:
                hull_edges.append((p1, p2))
                
    return hull_edges, tests_performed
