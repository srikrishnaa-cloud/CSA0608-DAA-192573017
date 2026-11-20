# Task 2 – Identify the Basic Operation

## Conceptual Definition of Basic Operation
In algorithmic analysis, the **basic operation** is the single computational step within an algorithm that contributes most predominantly to its overall total running time. As the input size $n$ approaches infinity ($n \to \infty$), the execution frequency of the basic operation grows at the same asymptotic rate as the total execution time:
$$T(n) \approx c_{\text{op}} \times C(n)$$
where $c_{\text{op}}$ is the constant execution time of one basic operation, and $C(n)$ is the count of basic operations executed.

---

## 1. Iterative Linear Search

### 1.1 Identification
* **Basic Operation:** String equality comparison between the query key and the student record key:
  $$\text{records}[i].\text{reg\_no} == \text{target}$$

### 1.2 Location in Algorithm
* It resides directly inside the innermost loop body (`for i = 0 to n - 1`).

### 1.3 Justification for Selection
* Loop index increments and bounds checks (`i < n`) are executed in constant time lockstep with the equality comparison.
* The string comparison operation involves reading string memory and checking characters lexicographically, dominating the CPU instruction cycles compared to integer register incrementing.
* The number of key comparisons directly dictates how many loop iterations are performed before termination.

### 1.4 Growth Behavior as $n$ Increases
* If the target is at position $k$, the operation executes $k$ times.
* For a successful search uniformly distributed across $n$ records, the expected number of comparisons is:
  $$C_{\text{avg}}(n) = \frac{n + 1}{2}$$
* In the worst case (target not present), it executes exactly $n$ times. Thus, the operation count scales strictly **linearly** with $n$:
  $$C(n) \propto n$$

---

## 2. Recursive Binary Search

### 2.1 Identification
* **Basic Operation:** Three-way key comparison (or two binary checks: equality and relational order):
  $$\text{sorted\_records}[\text{mid}].\text{reg\_no} \lessgtr \text{target}$$

### 2.2 Location in Algorithm
* Located inside the recursive function activation frame immediately following midpoint calculation:
  $$\text{mid} \leftarrow \text{low} + \lfloor(\text{high} - \text{low})/2\rfloor$$

### 2.3 Justification for Selection
* Midpoint calculation and boundary assignments (`mid - 1`, `mid + 1`) take strictly constant time $O(1)$.
* Each recursive call executes exactly one three-way key comparison before deciding whether to terminate or branch into a subproblem of size $\lfloor n/2 \rfloor$.
* Therefore, the total count of key comparisons directly bounds the recursion depth of the call stack.

### 2.4 Growth Behavior as $n$ Increases
* With each execution of the basic operation, the remaining search window is halved:
  $$n \to \frac{n}{2} \to \frac{n}{4} \to \dots \to 1$$
* The maximum number of executions in the worst case (element missing or at a leaf) is:
  $$C_{\text{worst}}(n) = \lfloor \log_2 n \rfloor + 1$$
* As $n$ grows from $1,000$ to $1,000,000$, the basic operation count only increases from $\approx 10$ to $\approx 20$, exhibiting **logarithmic growth**:
  $$C(n) \propto \log_2 n$$

---

## 3. Hash Table Search (Chained Hashing)

### 3.1 Identification
* **Basic Operation:** Key equality comparison during bucket chain traversal:
  $$\text{node}.\text{reg\_no} == \text{target}$$
  *(accompanied by the initial hash evaluation $h(\text{target})$)*

### 3.2 Location in Algorithm
* Located within the linear traversal of the collision chain corresponding to bucket index $\text{hash}(\text{target}) \pmod m$.

### 3.3 Justification for Selection
* The hash calculation $h(\text{target})$ executes in $O(L)$ where $L$ is string length (a constant for fixed-length registration numbers like `REG123456`).
* Once the bucket is resolved in $O(1)$, the bottleneck becomes traversing the linked list / bucket chain and checking equality with stored records.

### 3.4 Growth Behavior as $n$ Increases
* Under the assumption of **Simple Uniform Hashing**, keys are distributed uniformly across $m$ buckets.
* The average chain length is the load factor:
  $$\alpha = \frac{n}{m}$$
* When table capacity $m$ is maintained proportional to $n$ (dynamic resizing maintaining $\alpha \le 0.75$), the expected number of comparisons is:
  $$C_{\text{avg}}(n) = 1 + \frac{\alpha}{2} = 1 + \frac{0.75}{2} = 1.375$$
* Thus, the basic operation count remains **constant** $O(1)$, independent of $n$ even as $n$ reaches $1,000,000+$.

---

## Comparative Matrix of Basic Operations

| Algorithm | Basic Operation | Location | Growth Rate $C(n)$ | Operation Count for $n = 10^6$ (Worst Case) |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | Key Equality Comparison | Inside sequential loop | Linear $O(n)$ | $1,000,000$ comparisons |
| **Recursive Binary Search** | Three-way Key Comparison | Inside recursive frame | Logarithmic $O(\log n)$ | $20$ comparisons |
| **Hash Table Search** | Chain Node Key Comparison | Inside bucket chain traversal | Constant $O(1)$ expected | $\approx 1 - 3$ comparisons (expected) |
