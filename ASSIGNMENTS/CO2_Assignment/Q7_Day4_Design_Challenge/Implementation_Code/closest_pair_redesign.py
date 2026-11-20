import math
from typing import List, Tuple

def closest_pair_redesign_divide_conquer(points: List[Tuple[float, float]]):
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
        
        mid_set = set(left_px)
        left_py = [p for p in py if p in mid_set]
        right_py = [p for p in py if p not in mid_set]
        
        p1, d1 = recurse(left_px, left_py)
        p2, d2 = recurse(right_px, right_py)
        
        min_pair, delta = (p1, d1) if d1 < d2 else (p2, d2)
        
        strip = [p for p in py if abs(p[0] - mid_x) < delta]
        for i in range(len(strip)):
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
