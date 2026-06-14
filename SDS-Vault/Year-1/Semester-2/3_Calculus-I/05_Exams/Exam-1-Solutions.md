# Exam-1 Solutions

---

### 1. (a) What do you mean by function? What are the basic ways of expressing function? Illustrate vertical line test for verifying function. **[4]**

A **function** is a relation between a set of inputs and a set of permissible outputs such that each input is related to exactly one output. If f is a function from set A to set B, we write f: A → B, and for every x ∈ A, there is exactly one y ∈ B such that y = f(x).

**Basic ways of expressing a function:**
1. **Symbolic form (formula)** — e.g., f(x) = x² + 1
2. **Tabular form** — using a table of x and y values
3. **Graphical form** — plotting points on a coordinate plane
4. **Verbal description** — describing the relationship in words
5. **Mapping diagram** — showing arrows from domain to range

**Vertical Line Test:** A graph in the xy-plane represents a function if and only if no vertical line intersects the graph at more than one point. If a vertical line cuts the graph at two or more points, then there exists an x-value with multiple y-values, which violates the definition of a function.

---

### 1. (b) Define constant as well as linear function with illustrations. Hence, interpret the slope of a linear function. **[5]**

**Constant Function:** A function of the form f(x) = c, where c is a constant. For every input x, the output is always c. Its graph is a horizontal line parallel to the x-axis.

*Illustration:* f(x) = 5. For x = 1, 2, 3, ..., f(x) = 5 always.

**Linear Function:** A function of the form f(x) = mx + b, where m and b are constants. m is the slope and b is the y-intercept. Its graph is a straight line.

*Illustration:* f(x) = 2x + 3. When x = 0, y = 3; when x = 1, y = 5; when x = −1, y = 1.

**Slope Interpretation:** The slope m of a linear function f(x) = mx + b represents the rate of change of y with respect to x. It is calculated as m = (y₂ − y₁)/(x₂ − x₁) = Δy/Δx. A positive slope means the line rises as x increases; a negative slope means the line falls as x increases; a zero slope means a horizontal line (constant function); an undefined slope (vertical line) is not a function.

---

### 1. (c) Consider the following data table and answer the questions below: **[5]**

| x | 1.5 | 2.5 | 3.5 | 5.5 | 9.5 |
|---|---|---|---|---|---|
| y | 0.3 | 1.1 | 1.9 | 3.5 | 6.7 |

**(i) Explain why a linear model is appropriate for the data table.**

We check whether the differences in y are roughly proportional to the differences in x:

From x = 1.5 to 2.5 (Δx = 1): Δy = 1.1 − 0.3 = 0.8
From x = 2.5 to 3.5 (Δx = 1): Δy = 1.9 − 1.1 = 0.8
From x = 3.5 to 5.5 (Δx = 2): Δy = 3.5 − 1.9 = 1.6 (0.8 per unit)
From x = 5.5 to 9.5 (Δx = 4): Δy = 6.7 − 3.5 = 3.2 (0.8 per unit)

Since the rate of change is constant at 0.8 per unit change in x, a linear model is appropriate.

**(ii) Find a linear function that relates x and y, and graph the equation.**

Slope m = Δy/Δx = 0.8/1 = 0.8

Using point-slope form with (x₁, y₁) = (1.5, 0.3):
y − 0.3 = 0.8(x − 1.5)
y = 0.8x − 1.2 + 0.3
y = 0.8x − 0.9

The linear function is **y = 0.8x − 0.9**.

---

### 2. (a) What do you mean by continuity of a function? Explain with example. What are the conditions to be meet for a continuous function? **[3+2]**

**Continuity:** A function f(x) is said to be continuous at a point x = a if the function has no breaks, jumps, or holes at that point. Formally, f is continuous at x = a if the limit of f(x) as x approaches a equals the function value at a.

**Conditions for continuity at x = a (all three must hold):**
1. f(a) is defined (the function exists at x = a)
2. lim_{x→a} f(x) exists (the left-hand and right-hand limits are equal)
3. lim_{x→a} f(x) = f(a) (the limit equals the function value)

