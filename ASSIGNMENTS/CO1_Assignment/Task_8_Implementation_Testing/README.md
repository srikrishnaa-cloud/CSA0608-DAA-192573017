# Task 8 – Implement and Test the Algorithms

## 1. Overview and Implementation Details
The benchmarking and testing suite is implemented in Python 3 under `Task_8_Implementation_Testing/Source_Code/student_record_search.py`. It provides exact, mathematically rigorous implementations of all three search paradigms:
1. **Iterative Linear Search** (`linear_search`)
2. **Recursive Binary Search** (`recursive_binary_search`, `binary_search_wrapper`)
3. **Hash Table with Chaining** (`StudentHashTable`, `HashTableSearch`)

### 1.1 Data Structure Representation
Each student record is stored using Python's high-efficiency slotted `@dataclass`:
```python
@dataclass(slots=True)
class StudentRecord:
    reg_no: str       # Unique Alphanumeric Key, e.g. "REG000123"
    student_id: int   # Numeric ID
    name: str         # Full Student Name
    dept: str         # Department Code (CSE, ECE, IT, etc.)
    cgpa: float       # Cumulative GPA
```

---

## 2. Source Code Architecture

```
Task_8_Implementation_Testing/
├── README.md
└── Source_Code/
    └── student_record_search.py
```

### 2.1 Key Implementation Snippets

#### A. Iterative Linear Search
```python
def linear_search(records: List[StudentRecord], target: str) -> Tuple[Optional[StudentRecord], int]:
    comparisons = 0
    for record in records:
        comparisons += 1
        if record.reg_no == target:
            return record, comparisons
    return None, comparisons
```

#### B. Recursive Binary Search
```python
def recursive_binary_search(
    sorted_records: List[StudentRecord],
    target: str,
    low: int,
    high: int,
    counter: ComparisonCounter
) -> Optional[StudentRecord]:
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
```

#### C. Hash Table Search (Separate Chaining)
```python
class StudentHashTable:
    def __init__(self, capacity: int):
        self.capacity = max(capacity, 1024)
        self.buckets: List[List[StudentRecord]] = [[] for _ in range(self.capacity)]
        self.size = 0

    def _hash(self, key: str) -> int:
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
```

---

## 3. Testing and Verification Protocol

To ensure reproducible, unbiased, and mathematically valid testing:
1. **Target Datasets:** Evaluated across four orders of magnitude:
   $$n \in \{1\,000,\; 10\,000,\; 100\,000,\; 1\,000\,000\}$$
2. **Identical Datasets:** The exact same synthetic dataset generated with fixed pseudo-random seed (`seed=42`) is utilized across all algorithms.
3. **Timer Precision:** Execution intervals are measured using `time.perf_counter()`, offering sub-microsecond resolution.
4. **Boundary & Correctness Checks:**
   * **Target at First Position:** Verified $O(1)$ best-case behavior.
   * **Target at Midpoint:** Verified $O(1)$ binary search midpoint trigger.
   * **Target Missing (`REG_NON_EXISTENT_999999`):** Verified boundary behavior under total search space exhaustion.
   * **Correctness Assertion:** Verified that returned record matches the query `reg_no` across all sample queries.

---

## 4. Execution Command
To run the automated benchmark suite:
```bash
python Task_8_Implementation_Testing/Source_Code/student_record_search.py --sizes 1000 10000 100000 1000000 --queries 30 --output Report/Tables_and_Graphs
```
