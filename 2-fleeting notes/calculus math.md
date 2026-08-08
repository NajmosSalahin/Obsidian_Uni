## Prove: A Polynomial with Positive Coefficients is Increasing

---

### The General Polynomial

Let the polynomial be:

$$y = a_1x^n + a_2x^{n-1} + a_3x^{n-2} + \cdots + a_nx^1 + a_{n+1}x^0$$

where all coefficients $a_1, a_2, a_3, \ldots, a_{n+1} > 0$

---

### Step 1 — Differentiate

$$\frac{dy}{dx} = a_1nx^{n-1} + a_2(n-1)x^{n-2} + a_3(n-2)x^{n-3} + \cdots + a_n + 0$$

The constant term $a_{n+1}x^0$ disappears (derivative of a constant = 0).

---

### Step 2 — Analyze the Sign

Two conditions hold:

|Condition|Reason|
|---|---|
|All coefficients $a_1, a_2, \ldots > 0$|Given|
|All powers of x are even or $x^0$ after differentiation, so $x^{n-1}, x^{n-2}, \ldots \geq 0$|For a polynomial, $n \geq 0$|
|All multiplied factors $(n), (n-1), (n-2)\ldots \geq 0$|Since $n \geq 0$|

So every single term in $\frac{dy}{dx}$ is:

$$\underbrace{a_i}_{>0} \times \underbrace{(n-i+1)}_{\geq 0} \times \underbrace{x^{n-i}}_{\geq 0} \geq 0$$

---

### Step 3 — Conclude

$$\frac{dy}{dx} \geq 0 \quad \text{for all } x \geq 0$$

Therefore, **a polynomial with positive coefficients is a monotonically increasing function.** ✅

---

### Quick Concrete Example

$$y = 3x^3 + 5x^2 + 2x + 7$$

$$\frac{dy}{dx} = 9x^2 + 10x + 2$$

All coefficients positive → $\frac{dy}{dx} \geq 0$ → **increasing** ✅