**Example:** f(x) = x² is continuous at x = 2 because:
1. f(2) = 4 is defined
2. lim_{x→2} x² = 4 (the limit exists)
3. lim_{x→2} x² = 4 = f(2)

A simple example of discontinuity: f(x) = 1/(x−2). At x = 2, f(2) is undefined (division by zero), so the function is discontinuous at x = 2.

---

### 2. (b) i. Show that |x| is continuous everywhere. **[2]**

The function f(x) = |x| is defined piecewise as:
- f(x) = x for x ≥ 0
- f(x) = −x for x < 0

**At x = 0:**
- f(0) = 0 is defined
- Left-hand limit: lim_{x→0⁻} |x| = lim_{x→0⁻} (−x) = 0
- Right-hand limit: lim_{x→0⁺} |x| = lim_{x→0⁺} (x) = 0
- Since LHL = RHL = 0 = f(0), f is continuous at x = 0

**For x > 0:** f(x) = x is a polynomial (linear), hence continuous.
**For x < 0:** f(x) = −x is a polynomial (linear), hence continuous.

Since f(x) = |x| is continuous at x = 0 and at all other points, it is continuous everywhere.

---

### 2. (b) ii. Show that \lim_{x \to 0} \frac{1 - \cos x}{x} = 0 **[3]**

We evaluate the limit using the known trigonometric limit and algebraic manipulation:

lim_{x→0} (1 − cos x)/x

Multiply numerator and denominator by (1 + cos x):

= lim_{x→0} [(1 − cos x)(1 + cos x)] / [x(1 + cos x)]
= lim_{x→0} (1 − cos² x) / [x(1 + cos x)]
= lim_{x→0} sin² x / [x(1 + cos x)]
= lim_{x→0} (sin x/x) · [sin x/(1 + cos x)]

We know that lim_{x→0} sin x/x = 1.

Also, as x → 0, sin x → 0 and cos x → 1, so sin x/(1 + cos x) → 0/(1+1) = 0.

Therefore:

lim_{x→0} (1 − cos x)/x = 1 · 0 = 0

---

### 2. (c) Prove that the function f(x) = \begin{cases} x \sin \frac{1}{x}, & x \neq 0 \\ 5 & x = 0 \end{cases} is not continuous at x = 0 **[4]**

For f to be continuous at x = 0, we need lim_{x→0} f(x) = f(0) = 5.

Let us evaluate lim_{x→0} x sin(1/x).

Since −1 ≤ sin(1/x) ≤ 1 for all x ≠ 0, we have:

−|x| ≤ x sin(1/x) ≤ |x|

By the Squeeze Theorem, since lim_{x→0} (−|x|) = 0 and lim_{x→0} |x| = 0, we get:

lim_{x→0} x sin(1/x) = 0

Thus, lim_{x→0} f(x) = 0, but f(0) = 5.

Since lim_{x→0} f(x) ≠ f(0), the function is **not continuous** at x = 0.

---

### 3. (a) What do you mean by differentiability? What are the necessary and sufficient conditions of differentiability? Hence, illustrate graphical interpretation of differentiability **[6]**

**Differentiability:** A function f(x) is said to be differentiable at a point x = a if the derivative f'(a) exists. That is, the limit

f'(a) = lim_{h→0} [f(a+h) − f(a)]/h

exists and is finite.

**Necessary condition for differentiability:** For f to be differentiable at x = a, f must be continuous at x = a. (If f is not continuous at a, it cannot be differentiable there.)

**Sufficient conditions for differentiability:**
1. f is continuous at x = a
2. The left-hand derivative lim_{h→0⁻} [f(a+h) − f(a)]/h exists and equals the right-hand derivative lim_{h→0⁺} [f(a+h) − f(a)]/h
3. The common value is finite

**Graphical interpretation:** If f is differentiable at x = a, then the graph of f has a unique tangent line at the point (a, f(a)) that is non-vertical. The slope of this tangent line is f'(a). Geometrically, differentiability means the graph is "smooth" (no sharp corners, cusps, or vertical tangents) at that point. A differentiable function has a well-defined instantaneous rate of change at every point in its domain.

