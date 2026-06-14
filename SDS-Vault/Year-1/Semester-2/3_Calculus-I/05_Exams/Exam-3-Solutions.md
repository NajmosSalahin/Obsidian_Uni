# Exam-3 Solutions

> **Legend:** Parts marked **[AI generated]** were not found in the lecture notes. Content labeled **[From notes]** is taken verbatim from the notes.

---

### 1. Sketch the graphs where the following functions are increasing or decreasing: **[25]**

*Note: The questions.md lists "the following functions" but does not specify particular functions. Below are three representative examples covering the key concepts of increasing/decreasing functions, with sketches described in detail.*

**The increasing/decreasing definitions and theorem are from notes. The function choices and example computations below are [AI generated].**

**(a) f(x) = x² − 4x + 3**

**Function:** f(x) = x² − 4x + 3

**Domain:** All real numbers

**Derivative:** f'(x) = 2x − 4 = 2(x − 2)

**Critical point:** x = 2

**Sign analysis of f':**
- For x < 2: f'(x) < 0 → f is **decreasing**
- For x > 2: f'(x) > 0 → f is **increasing**

**Key points:**
- Vertex (minimum): f(2) = 4 − 8 + 3 = −1 → point (2, −1)
- y-intercept: f(0) = 3 → point (0, 3)
- x-intercepts: x² − 4x + 3 = 0 → (x−1)(x−3) = 0 → x = 1, 3

**Graph description:** A parabola opening upward with vertex at (2, −1). The graph decreases from x = −∞ to x = 2, reaching a minimum at (2, −1), then increases from x = 2 to x = +∞.

```
y
|
|    3
|   / \
|  /   \
| /     \
|/       \
|  (2,-1)
|__________________ x
```

---

**(b) f(x) = x³ − 3x + 2**

**Function:** f(x) = x³ − 3x + 2

**Domain:** All real numbers

**Derivative:** f'(x) = 3x² − 3 = 3(x² − 1) = 3(x−1)(x+1)

**Critical points:** x = −1, x = 1

**Sign analysis of f':**
- For x < −1: f'(x) > 0 → f is **increasing**
- For −1 < x < 1: f'(x) < 0 → f is **decreasing**
- For x > 1: f'(x) > 0 → f is **increasing**

**Key points:**
- Local maximum at x = −1: f(−1) = −1 + 3 + 2 = 4 → point (−1, 4)
- Local minimum at x = 1: f(1) = 1 − 3 + 2 = 0 → point (1, 0)
- y-intercept: f(0) = 2 → point (0, 2)

**Graph description:** A cubic function that rises from −∞ to a local maximum at (−1, 4), then falls to a local minimum at (1, 0), then rises again to +∞.

```
y
|
|    4 (−1,4)
|   /|\
|  / | \
| /  |  \
|/   |   \
|   (0,2) \ (1,0)
|__________________ x
```

---

**(c) f(x) = x⁴ − 8x²**

**Function:** f(x) = x⁴ − 8x²

**Domain:** All real numbers

**Derivative:** f'(x) = 4x³ − 16x = 4x(x² − 4) = 4x(x−2)(x+2)

**Critical points:** x = −2, x = 0, x = 2

**Sign analysis of f':**
- For x < −2: f'(x) < 0 → f is **decreasing**
- For −2 < x < 0: f'(x) > 0 → f is **increasing**
- For 0 < x < 2: f'(x) < 0 → f is **decreasing**
- For x > 2: f'(x) > 0 → f is **increasing**

**Key points:**
- Local minimum at x = −2: f(−2) = 16 − 32 = −16 → point (−2, −16)
- Local maximum at x = 0: f(0) = 0 → point (0, 0)
- Local minimum at x = 2: f(2) = 16 − 32 = −16 → point (2, −16)
- x-intercepts: x⁴ − 8x² = x²(x² − 8) = 0 → x = 0, x = ±2√2

