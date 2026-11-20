# Task 7 – Solve the Recurrence Relation

## Recurrence to Solve
From Task 6, the recurrence relation for the worst-case time complexity of Recursive Binary Search is:
$$T(n) = T\left(\frac{n}{2}\right) + c, \quad \text{with base condition } T(1) = c_0$$

Below, we provide complete, step-by-step analytical solutions using **three distinct mathematical techniques**:
1. **The Master Theorem** (Primary Method)
2. **The Iteration / Expansion Method**
3. **The Substitution / Mathematical Induction Method**

---

## Method 1: The Master Theorem

### 1.1 Applicability Justification
The standard Master Theorem applies to divide-and-conquer recurrences of the canonical form:
$$T(n) = a \, T\left(\frac{n}{b}\right) + f(n)$$
where $a \ge 1$, $b > 1$, and $f(n)$ is asymptotically positive.

For our recurrence $T(n) = T(n/2) + c$:
* $a = 1$ (number of recursive calls per level)
* $b = 2$ (input divisor factor)
* $f(n) = c = \Theta(1) = \Theta(n^0)$

All preconditions for the Master Theorem are strictly satisfied.

### 1.2 Step-by-Step Evaluation
1. Calculate the critical exponent:
   $$c_{\text{crit}} = \log_b a = \log_2 1 = 0$$
2. Compare $f(n)$ with $n^{\log_b a}$:
   $$n^{\log_b a} = n^0 = 1$$
   $$f(n) = \Theta(1) = \Theta(n^{\log_b a}) = \Theta(n^0)$$
3. Identify the applicable Master Theorem Case:
   * Since $f(n) = \Theta(n^{\log_b a})$, this matches **Case 2** of the Master Theorem (with $k = 0$).
4. Apply the Case 2 formula:
   $$T(n) = \Theta\left(n^{\log_b a} \log^{k+1} n\right) = \Theta\left(n^0 \log^{0+1} n\right) = \Theta(\log n)$$

**Conclusion via Master Theorem:**
$$T(n) = \Theta(\log n)$$

---

## Method 2: Iteration / Expansion Method

### 2.1 Applicability Justification
The Iteration Method repeatedly expands the recurrence backward until a recognizable algebraic summation pattern emerges, terminating at the base case $T(1)$.

### 2.2 Step-by-Step Expansion
Assume $n = 2^k$, which means $k = \log_2 n$.

* **Step 1:** Initial equation
  $$T(n) = T\left(\frac{n}{2}\right) + c$$
* **Step 2:** Substitute $T(n/2) = T(n/4) + c$
  $$T(n) = \left[ T\left(\frac{n}{4}\right) + c \right] + c = T\left(\frac{n}{4}\right) + 2c = T\left(\frac{n}{2^2}\right) + 2c$$
* **Step 3:** Substitute $T(n/4) = T(n/8) + c$
  $$T(n) = \left[ T\left(\frac{n}{8}\right) + c \right] + 2c = T\left(\frac{n}{2^3}\right) + 3c$$
* **Step $i$:** By mathematical induction on the expansion depth $i$:
  $$T(n) = T\left(\frac{n}{2^i}\right) + i \cdot c$$

### 2.3 Reaching the Base Case
The iteration terminates when the subproblem size reaches the base case:
$$\frac{n}{2^k} = 1 \implies 2^k = n \implies k = \log_2 n$$

Substitute $i = k = \log_2 n$ into the general formula:
$$T(n) = T(1) + (\log_2 n) \cdot c$$
Given $T(1) = c_0$:
$$T(n) = c_0 + c \cdot \log_2 n$$

Taking the asymptotic limit as $n \to \infty$:
$$T(n) = \Theta(\log_2 n) = \Theta(\log n)$$

---

## Method 3: Substitution Method (Mathematical Induction)

### 3.1 Applicability Justification
The Substitution Method guesses the form of the mathematical solution based on inspection and proves it holds for all $n \ge n_0$ using mathematical induction.

### 3.2 Inductive Hypothesis
* **Guess:** $T(n) \le d \log_2 n$ for some constant $d > 0$.

### 3.3 Inductive Step
Assume the hypothesis holds for all subproblem sizes smaller than $n$, specifically for $n/2$:
$$T\left(\frac{n}{2}\right) \le d \log_2\left(\frac{n}{2}\right)$$

Substitute into the original recurrence:
$$T(n) = T\left(\frac{n}{2}\right) + c$$
$$T(n) \le d \log_2\left(\frac{n}{2}\right) + c$$
Using logarithmic identities $\log_2(n/2) = \log_2 n - \log_2 2 = \log_2 n - 1$:
$$T(n) \le d (\log_2 n - 1) + c = d \log_2 n - d + c$$

For the inductive hypothesis $T(n) \le d \log_2 n$ to hold:
$$d \log_2 n - d + c \le d \log_2 n$$
$$-d + c \le 0 \implies d \ge c$$

Thus, choosing any constant $d \ge c$ satisfies the inequality for all $n \ge 2$.

### 3.4 Base Case Verification
For $n = 2$: $T(2) = T(1) + c = c_0 + c$.
We require $c_0 + c \le d \log_2(2) = d$, which holds whenever $d \ge c_0 + c$.
Both the inductive step and base case hold, formally proving:
$$T(n) = O(\log n)$$

Similarly, proving $T(n) \ge d' \log_2 n$ yields $\Omega(\log n)$, establishing the tight bound $\Theta(\log n)$.

---

## 4. Interpretation of the Result
* **Sub-linear Scaling:** The growth rate $O(\log n)$ is strictly sub-linear. Doubling the dataset size $n \to 2n$ merely adds a constant execution penalty $c$:
  $$T(2n) = c \log_2(2n) = c(\log_2 n + 1) = T(n) + c$$
* **Practical Implication:** In an academic institution with $1,000,000$ student records, Recursive Binary Search guarantees resolution in no more than $\approx 20$ recursive levels ($2^{20} = 1,048,576$).