From the notes: A differentiable function f is increasing on any interval where its graph has tangent lines with positive slope, is decreasing on any interval where its graph has tangent lines with negative slope, and is constant on any interval where its graph has tangent lines with zero slope.

---

### 3. (b) What is successive differentiation and how does it work? Find out nth derivative of (ax + b)^m **[4]**

**What is Successive Differentiation, and how does it work?**

Successive differentiation is a process of deriving higher-order derivatives from a function by sequentially differentiating it.

1. If y = f(x) is a function of x, then dy/dx or d/dx or f'(x) or y₁ is the derivative of y with respect to x. The first-order derivatives of y are this.

2. If dy/dx is differentiated again, y = f(x) is derivable double with respect to x, then d²y/dx² or d²y or f"(x) or y₂ is the derivative of dy/dx with regard to x. The 2nd derivative of y is this.

3. If d²y/dx² is differentiated twice, y = f(x) is derivable three with respect to x, then d³y/dx³ or d³y or f'"(x) or y₃ is the derivative of d²y/dx² with respect to x. The 3rd derivative of y is what it's called.

Similarly, the successive derivatives may be found, and the nth derivative of y can be found by differentiating a given function n times with respect to x.

**nth Derivative of (ax + b)^m, m is a +ve integer greater than n**

Let y = (ax + b)^m

y₁ = ma(ax + b)^(m−1)

y₂ = m(m−1)a²(ax + b)^(m−2)

yₙ = m(m−1)...(m−n+1)aⁿ(ax + b)^(m−n)

= [m! / (m−n)!] aⁿ (ax + b)^(m−n)

---

### 3. (c) Consider the function f(x) = x^3 \sin x and determine the nth derivative of the function. **[4]**

Using **Leibnitz's Theorem**: If u and v are functions of x with derivatives up to order n, then

(uv)ⁿ = Σᵢ₌₀ⁿ (ⁿᵢ) u⁽ⁿ⁻ⁱ⁾ v⁽ⁱ⁾

Let u = x³ and v = sin x.

We note the derivatives:
- For u = x³: u' = 3x², u" = 6x, u"' = 6, u⁽⁴⁾ = 0, and all higher derivatives are zero.
- For v = sin x: v' = cos x, v" = −sin x, v"' = −cos x, v⁽⁴⁾ = sin x, ... (cyclic with period 4)

By Leibnitz's theorem:

fⁿ(x) = (ⁿ₀) (x³)⁽ⁿ⁾ sin x + (ⁿ₁) (x³)⁽ⁿ⁻¹⁾ sin' x + (ⁿ₂) (x³)⁽ⁿ⁻²⁾ sin" x + (ⁿ₃) (x³)⁽ⁿ⁻³⁾ sin"' x + ...

For n ≥ 4, (x³)⁽ⁿ⁾ = 0, so only terms with i = 0, 1, 2, 3 survive.

Therefore:

fⁿ(x) = (ⁿ₀) (x³)⁽ⁿ⁾ sin x + (ⁿ₁) (x³)⁽ⁿ⁻¹⁾ cos x + (ⁿ₂) (x³)⁽ⁿ⁻²⁾ (−sin x) + (ⁿ₃) (x³)⁽ⁿ⁻³⁾ (−cos x)

For the specific cases:
- n = 1: f'(x) = 3x² sin x + x³ cos x
- n = 2: f"(x) = 6x sin x + 6x² cos x − x³ sin x
- n = 3: f"'(x) = 6 sin x + 18x cos x − 9x² sin x − x³ cos x

The general formula for the nth derivative can be obtained by continuing this pattern using Leibnitz's theorem.

---

### 4. (a) State and prove Rolle's theorem. **[6]**

**Statement:** Rolle's theorem states that "If a function f is defined in the closed interval [a, b] in such a way that it satisfies the following condition: i) f is continuous on [a, b], ii) f is differentiable on (a, b), and iii) f(a) = f(b), then there exists at least one value of x, let us assume this value to be c, which lies between a and b i.e. (a < c < b) in such a way that f'(c) = 0."

**Proof:** When proving a theorem directly, you start by assuming all of the conditions are satisfied. So, our discussion below relates only to functions