**Graph description:** A quartic (W-shaped) function with two minima at (−2, −16) and (2, −16), and a local maximum at (0, 0). The function decreases on (−∞, −2), increases on (−2, 0), decreases on (0, 2), and increases on (2, ∞).

```
y
|
|    (0,0)
|   /     \
|  /       \
| /         \
|/           \
|  (−2,−16)  (2,−16)
|__________________ x
```

---

### 2. Find the limiting value of the given function as x approaches 3? **[20]**

**[AI generated] — Not found in notes. The questions.md also does not specify a function.*

*Below we evaluate the limit for several common types of functions as x → 3.*

---

**(a) Polynomial function:** lim_{x→3} (x² − 2x + 1)

For a polynomial, we can directly substitute x = 3:

= (3)² − 2(3) + 1 = 9 − 6 + 1 = **4**

---

**(b) Rational function:** lim_{x→3} (x² − 9)/(x − 3)

Direct substitution gives 0/0 (indeterminate). Factor the numerator:

= lim_{x→3} (x−3)(x+3)/(x−3)

= lim_{x→3} (x+3) = 3 + 3 = **6**

---

**(c) Rational function with non-removable discontinuity:** lim_{x→3} 1/(x−3)

Left-hand limit: lim_{x→3⁻} 1/(x−3) = −∞

Right-hand limit: lim_{x→3⁺} 1/(x−3) = +∞

Since LHL ≠ RHL, the limit **does not exist**.

---

**(d) Radical function:** lim_{x→3} √(x+1)

= √(3+1) = √4 = **2**

---

**(e) Exponential function:** lim_{x→3} 2ˣ

= 2³ = **8**

---

### 3. Find the expansion of the function f(x) = 2x - 2x² centered at a = -3 with Taylor's series formula. **[25]**

**From notes. The verification expansion at the end (the last 6 lines) is [AI generated].**

**Example 1:** Find the expansion for the function, f(x) = 2x − 2x² centered at a = −3 using the Taylor series formula.

**Solution:**

To find: Taylor series for the given function

Given:

Function, f(x) = 2x − 2x²

Center at a = −3

**Taylor series formula:**

f(x) = f(a) + f'(a)(x − a) + f"(a)/2! × (x − a)² + f'"(a)/3! × (x − a)³ + f⁽⁴⁾(a)/4! × (x − a)⁴ + ... + fⁿ(a)/n! × (x − a)ⁿ

**Function and its derivatives:**

f(x) = 2x − 2x²

f'(x) = 2 − 4x

f"(x) = −4

f"'(x) = 0 (and all higher derivatives are zero)

Since a = −3 and n = 3, the required expansion is:

f(x) = f(−3) + f'(−3)(x − (−3)) + f"(−3)/2! × (x − (−3))² + f"'(−3)/3! × (x − (−3))³

f(x) = f(−3) + f'(−3)(x + 3) + f"(−3)/2! × (x + 3)² + f"'(−3)/3! × (x + 3)³

**We evaluate the function and its derivatives at x = a = −3:**

f(−3) = 2(−3) − 2(−3)² = −6 − 18 = −24

f'(−3) = 2 − 4(−3) = 2 + 12 = 14

f"(−3) = −4

f"'(−3) = 0 and all the derivatives from here onwards are zeros.

**Taylor series expansion for the given function:**

P₃(x) = −24 + 14(x + 3) + (−4)/2! (x + 3)² + 0/3! (x + 3)³

P₃(x) = −24 + 14(x + 3) − 2(x + 3)²

**Answer:** Taylor series expansion around a = −3 for the function f(x) = 2x − 2x² is

**−24 + 14(x + 3) − 2(x + 3)²**

We can verify by expanding:

= −24 + 14x + 42 − 2(x² + 6x + 9)

= −24 + 14x + 42 − 2x² − 12x − 18

= (−24 + 42 − 18) + (14x − 12x) − 2x²

= 0 + 2x − 2x²

= 2x − 2x² ✓

The expansion is exact (not an approximation) because f(x) is a polynomial of degree 2, so the Taylor series terminates after the quadratic term.
