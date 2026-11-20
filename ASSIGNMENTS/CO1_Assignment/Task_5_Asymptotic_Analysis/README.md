# Task 5 – Perform Asymptotic Analysis

## Theoretical Definitions of Asymptotic Notations

Asymptotic notation describes the limiting behavior of an execution-time function $T(n)$ as input size $n$ approaches infinity ($n \to \infty$):

1. **Big-O Notation ($O$): Asymptotic Upper Bound**
   $$f(n) = O(g(n)) \iff \exists c > 0, n_0 \ge 1 \text{ such that } 0 \le f(n) \le c \cdot g(n), \, \forall n \ge n_0$$
   Represents the guaranteed worst-case execution envelope.

2. **Big-Omega Notation ($\Omega$): Asymptotic Lower Bound**
   $$f(n) = \Omega(g(n)) \iff \exists c > 0, n_0 \ge 1 \text{ such that } 0 \le c \cdot g(n) \le f(n), \, \forall n \ge n_0$$
   Represents the best-case execution floor.

3. **Big-Theta Notation ($\Theta$): Asymptotically Tight Bound**
   $$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n))$$
   $$\exists c_1, c_2 > 0, n_0 \ge 1 \text{ such that } c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n), \, \forall n \ge n_0$$

---

## 1. Asymptotic Comparison of Proposed Algorithms

### 1.1 Summary Matrix

| Algorithm | Best-Case Bound | Worst-Case Bound | Average-Case Bound | Tight Bound ($\Theta$) on Search |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $\Omega(1)$ | $O(n)$ | $\Theta(n)$ | $\Theta(n)$ (overall average) |
| **Recursive Binary Search** | $\Omega(1)$ | $O(\log n)$ | $\Theta(\log n)$ | $\Theta(\log n)$ (overall average) |
| **Hash Table Search** | $\Omega(1)$ | $O(n)$ (pathological) | $\Theta(1)$ (expected) | $\Theta(1)$ (amortized/expected) |

---

## 2. Growth Rates When Scaling: $1,000 \to 1,000,000+$ Records

To interpret what these asymptotic growth rates mean in the real university student record system, consider scaling the database from $1,000$ to $1,000,000$ records (a **$1,000\times$ increase**):

### 2.1 Impact on Linear Search ($O(n)$)
* For $n = 1,000$: Average operations $\approx 500$.
* For $n = 1,000,000$: Average operations $\approx 500,000$.
* **Scaling Impact:** A $1,000\times$ increase in database size results in an exact **$1,000\times$ increase** in query execution time. 
* At high query volumes (e.g. 50,000 searches/hour), Linear Search suffers catastrophic CPU saturation.

### 2.2 Impact on Recursive Binary Search ($O(\log n)$)
* For $n = 1,000$: Operations $\approx \log_2(1,000) \approx 10$ comparisons.
* For $n = 1,000,000$: Operations $\approx \log_2(1,000,000) \approx 20$ comparisons.
* **Scaling Impact:** While the data grew by **$1,000\times$ (100,000%)**, the comparison count only **doubled** (from 10 to 20). 
* This illustrates the immense power of logarithmic scalability for large-scale enterprise databases.

### 2.3 Impact on Hash Table Search ($O(1)$)
* For $n = 1,000$: Operations $\approx 1 + \alpha/2 \approx 1.37$ comparisons.
* For $n = 1,000,000$: Operations $\approx 1 + \alpha/2 \approx 1.37$ comparisons (with dynamic bucket sizing $m \propto n$).
* **Scaling Impact:** Zero asymptotic growth. Query latency remains virtually identical whether the institution holds 1,000 students or 10,000,000 students.

---

## Comparative Operational Scale Table

| Database Size ($n$) | Linear Search ($0.5n$) | Binary Search ($\log_2 n$) | Hash Table ($1 + \alpha/2$) | Relative Speedup (Hash vs Linear) |
| :--- | :--- | :--- | :--- | :--- |
| **$1,000$** | $500$ | $10$ | $1.37$ | $365\times$ |
| **$10,000$** | $5,000$ | $13$ | $1.37$ | $3,650\times$ |
| **$100,000$** | $50,000$ | $17$ | $1.37$ | $36,500\times$ |
| **$1,000,000$** | $500,000$ | $20$ | $1.37$ | **$365,000\times$** |