- that is continuous over [a, b],
- that is differentiable (a, b),
- and have f(a) = f(b).

With that in mind, notice that when a function satisfies Rolle's Theorem, the place where f'(x)=0 occurs at a maximum or a minimum value (i.e., extrema).

How do we know that a function will even have one of these extrema? The Extreme Value Theorem says that if a function is continuous, then it is guaranteed to have both a maximum and a minimum point in the interval.

Now, there are two basic possibilities for our function.

**Case 1: the function is constant.**
For a constant function, the graph is a horizontal line segment. In this case, every point satisfies Rolle's Theorem since the derivative is zero everywhere. (Remember, Rolle's Theorem guarantees at least one point. It doesn't preclude multiple points!)

**Case 2: the function is not constant.**
Since the function isn't constant, it must change directions in order to start and end at the same y-value. It means at some point within the interval the function will either have a minimum, a maximum or both. So, now we need to show that at this interior-point the derivative is equal to zero. The rest of the discussion will focus on the cases where the interior extrema is a maximum, but the discussion for a minimum is largely the same.

Possibility 1: Could the maximum occur at a point where f'>0?
No, because if f'>0 we know the function is increasing. But it can't increase since we are at its maximum point.

Possibility 2: Could the maximum occur at a point where f'<0?
No, because if f'<0 we know that function is decreasing, which means it was larger just a little to the left of where we are now. But we are at the function's maximum value, so it couldn't have been larger. Since f' exists, but isn't larger than zero, and isn't smaller than zero, the only possibility that remains is that f'=0. And that's it! We have shown that the function must have extrema and that at the extrema the derivative must equal zero!

---

### 4. (b) Illustrate Rolle's theorem graphically. **[4]**

```
Y
|
|    /|  |\
|   / |  | \
|  /  |  |  \
| /   |  |   \
|/    |  |    \
|___________________
x' a c b x
Y'
```

The graph shows a function f(x) where f(a) = f(b). The curve starts at a, rises to a maximum, then falls back to the same height at b. At the point x = c between a and b, the tangent line is horizontal, meaning f'(c) = 0. This is the geometric interpretation of Rolle's theorem — there is at least one point where the tangent is parallel to the x-axis.

---

### 4. (c) Verify the function f(x) = x^2 + 2 satisfies the Rolle's theorem in the interval [-2, 2]. **[4]**

Verify Rolle's theorem for the functions y = x² + 2, a = −2, and b = 2

The function y = x² + 2 is continuous in [−2, 2] and differentiable in (−2, 2), according to Rolle's theorem formulation.

Given the circumstances,

f(x) = x² + 2

f(−2) = (−2)² + 2 = 4 + 2 = 6

f(2) = (2)² + 2 = 4 + 2 = 6

Thus, f(−2) = f(2) = 6

As a result, the function f(x) is continuous in the range [−2, 2].

Now, f'(x) = 2x

According to Rolle's theorem, there is a point c ∈ (−2, 2) where f'(c) = 0.

f'(c) = 2(c) = 0 at c = 0, when c = 0 ∈ (−2, 2)

As a result, Rolle's theorem is proven.

---

### 5. (a) What do you mean by Maclaurin's series. Hence, derive Maclaurin's formulae? **[7]**

**What is Maclaurin Series?**

The Maclaurin series is a power series that uses successive derivatives when the input is equal to zero.

The Maclaurin series is another polynomial approximation of a function. In fact, it is a special case of a Taylor series where each of the successive derivatives is evaluated at x = 0. Simply put, the Maclaurin series is the Taylor series of the function at x = 0.

**Maclaurin Series Formula**

The Maclaurin series formula is simply the resulting expression when c = 0. Hence, we have the Maclaurin series formula as shown below:

```
f(x) = Σ_{n=0}^{∞} fⁿ(0)/n!  xⁿ
     = f(0) + f'(0)/1! x + f"(0)/2! x² + f'"(0)/3! x³ + ...
```

**Derivation:** Starting from the general Taylor series expanded about x = a:

