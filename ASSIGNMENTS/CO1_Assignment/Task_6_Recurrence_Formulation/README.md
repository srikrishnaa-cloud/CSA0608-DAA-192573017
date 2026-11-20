# Task 6 – Formulate the Recurrence Relation

## 1. Context and Derivation from Recursive Binary Search
For recursive divide-and-conquer algorithms, the execution time cannot be expressed as a simple iterative summation. Instead, it must be formulated as a **recurrence relation** that captures:
1. The base condition (when recursion halts).
2. The division of the input problem into subproblems.
3. The recursive invocation cost.
4. The non-recursive overhead (work performed outside the recursive call).

---

## 2. Step-by-Step Component Identification

Referencing our implementation of `recursive_binary_search(sorted_records, target, low, high)`:

### 2.1 Input Size of Original Problem
* Let $n$ be the number of records in the active search window, where:
  $$n = \text{high} - \text{low} + 1$$

### 2.2 Size of the Recursive Subproblem
* The algorithm determines the midpoint:
  $$\text{mid} = \text{low} + \lfloor (\text{high} - \text{low}) / 2 \rfloor$$
* Depending on whether $\text{target} < \text{records}[\text{mid}]$ or $\text{target} > \text{records}[\text{mid}]$, the search proceeds in either the left subarray $[low, mid - 1]$ or the right subarray $[mid + 1, high]$.
* The size of the subproblem is strictly at most:
  $$\lfloor n / 2 \rfloor$$

### 2.3 Number of Recursive Calls
* Crucially, although two recursive calls appear in the source code branches (`if ... else if ... else`), **exactly one** recursive call is executed per activation frame (binary search eliminates half the remaining search space on each step).
* Number of subproblems solved: $a = 1$.
* Subproblem division factor: $b = 2$.

### 2.4 Work Performed Outside the Recursive Call ($f(n)$)
* Evaluating base condition (`low > high`): $\mathcal{O}(1)$
* Midpoint index computation ($\text{mid} = \text{low} + \lfloor(\text{high}-\text{low})/2\rfloor$): $\mathcal{O}(1)$
* String key comparison ($\text{records}[\text{mid}].\text{reg\_no} == \text{target}$): $\mathcal{O}(1)$
* Argument passing and return branching: $\mathcal{O}(1)$
* Therefore, the non-recursive overhead is bounded by a constant $c$:
  $$f(n) = c = \Theta(1)$$

### 2.5 Base Case
* When the search range collapses such that $\text{low} > \text{high}$, the subproblem size is $n = 0$ (or $n = 1$ when a single element is checked directly).
* The function executes a constant number of comparisons and returns `NULL` or the matching record without further recursive descent:
  $$T(1) = c_0 = \Theta(1)$$

---

## 3. Formal Recurrence Formulation

Combining the components above, the exact recurrence relation governing the worst-case runtime $T(n)$ of Recursive Binary Search is:

$$
T(n) = 
\begin{cases} 
c_0 & \text{for } n = 1 \\ 
T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + c & \text{for } n > 1 
\end{cases}
$$

In standard asymptotic divide-and-conquer notation:
$$T(n) = T\left(\frac{n}{2}\right) + \Theta(1)$$
where:
* $a = 1$ (one subproblem)
* $b = 2$ (subproblem size halved)
* $f(n) = \Theta(1) = \Theta(n^0)$ (constant non-recursive work per step).
