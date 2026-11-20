# Task 4 – Analyse Best, Average and Worst-Case Behaviour

## Overview of Input Conditions
An algorithm's runtime fluctuates based on the distribution and position of the query key within the database. We analyze the input configurations that trigger the **Best**, **Average**, and **Worst** case scenarios for each of the three searching strategies.

---

## 1. Iterative Linear Search

### 1.1 Best-Case Scenario
* **Input Condition:** The requested student registration number happens to be stored at the very first position of the array ($\text{records}[0]$).
* **Number of Operations:** Exactly $1$ key comparison ($C_{\text{best}} = 1$).
* **Time Complexity:** $\Omega(1)$ / $O(1)$.
* **Why this occurs:** The loop test on the first iteration evaluates to `true`, and the function returns immediately without further traversal.

### 1.2 Worst-Case Scenario
* **Input Condition:** The requested student registration number is either located at the final index ($\text{records}[n-1]$) or does **not exist** anywhere in the database.
* **Number of Operations:** Exactly $n$ comparisons ($C_{\text{worst}} = n$).
* **Time Complexity:** $O(n)$ / $\mathcal{O}(n)$.
* **Why this occurs:** In an unsorted collection with no structural indices, absence can only be confirmed by exhausting all $n$ candidate positions.

### 1.3 Average-Case Scenario
* **Input Condition:** The requested student record is present with equal probability across all $n$ positions, or uniformly absent with probability $p$.
* **Number of Operations:**
  $$C_{\text{avg}} = \frac{n + 1}{2} \approx 0.5n$$
* **Time Complexity:** $\Theta(n)$.
* **Why this occurs:** On average, a sequential scan examines half the dataset before encountering the target.

---

## 2. Recursive Binary Search

### 2.1 Best-Case Scenario
* **Input Condition:** The target registration number corresponds exactly to the record stored at the initial midpoint index:
  $$\text{mid}_0 = \left\lfloor \frac{0 + n - 1}{2} \right\rfloor$$
* **Number of Operations:** Exactly $1$ key comparison ($C_{\text{best}} = 1$).
* **Time Complexity:** $\Omega(1)$ / $O(1)$.
* **Why this occurs:** The initial check `sorted_records[mid].reg_no == target` succeeds on the root activation frame, returning without any recursive branching.

### 2.2 Worst-Case Scenario
* **Input Condition:** The target key is absent from the database, or lies at the deepest leaf level of the binary decision tree (e.g., at the extreme ends or between two adjacent values).
* **Number of Operations:** The search window is continually halved until $low > high$:
  $$C_{\text{worst}} = \lfloor \log_2 n \rfloor + 1$$
* **Time Complexity:** $O(\log n)$.
* **Why this occurs:** The algorithm must navigate through the full depth of the decision tree before reaching the base condition.

### 2.3 Average-Case Scenario
* **Input Condition:** The target is equally likely to be any of the $n$ distinct records stored in the sorted array.
* **Number of Operations:**
  $$C_{\text{avg}} \approx \log_2(n) - 1$$
* **Time Complexity:** $\Theta(\log n)$.
* **Why this occurs:** Because the majority of nodes in a complete binary tree reside in the bottom two levels (level $h$ has roughly $n/2$ nodes), almost all successful searches require between $\log_2(n) - 1$ and $\log_2(n)$ comparisons.

---

## 3. Hash Table Search (Chained Hashing)

### 3.1 Best-Case Scenario
* **Input Condition:** The target key hashes to a bucket that is non-empty, and the target record is the **head** (first node) of that bucket's collision chain.
* **Number of Operations:** $1$ hash evaluation + $1$ key comparison ($C_{\text{best}} = 1$).
* **Time Complexity:** $\Omega(1)$ / $O(1)$.
* **Why this occurs:** Direct bucket indexing resolves immediately in $O(1)$, and zero collision traversal is required.

### 3.2 Worst-Case Scenario
* **Input Condition:** Pathological collision distribution where **all $n$ records hash into the exact same bucket** (e.g. poor hash function or adversarial key collision attacks), degenerating the chain into a linked list of length $n$.
* **Number of Operations:** $n$ key comparisons ($C_{\text{worst}} = n$).
* **Time Complexity:** $O(n)$.
* **Why this occurs:** When all elements collide, searching degrades to linear search through the singly-linked collision chain.

### 3.3 Average-Case Scenario
* **Input Condition:** The hash function distributes keys uniformly across $m$ buckets according to the Simple Uniform Hashing Assumption (SUHA).
* **Number of Operations:**
  $$C_{\text{avg}} = 1 + \frac{\alpha}{2} = 1 + \frac{n}{2m}$$
  For load factor $\alpha \approx 0.75$, $C_{\text{avg}} \approx 1.375$ comparisons.
* **Time Complexity:** $\Theta(1)$.
* **Why this occurs:** Collisions are uniformly minimized; the expected chain length is small and bounded by a constant.

---

## Comprehensive Case Analysis Comparison

| Algorithm | Best-Case Input | Best $C(n)$ | Average-Case Input | Avg $C(n)$ | Worst-Case Input | Worst $C(n)$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | First array position | $1$ | Uniform random position | $\frac{n+1}{2}$ | Final position or missing | $n$ |
| **Recursive Binary Search** | Middle array position | $1$ | Uniform random position | $\approx \log_2 n - 1$ | Missing or deepest leaf | $\lfloor \log_2 n \rfloor + 1$ |
| **Hash Table** | Head of bucket chain | $1$ | Uniform key distribution | $1 + \frac{\alpha}{2}$ | All $n$ keys in 1 bucket | $n$ |