f(x) = f(a) + f'(a)(x−a) + f"(a)/2! (x−a)² + f'"(a)/3! (x−a)³ + ...

Setting a = 0, we get the Maclaurin series:

f(x) = f(0) + f'(0)x + f"(0)/2! x² + f'"(0)/3! x³ + ... + fⁿ(0)/n! xⁿ + ...

The coefficients cₙ = fⁿ(0)/n! are determined by evaluating the successive derivatives at x = 0.

**How to find a Maclaurin series:**

- Take the successive derivatives of f(x).
- Evaluate f(x), f'(x), f"(x), f'"(x), and more at x = 0.
- Write down the functions' Maclaurin series by adding the resulting terms.

---

### 5. (b) Find the Maclaurin's series of f(x) = \sqrt{1 + 2x} up to the fourth order and use your answer from the given function to find an approximation for the value of \sqrt{1.02} and compare the approximation found to the actual value of the square root. **[7]**

From the worked example in the notes:

**Use the Maclaurin series formula to find the Maclaurin series for f(x) = √(1+2x) up to and including the term in x⁴.**

f(x) = √(1+2x) = (1+2x)^(½)

**Step 1:** Compute the derivatives and evaluate at x = 0:

f(0) = 1
f'(x) = (1+2x)^(−½) → f'(0) = 1
f"(x) = −(1+2x)^(−³/²) → f"(0) = −1
f'"(x) = 3(1+2x)^(−⁵/²) → f'"(0) = 3
f⁽⁴⁾(x) = −15(1+2x)^(−⁷/²) → f⁽⁴⁾(0) = −15

**Step 2:** Apply the Maclaurin series formula:

f(x) = f(0) + f'(0)x + f"(0)/2! x² + f'"(0)/3! x³ + f⁽⁴⁾(0)/4! x⁴ + ...

= 1 + (1)x + (−1)/2! x² + 3/3! x³ + (−15)/4! x⁴ + ...

= 1 + x − ½ x² + ½ x³ − ⅝ x⁴ + ...

**Step 3:** Up to the x⁴ term:

√(1+2x) ≈ 1 + x − ½x² + ½x³ − ⅝x⁴

**Use the answer to find an approximation for √1.02, and compare:**

Let x = 0.01. Then √(1+2x) = √(1+2(0.01)) = √1.02.

√1.02 ≈ 1 + (0.01) − ½(0.01)² + ½(0.01)³ − ⅝(0.01)⁴

= 1 + 0.01 − 0.00005 + 0.0000005 − 0.00000000625

= 1.00995049375

The exact value of the square root is:

√1.02 = 1.0099504913836...

**Comparison:** The approximation 1.00995049375 matches the exact value 1.0099504913836 to 9 decimal places. The error is approximately 2.37 × 10⁻⁹, which is extremely small, demonstrating the accuracy of the Maclaurin series approximation.

---

### 6. (a) What do you mean by indefinite integral. Hence, write down the properties of indefinite integral. **[4]**

The process of finding antiderivatives is called antidifferentiation or integration. Thus, if

(d/dx)[F(x)] = f(x)

then integrating (or antidifferentiating) f(x) produces the antiderivatives F(x) + C. We denote this by writing

∫ f(x) dx = F(x) + C

The "elongated s" that appears on the left side is called an integral sign or an indefinite integral, the function f(x) is called the integrand, and the constant C is called the constant of integration.

**Properties of the Indefinite Integral**

If we differentiate an antiderivative of f(x), we obtain f(x) back again. Thus,

d/dx [∫ f(x) dx] = f(x)

This result is helpful for proving the following basic properties of antiderivatives:

**7.2.3 THEOREM**

(a) A constant factor can be moved through an integral sign; that is,

∫ cf(x) dx = c ∫ f(x) dx

(b) An antiderivative of a sum is the sum of the antiderivatives; that is,

∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx

(c) An antiderivative of a difference is the difference of the antiderivatives; that is,

∫ [f(x) − g(x)] dx = ∫ f(x) dx − ∫ g(x) dx

---

### 6. (b) Integrate the following terms: \sin^2 x \cdot \cos^2 x and 3x^2 \sin^3 x **[6]**

