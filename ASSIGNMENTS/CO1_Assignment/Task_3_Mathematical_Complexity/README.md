# Task 3 – Derive the Time-Complexity Function Mathematically

## Mathematical Framework
Let $n$ represent the total number of student records in the database.
Let $C(n)$ denote the number of basic operations executed by the search procedure.
Let $T_{\text{search}}(n)$ be the query running time.
Let $T_{\text{prep}}(n)$ represent any mandatory one-time preprocessing cost (sorting or index construction).
The total computational cost for $Q$ search requests is expressed as:
$$T_{\text{total}}(n, Q) = T_{\text{prep}}(n) + Q \times T_{\text{search}}(n)$$

---

## 1. Iterative Linear Search

### 1.1 Derivation of Basic Operation Count $C(n)$
In Linear Search, records are inspected sequentially:
* **Worst Case ($C_{\text{worst}}$):** The target is either at the final index ($n-1$) or not present in the database. The algorithm iterates through all $n$ items:
  $$C_{\text{worst}}(n) = \sum_{i=1}^{n} 1 = n$$
* **Best Case ($C_{\text{best}}$):** The target record is located at the first index ($i = 0$):
  $$C_{\text{best}}(n) = 1$$
* **Average Case ($C_{\text{avg}}$):** Assuming all $n$ records are equally likely to be searched with probability $P(\text{target} = \text{records}[i]) = \frac{1}{n}$:
  $$C_{\text{avg}}(n) = \sum_{i=1}^{n} i \cdot P(\text{target} = \text{records}[i]) = \frac{1}{n} \sum_{i=1}^{n} i = \frac{1}{n} \left( \frac{n(n + 1)}{2} \right) = \frac{n + 1}{2}$$

### 1.2 Running Time Expression
With each basic operation taking constant execution time $c_1$ and overhead $c_0$:
$$T_{\text{search}}(n) = c_1 \cdot C(n) + c_0 = c_1 \left(\frac{n + 1}{2}\right) + c_0 = \Theta(n)$$

### 1.3 Preprocessing and Total Cost
* **Preprocessing Cost:** $T_{\text{prep}}(n) = 0$ (Records can be loaded in raw, unsorted order).
* **Total Cost for $Q$ queries:**
  $$T_{\text{total}}(n, Q) = 0 + Q \times \left( c_1 \frac{n+1}{2} + c_0 \right) = \Theta(Q \cdot n)$$

---

## 2. Recursive Binary Search

### 2.1 Derivation of Basic Operation Count $C(n)$
Binary search operates on a sorted array of size $n$. At each step, the search interval $[low, high]$ of size $k$ is reduced to $\lfloor k/2 \rfloor$:
* Let $k$ be the size of the search space.
* Initial size: $n$.
* After step 1: $\lfloor n/2 \rfloor$.
* After step 2: $\lfloor n/4 \rfloor = \lfloor n/2^2 \rfloor$.
* After step $k$: $\lfloor n/2^k \rfloor$.

The algorithm terminates when the interval size becomes $1$, i.e., $\frac{n}{2^k} \le 1 \implies 2^k \ge n \implies k = \lceil \log_2 n \rceil$.

* **Best Case:** The target is located at the very first midpoint $\lfloor (0 + n - 1)/2 \rfloor$:
  $$C_{\text{best}}(n) = 1$$
* **Worst Case:** The target is at an external node / leaf node or not present at all. The recursion proceeds to maximum depth:
  $$C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1$$
* **Average Case:** Using the internal path length of an optimal binary decision tree with $n$ keys:
  $$C_{\text{avg}}(n) = \frac{1}{n} \sum_{i=1}^{n} (\text{depth}(i) + 1) \approx \log_2(n) - 1 + \frac{1}{n}$$
  As $n \to \infty$, $C_{\text{avg}}(n) \approx \log_2 n - 1$.

### 2.2 Running Time Expression
$$T_{\text{search}}(n) = c_2 \cdot \log_2 n + c_3 = \Theta(\log n)$$

### 2.3 Preprocessing and Total Cost
* **Preprocessing Cost:** An unsorted database must first be sorted. Using Mergesort or Quicksort:
  $$T_{\text{prep}}(n) = c_{\text{sort}} \cdot n \log_2 n = \Theta(n \log n)$$
* **Total Cost for $Q$ queries:**
  $$T_{\text{total}}(n, Q) = c_{\text{sort}} n \log_2 n + Q \cdot (c_2 \log_2 n + c_3) = \Theta(n \log n + Q \log n)$$

---

## 3. Hash Table Search (Chained Hashing)

### 3.1 Derivation of Basic Operation Count $C(n)$
Let $m$ be the number of buckets in the hash table and $n$ be the number of stored student records.
The **load factor** is defined as:
$$\alpha = \frac{n}{m}$$

* **Unsuccessful Search (Worst Case for a bucket):** 
  Under the Simple Uniform Hashing Assumption (SUHA), any key is equally likely to hash into any of the $m$ slots. The expected length of a chain at any bucket is $\alpha$. Thus, an unsuccessful search examines the entire chain:
  $$E[C_{\text{unsuccessful}}] = \alpha = \frac{n}{m}$$
* **Successful Search (Average Case):**
  A successful search expects to find the key halfway down the chain:
  $$E[C_{\text{successful}}] = 1 + \frac{\alpha}{2}$$
* With dynamic rehashing keeping $\alpha = \mathcal{O}(1)$ (typically $\alpha \le 0.75$):
  $$C(n) \le 1 + \frac{0.75}{2} = 1.375 = \mathcal{O}(1)$$

### 3.2 Running Time Expression
$$T_{\text{search}}(n) = c_{\text{hash}} + c_4 \left(1 + \frac{\alpha}{2}\right) = \Theta(1) \quad (\text{when } \alpha \text{ is constant})$$

### 3.3 Preprocessing and Total Cost
* **Preprocessing Cost:** Inserting $n$ elements into the hash table of size $m = \Theta(n)$:
  $$T_{\text{prep}}(n) = \sum_{i=1}^{n} \mathcal{O}(1) = \Theta(n)$$
* **Total Cost for $Q$ queries:**
  $$T_{\text{total}}(n, Q) = c_{\text{build}} \cdot n + Q \cdot c_{\text{lookup}} = \Theta(n + Q)$$

---

## Mathematical Comparison Summary

| Metric | Linear Search | Recursive Binary Search | Hash Table Search |
| :--- | :--- | :--- | :--- |
| **Basic Op Count $C(n)$** | $\frac{n+1}{2}$ | $\approx \log_2 n$ | $1 + \frac{\alpha}{2} \approx 1.37$ |
| **Search Time $T_{\text{search}}(n)$** | $\Theta(n)$ | $\Theta(\log n)$ | $\Theta(1)$ expected |
| **Preprocessing Cost $T_{\text{prep}}(n)$** | $0$ (None) | $\Theta(n \log n)$ | $\Theta(n)$ |
| **Amortized Cost for $Q$ searches** | $\mathcal{O}(Q \cdot n)$ | $\mathcal{O}(n \log n + Q \log n)$ | $\mathcal{O}(n + Q)$ |
| **Breakeven Point ($Q$) vs Linear** | $0$ | $Q > \frac{n \log n}{n - \log n} \approx \log_2 n$ | $Q > \frac{n}{n - 1} \approx 1$ |
