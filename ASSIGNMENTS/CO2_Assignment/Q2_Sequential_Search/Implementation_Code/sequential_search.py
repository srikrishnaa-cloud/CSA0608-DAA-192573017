from dataclasses import dataclass
from typing import List, Optional, Tuple

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