**∫ sin²x · cos²x dx**

From the notes:

We know, 2 sin x cos x = sin 2x
sin x cos x = (sin 2x)/2

Substituting:

∫ sin²x · cos²x dx = ∫ (sin x cos x)² dx = ∫ ((sin 2x)/2)² dx

= ¼ ∫ sin² 2x dx

We know sin²θ = (1 − cos 2θ)/2. Let θ = 2x, then sin² 2x = (1 − cos 4x)/2.

= ¼ ∫ (1 − cos 4x)/2 dx

= ⅛ ∫ (1 − cos 4x) dx

= ⅛ [ x − (sin 4x)/4 ] + C

= **x/8 − (sin 4x)/32 + C**

**∫ 3x² sin³x dx**

We use integration by parts. Let u = 3x², dv = sin³x dx.

First find ∫ sin³x dx. Write sin³x = sin x · sin²x = sin x (1 − cos²x).

∫ sin³x dx = ∫ sin x dx − ∫ sin x cos²x dx

= −cos x + (cos³x)/3 + C₁

Now apply integration by parts to the original integral:

Let u = 3x², dv = sin³x dx
du = 6x dx, v = ∫ sin³x dx = −cos x + (cos³x)/3

∫ 3x² sin³x dx = 3x²[−cos x + (cos³x)/3] − ∫ [−cos x + (cos³x)/3] · 6x dx

= 3x²(−cos x) + 3x²(cos³x)/3 − ∫ [−6x cos x + 2x cos³x] dx

= −3x² cos x + x² cos³x + ∫ (6x cos x − 2x cos³x) dx

The remaining integrals can be further evaluated using integration by parts and trigonometric identities. The final result is:

∫ 3x² sin³x dx = −3x² cos x + x² cos³x + 6x sin x − 6 cos x − 2x sin x cos²x + (2/3) cos³x + C

---

### 6. (c) Solve the following problems: \int x \sqrt{1 - x^2} dx and \int \frac{\sec^2 3x}{\tan 3x} dx **[4]**

**∫ x √(1−x²) dx**

From the notes:

Let u = 1−x². Then du/dx = −2x or du = −2x dx.
Need: x dx. We get x dx = −½ du.

∫ x √(1−x²) dx = ∫ √u · (−½) du

= −½ ∫ u^½ du

= −½ · (2/3) u^(3/2) + C

= −⅓ u^(3/2) + C

= **−⅓ (1−x²)^(3/2) + C**

You may check this by differentiation.

**∫ sec²(3x) / tan(3x) dx**

From the notes:

Let u = tan(3x). Then du/dx = sec²(3x) · 3 or du = 3 sec²(3x) dx.
Need: sec²(3x) dx. We get sec²(3x) dx = du/3.

∫ sec²(3x)/tan(3x) dx = ∫ (1/u)(du/3)

= ⅓ ∫ du/u

= ⅓ ln|u| + C

= **⅓ ln|tan(3x)| + C**

---

### 7. (a) Explain area under curve and net signed area for any interval. **[2+2]**

**Area under the curve:**

Assuming that f is a continuous function and positive on the interval [a, b]. So, its graph is above the x-axis. The definite integral ∫ₐᵇ f(x)dx is the area bounded by the curve y = f(x), the ordinates x = a and x = b and the x-axis.

The area A under the graph of f over the interval [a, b] is represented by the definite integral:

A = ∫ₐᵇ f(x) dx

**Net signed area:**

The Riemann sum contains terms such as f(cᵢ)Δxᵢ that give the area of a rectangle when f(cⱼ) is positive. When f(cⱼ) is negative, then the product f(cⱼ)Δxᵢ is the negative of the rectangle's area. When we add up such terms for a negative function we get the negative of the area between the curve and the x-axis. If we then take the absolute value, we obtain the correct positive area.

The **net signed area** is the sum of areas above the x-axis minus the sum of areas below the x-axis. It is given by the definite integral ∫ₐᵇ f(x) dx, which accounts for the sign. If f(x) ≥ 0 on [a, b], the net signed area equals the total area. If f(x) takes both positive and negative values, the net signed area may be less than the total geometric area.

---

### 7. (b) Explain the Riemann sum and definite integral. What is the relation between Riemann sum and definite integral? **[3+2]**

**Riemann sum:** A Riemann sum approximates the area under a curve by dividing the interval [a, b] into n subintervals of equal width Δx = (b−a)/n, choosing a sample point xᵢ* in each subinterval, and forming the sum:

Sₙ = Σᵢ₌₁ⁿ f(xᵢ*) Δx

If xᵢ* is the left endpoint, we get the left Riemann sum. If xᵢ* is the right endpoint, we get the right Riemann sum.

**Definite integral:** The definite integral ∫ₐᵇ f(x) dx is defined as the limit of the Riemann sum as the number of subintervals approaches infinity (equivalently, as Δx → 0):

∫ₐᵇ f(x) dx = lim_{n→∞} Σᵢ₌₁ⁿ f(xᵢ*) Δx

**Relation:** The definite integral is the limit of the Riemann sum as n → ∞. The Riemann sum provides an approximation to the definite integral, and as the subintervals become finer (n → ∞), the approximation converges to the exact value of the definite integral, provided f is continuous on [a, b].

From the notes: The Fundamental Theorem of Calculus, which is the central theorem of integral calculus, connects integration and differentiation, enabling us to compute integrals using an antiderivative of the integrand function rather than by taking limits of Riemann sums.

---

### 7. (c) Answer the following questions: **[2.5 × 2]**

**(i) Using the definition of area under the curve with x_k^* as the left end point of each subinterval, obtain the area under the curve y = f(x) = 4 - \frac{1}{4}x^2 over the interval [0,3].**

Divide [0, 3] into n equal subintervals of width Δx = 3/n.

The left endpoints are xₖ = (k−1)Δx = 3(k−1)/n for k = 1, 2, ..., n.

The left Riemann sum is:

Lₙ = Σₖ₌₁ⁿ f(xₖ) Δx = Σₖ₌₁ⁿ [4 − ¼(3(k−1)/n)²] · (3/n)

= (3/n) Σₖ₌₁ⁿ [4 − (9(k−1)²)/(4n²)]

= (3/n) [4n − (9/(4n²)) Σₖ₌₁ⁿ (k−1)²]

We know Σₖ₌₁ⁿ (k−1)² = Σⱼ₌₀ⁿ⁻¹ j² = (n−1)n(2n−1)/6

Lₙ = (3/n) [4n − (9/(4n²)) · (n−1)n(2n−1)/6]

= (3/n) [4n − (9(n−1)(2n−1))/(24n)]

= 12 − (9(n−1)(2n−1))/(8n²)

Taking the limit as n → ∞:

A = lim_{n→∞} Lₙ = 12 − (9·2n·2n)/(8n²) = 12 − (36n²)/(8n²) = 12 − 4.5 = 7.5

Therefore, the area is **7.5 square units**.

**(ii) Using the definition of area under the curve with x_k^* as the right end point of each subinterval, obtain the area under the curve y = f(x) = x^2 and the interval [0,1].**

Divide [0, 1] into n equal subintervals of width Δx = 1/n.

The right endpoints are xₖ = kΔx = k/n for k = 1, 2, ..., n.

The right Riemann sum is:

Rₙ = Σₖ₌₁ⁿ f(xₖ) Δx = Σₖ₌₁ⁿ (k/n)² · (1/n)

= (1/n³) Σₖ₌₁ⁿ k²

= (1/n³) · n(n+1)(2n+1)/6

= (n+1)(2n+1)/(6n²)

Taking the limit as n → ∞:

A = lim_{n→∞} Rₙ = lim_{n→∞} (n+1)(2n+1)/(6n²)

= lim_{n→∞} (2n² + 3n + 1)/(6n²)

= 2/6 = 1/3

Therefore, the area is **⅓ square units**.

---

### 8. (a) Show that definite integral can be expressed as a limit of a sum. **[8]**

**Definite Integral as Limit of a Sum**

Assuming that f is a continuous function and positive on the interval [a, b]. So, its graph is above the x-axis.

Definite integral ∫ₐᵇ f(x)dx is the area bounded by the curve y = f(x), the ordinates x = a and x = b and the x-axis.

Now to evaluate this area, consider the region ABCD.

Let x₀ = a and xₙ = b.

Now divide the interval [a, b] into n equal subintervals denoted by [x₀, x₁], [x₁, x₂], [x₂, x₃], ..., [xᵣ₋₁, xᵣ], ..., [xₙ₋₁, xₙ]

where x₀ = a, x₁ = a + h, x₂ = a + 2h, ... and xₙ = a + nh or h = (b−a)/n. As n → ∞, h → 0.

The region ABCD under consideration is the sum of n subregions, where each subregion is defined on subintervals [xᵣ₋₁, xᵣ], where r = 1, 2, 3, ..., n.

The area of each subregion = (xᵣ − xᵣ₋₁) × f(xᵣ₋₁)

As xᵢ − xᵢ₋₁ → 0, i.e., h → 0, the area above becomes a nearly perfect rectangle. Now the area under the curve can be broken into n different rectangles. Adding all these rectangles' areas we get the area under the curve.

**Lower sum:** sₙ = h[f(x₀) + f(x₁) + ... + f(xₙ₋₁)] = h Σᵣ₌₁ⁿ f(xᵣ₋₁)

**Upper sum:** Sₙ = h[f(x₁) + f(x₂) + ... + f(xₙ)] = h Σᵣ₌₁ⁿ f(xᵣ)

sₙ and Sₙ denote the sum of areas of all lower rectangles and upper rectangles raised over subintervals [xᵣ₋₁, xᵣ] for r = 1, 2, 3, ..., n respectively.

As n → ∞, strips become narrower and narrower, so the limiting values of sₙ and Sₙ are the same in both cases, and the common limiting value is the required area under the curve.

So,

lim_{n→∞} sₙ = lim_{n→∞} Sₙ = area of the region = ∫ₐᵇ f(x) dx

Now, this equation can also be re-written as:

∫ₐᵇ f(x) dx = lim_{n→∞} h [f(a) + f(a+h) + f(a+2h) + f(a+3h) + ... + f(a+(n−1)h)]

where h = (b−a)/n, and h → 0 as n → ∞.

This expression is known as the definition of the definite integral as a limit of a sum.

---

### 8. (b) Find \int_0^2 (x^2 + 1) dx as the limit of sum. **[6]**

We evaluate ∫₀² (x² + 1) dx as a limit of a Riemann sum.

Here a = 0, b = 2, so h = (b−a)/n = 2/n.

The partition points are xₖ = a + kh = 2k/n for k = 0, 1, 2, ..., n.

Using the right-endpoint Riemann sum:

Rₙ = Σₖ₌₁ⁿ f(xₖ) · h = Σₖ₌₁ⁿ [(2k/n)² + 1] · (2/n)

= (2/n) Σₖ₌₁ⁿ [(4k²/n²) + 1]

= (2/n) [ (4/n²) Σₖ₌₁ⁿ k² + Σₖ₌₁ⁿ 1 ]

= (2/n) [ (4/n²) · n(n+1)(2n+1)/6 + n ]

= (2/n) [ (4(n+1)(2n+1))/(6n) + n ]

= (2/n) · [ (4(n+1)(2n+1))/(6n) + n ]

= (8(n+1)(2n+1))/(6n²) + 2

= (4(n+1)(2n+1))/(3n²) + 2

Now take the limit as n → ∞:

∫₀² (x² + 1) dx = lim_{n→∞} Rₙ

= lim_{n→∞} [ (4(n+1)(2n+1))/(3n²) + 2 ]

= lim_{n→∞} [ (4(2n² + 3n + 1))/(3n²) + 2 ]

= lim_{n→∞} [ (8n² + 12n + 4)/(3n²) + 2 ]

= 8/3 + 2

= 8/3 + 6/3

= **14/3**

Verification using the Fundamental Theorem:
∫₀² (x² + 1) dx = [x³/3 + x]₀² = (8/3 + 2) − (0 + 0) = 8/3 + 2 = 14/3. ✓
