---
title: limit
created: 2026-03-18
type: literature
tags:
  - reading-notes
  - flashcards
aliases:
sr-due: 2026-03-25
sr-interval: 1
sr-ease: 228
---
# limit


## Definitions

### Foundational Calculus Concepts


#flashcards

- **The Tangent Line Problem**::Given a function $f$ and a point $P(x_0, y_0)$ on its graph, the task is to find an equation of the line that is tangent to the graph at $P$.
    
- **The Area Problem:**:: Given a function $f$, the task is to find the area between the graph of $f$ and a specific interval $[a, b]$ on the x-axis.
    
- **Differential Calculus:** The portion of calculus that arises from the tangent line problem.
    
- **Integral Calculus:** The portion of calculus that arises from the area problem.
    
- **Terminal Velocity:** The limit approached by the velocity of a falling object, such as a skydiver, when air resistance prevents velocity from increasing indefinitely.
    
- **Limit:** Regarded as the "fundamental building block" on which all other calculus concepts, such as rates of change, are based.
    

### Geometric Definitions

- **Secant Line:** A line that passes through a point $P$ on a curve and another distinct point $Q$ on the same curve.
    
- **Tangent Line:** The limiting position of a secant line as the point $Q$ moves along the curve toward the point $P$.
    
- **Vertical Asymptote:** The vertical line $x = a$ is a vertical asymptote for the graph of $y = f(x)$ if the graph rises or falls without bound as $x$ approaches $a$ from either side.
    
- **Horizontal Asymptote:** The line $y = L$ is a horizontal asymptote for the graph of $f$ if the limit of $f(x)$ as $x$ increases or decreases without bound is equal to $L$.
    
- **Asymptotic Curves:** Two curves $y = f(x)$ and $y = g(x)$ are considered asymptotic as $x \to +\infty$ (or $x \to -\infty$) if the limit of their difference $[f(x) - g(x)]$ is zero as $x$ approaches that respective infinity.
    

### Informal and Intuitive Limit Definitions

- **Two-Sided Limit (Informal):** Written as $\lim_{x \to a} f(x) = L$, this means the values of $f(x)$ can be made as close as desired to $L$ by taking values of $x$ sufficiently close to $a$ (but not equal to $a$).
    
- **One-Sided Limits (Informal):**
    
    - Right-hand limit: $\lim_{x \to a^+} f(x) = L$ means $f(x)$ approaches $L$ as $x$ approaches $a$ from the right.
        
    - Left-hand limit: $\lim_{x \to a^-} f(x) = L$ means $f(x)$ approaches $L$ as $x$ approaches $a$ from the left.
        
- **Infinite Limits (Informal):** These describe cases where a limit fails to exist because the function increases or decreases without bound.
    
    - $\lim_{x \to a} f(x) = +\infty$ denotes $f(x)$ increases without bound as $x$ approaches $a$.
        
    - $\lim_{x \to a} f(x) = -\infty$ denotes $f(x)$ decreases without bound as $x$ approaches $a$.
        
- **End Behavior:** The behavior of a function $f(x)$ as the variable $x$ increases ($x \to +\infty$) or decreases ($x \to -\infty$) without bound.
    
- **Limits at Infinity (Informal):** Written as $\lim_{x \to +\infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$, these describe when $f(x)$ eventually gets as close as desired to a number $L$ as $x$ increases or decreases without bound.
    
- **Infinite Limits at Infinity (Informal):** Notation such as $\lim_{x \to +\infty} f(x) = +\infty$ used when a function increases or decreases without bound as $x$ itself increases or decreases without bound.
    

### Rigorous Mathematical Definitions

- **Two-Sided Limit (Epsilon-Delta):** $\lim_{x \to a} f(x) = L$ if for any number $\epsilon > 0$ there exists a number $\delta > 0$ such that $|f(x) - L| < \epsilon$ whenever $0 < |x - a| < \delta$.
    
- **Limit at $+\infty$:** $\lim_{x \to +\infty} f(x) = L$ if for any $\epsilon > 0$ there exists a positive number $N$ such that $|f(x) - L| < \epsilon$ whenever $x > N$.
    
- **Limit at $-\infty$:** $\lim_{x \to -\infty} f(x) = L$ if for any $\epsilon > 0$ there exists a negative number $N$ such that $|f(x) - L| < \epsilon$ whenever $x < N$.
    
- **Infinite Limit at a Point ($+\infty$):** $\lim_{x \to a} f(x) = +\infty$ if for any positive number $M$ there exists a $\delta > 0$ such that $f(x) > M$ whenever $0 < |x - a| < \delta$.
    
- **Infinite Limit at a Point ($-\infty$):** $\lim_{x \to a} f(x) = -\infty$ if for any negative number $M$ there exists a $\delta > 0$ such that $f(x) < M$ whenever $0 < |x - a| < \delta$.
    

### Algebraic Definitions

- **Indeterminate Form of Type 0/0:** A quotient $f(x)/g(x)$ where the limits of both the numerator and the denominator are zero as $x$ approaches $a$.
    

---

## Formulas and Mathematical Expressions

### Geometric and Foundational Formulas

- **Point-Slope Formula (Tangent Line):** For a point $P(1, 1)$ on $y = x^2$: $y - 1 = m_{tan}(x - 1)$.
    
- **Secant Line Slope:** $m_{sec} = \frac{x^2 - 1}{x - 1}$.
    
- **Tangent Line Equation (at $x=1$ for $y=x^2$):** $y - 1 = 2(x - 1)$ or $y = 2x - 1$.
    
- **Decimal Expansion as a Sum:** $\frac{1}{3} = 0.3 + 0.03 + 0.003 + 0.0003 + 0.00003 + \dots$
    

### Limit Laws and Properties (Theorem 1.2.2)

If $\lim_{x \to a} f(x) = L_1$ and $\lim_{x \to a} g(x) = L_2$, then:

- **Sum Rule:** $\lim_{x \to a} [f(x) + g(x)] = L_1 + L_2$.
    
- **Difference Rule:** $\lim_{x \to a} [f(x) - g(x)] = L_1 - L_2$.
    
- **Product Rule:** $\lim_{x \to a} [f(x)g(x)] = L_1L_2$.
    
- **Quotient Rule:** $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L_1}{L_2}$ (provided $L_2 \neq 0$).
    
- **Root Rule:** $\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{L_1}$ (provided $L_1 > 0$ if $n$ is even).
    
- **Constant Factor Rule:** $\lim_{x \to a} (kg(x)) = k \lim_{x \to a} g(x)$.
    
- **Power Rule:** $\lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n$.
    

### Basic and Polynomial Limits

- **Limit of a Constant:** $\lim_{x \to a} k = k$.
    
- **Limit of $x$:** $\lim_{x \to a} x = a$.
    
- **Limit of $x^n$:** $\lim_{x \to a} x^n = a^n$.
    
- **Polynomial Limit (Theorem 1.2.3):** For $p(x) = c_0 + c_1x + \dots + c_nx^n$, $\lim_{x \to a} p(x) = p(a)$.
    
- **End Behavior of Polynomials:** $\lim_{x \to \pm\infty} (c_0 + c_1x + \dots + c_nx^n) = \lim_{x \to \pm\infty} c_nx^n$.
    

### Special and Transcendental Limits

- **Trigonometric Limit:** $\lim_{x \to 0} \frac{\sin x}{x} = 1$.
    
- **Inverse Tangent Limits:** $\lim_{x \to +\infty} \tan^{-1} x = \frac{\pi}{2}$ and $\lim_{x \to -\infty} \tan^{-1} x = -\frac{\pi}{2}$.
    
- **The Number $e$:** $\lim_{x \to \pm\infty} (1 + \frac{1}{x})^x = e$.
    
- **Alternative $e$ Formula:** $\lim_{x \to 0} (1 + x)^{1/x} = e$.
    
- **Exponential and Logarithmic Limits:**
    
    - $\lim_{x \to +\infty} \ln x = +\infty$.
        
    - $\lim_{x \to +\infty} e^x = +\infty$.
        
    - $\lim_{x \to -\infty} e^x = 0$.
        
    - $\lim_{x \to 0^+} \ln x = -\infty$.
        
    - $\lim_{x \to +\infty} e^{-x} = 0$.
        
    - $\lim_{x \to -\infty} e^{-x} = +\infty$.
        

### Infinite Limits and Limits at Infinity

- **Reciprocal Limits at Zero:** $\lim_{x \to 0^+} \frac{1}{x} = +\infty$ and $\lim_{x \to 0^-} \frac{1}{x} = -\infty$.
    
- **Reciprocal Limits at Infinity:** $\lim_{x \to \pm\infty} \frac{1}{x} = 0$.
    
- **General Power Limits at Infinity:** $\lim_{x \to \pm\infty} \frac{1}{x^n} = 0$.
    
- **Limits of $x^n$ as $x \to \pm\infty$:**
    
    - $\lim_{x \to +\infty} x^n = +\infty$.
        
    - $\lim_{x \to -\infty} x^n = -\infty$ (if $n$ is odd) or $+\infty$ (if $n$ is even).
        
- **Radical Identity:** $\sqrt{x^2} = |x|$.
    
- **Asymptotic Curves:** $\lim_{x \to \pm\infty} [f(x) - g(x)] = 0$.
    

### Rigorous (Epsilon-Delta) Definitions

- **Two-Sided Limit:** $\lim_{x \to a} f(x) = L$ if for any $\epsilon > 0$ there exists a $\delta > 0$ such that $|f(x) - L| < \epsilon$ whenever $0 < |x - a| < \delta$.
    
- **Limit at $+\infty$:** $|f(x) - L| < \epsilon$ whenever $x > N$.
    
- **Limit at $-\infty$:** $|f(x) - L| < \epsilon$ whenever $x < N$.
    
- **Infinite Limit ($+\infty$):** $f(x) > M$ whenever $0 < |x - a| < \delta$.
    
- **Infinite Limit ($-\infty$):** $f(x) < M$ whenever $0 < |x - a| < \delta$.
    

---

## Theorems and Their Corresponding Proofs

### Theorem 1.1.3: Relationship Between One-Sided and Two-Sided Limits

- **The Theorem:** The two-sided limit of a function $f(x)$ exists at $a$ if and only if both of the one-sided limits exist at $a$ and have the same value. This is expressed as:
    
    $$\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = L = \lim_{x \to a^+} f(x)$$
    
- **The Proof:** The sources state this result without formal proof.
    

### Theorem 1.2.1: Basic Limits

- **The Theorem:** Let $a$ and $k$ be real numbers.
    
    (a) $\lim_{x \to a} k = k$.
    
    (b) $\lim_{x \to a} x = a$.
    
    (c) $\lim_{x \to 0^-} \frac{1}{x} = -\infty$.
    
    (d) $\lim_{x \to 0^+} \frac{1}{x} = +\infty$.
    
- **The Proof:** No formal proof is provided in the text for this theorem, though it is illustrated geometrically and explained through examples of behavior.
    

### Theorem 1.2.2: Limit Laws

- **The Theorem:** Let $a$ be a real number, and suppose that $\lim_{x \to a} f(x) = L_1$ and $\lim_{x \to a} g(x) = L_2$.
    
    (a) Sum Rule: $\lim_{x \to a} [f(x) + g(x)] = L_1 + L_2$.
    
    (b) Difference Rule: $\lim_{x \to a} [f(x) - g(x)] = L_1 - L_2$.
    
    (c) Product Rule: $\lim_{x \to a} [f(x)g(x)] = L_1L_2$.
    
    (d) Quotient Rule: $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L_1}{L_2}$, provided $L_2 \neq 0$.
    
    (e) Root Rule: $\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{L_1}$, provided $L_1 > 0$ if $n$ is even.
    
- **The Proof:** The sources note that parts of this theorem are proved in Appendix D, which is not included in the provided excerpts.
    

### Theorem 1.2.3: Limit of a Polynomial

- **The Theorem:** For any polynomial $p(x) = c_0 + c_1x + \dots + c_nx^n$ and any real number $a$, $\lim_{x \to a} p(x) = p(a)$.
    
- **The Proof:**
    
    1. State the limit of the polynomial: $\lim_{x \to a} p(x) = \lim_{x \to a} (c_0 + c_1x + \dots + c_nx^n)$.
        
    2. Apply the Sum Rule from Theorem 1.2.2: $\lim_{x \to a} c_0 + \lim_{x \to a} c_1x + \dots + \lim_{x \to a} c_nx^n$.
        
    3. Apply the Constant Factor Rule: $\lim_{x \to a} c_0 + c_1 \lim_{x \to a} x + \dots + c_n \lim_{x \to a} x^n$.
        
    4. Substitute the basic limits (Theorem 1.2.1): $c_0 + c_1a + \dots + c_na^n = p(a)$.
        

### Theorem 1.2.4: Limits of Rational Functions

- **The Theorem:** Let $f(x) = \frac{p(x)}{q(x)}$ be a rational function, and let $a$ be any real number.
    
    (a) If $q(a) \neq 0$, then $\lim_{x \to a} f(x) = f(a)$.
    
    (b) If $q(a) = 0$ but $p(a) \neq 0$, then $\lim_{x \to a} f(x)$ does not exist.
    
- **The Proof:** No formal proof is provided for this theorem in the text.
    

### Formal Limit Definitions (Rigorous Framework)

While presented as definitions, these provide the rigorous mathematical framework for the theorems above:

- **Definition 1.4.1 (Two-Sided Limit):** $\lim_{x \to a} f(x) = L$ if for any $\epsilon > 0$ there exists a $\delta > 0$ such that $|f(x) - L| < \epsilon$ whenever $0 < |x - a| < \delta$.
    
- **Definition 1.4.2 & 1.4.3 (Limits at Infinity):** Precise conditions for $x \to +\infty$ and $x \to -\infty$ using $\epsilon$ and a value $N$.
    
- **Definition 1.4.4 & 1.4.5 (Infinite Limits):** Precise conditions for $f(x) \to \pm\infty$ using a value $M$ and $\delta$.
    

---

## Mathematical Questions, Ranging from Introductory Examples

### 1. Geometric and Rate of Change Problems

- **Tangent Line Calculation:** Find an equation for the tangent line to the parabola $y = x^2$ at specific points, such as $P(1, 1)$, $(-1, 1)$, or $(0, 0)$.
    
- **Slope Analysis:** Determine the slope of a secant line ($m_{sec}$) through points $P$ and $Q$ on a curve and use it to find the limiting slope of the tangent line ($m_{tan}$).
    
- **Area Approximation:** Conceptually determine the exact area under a curve by taking the limit of the sum of areas of inscribed rectangles as their number increases indefinitely.
    

### 2. Evaluative Limit Questions

- **Intuitive and Numerical Estimation:**
    
    - Use numerical evidence (tables of values) to conjecture limits, such as $\lim_{x \to 1} \frac{x-1}{\sqrt{x}-1}$, $\lim_{x \to 0} \frac{\sin x}{x}$, and limits for functions like $e^x - 1/x$.
        
    - Analyze "sampling pitfalls" where numerical data might falsely suggest a limit, as with $\lim_{x \to 0} \sin(\pi/x)$.
        
- **Algebraic Computation (Section 1.2):**
    
    - Polynomials: Find limits like $\lim_{x \to 5} (x^2 - 4x + 3)$ or $\lim_{x \to 1} (x^7 - 2x^5 + 1)^{35}$.
        
    - Rational Functions: Evaluate $\lim_{x \to 2} \frac{5x^3 + 4}{x-3}$ and identify limits of the form $L/0$ (which do not exist) or indeterminate forms of type $0/0$ that require factoring and cancellation.
        
    - Radicals: Rationalize the numerator or denominator to solve limits like $\lim_{x \to 1} \frac{x-1}{\sqrt{x}-1}$ or $\lim_{x \to 0} \frac{\sqrt{x+4}-2}{x}$.
        
    - Piecewise Functions: Determine if a two-sided limit exists by calculating and comparing one-sided limits at the boundary points.
        
- **Limits at Infinity and End Behavior (Section 1.3):**
    
    - Find horizontal asymptotes by evaluating limits as $x \to \pm\infty$ for rational functions and functions involving radicals.
        
    - Identify the end behavior of transcendental functions like $\ln x$, $e^x$, and $e^{-x}$.
        
    - Use the substitution principle to evaluate complex limits at infinity, such as $\lim_{x \to 0^+} e^{1/x}$.
        

### 3. Conceptual and Graphical Questions

- **Graph Interpretation:** Given the graph of a function, find specific values for: $\lim_{x \to a^-} f(x)$, $\lim_{x \to a^+} f(x)$, and $\lim_{x \to a} f(x)$.
    
    - Vertical asymptotes where the function rises or falls without bound.
        
- **Existence Criteria:** Explain why a limit fails to exist, such as in cases of oscillation, unbounded behavior, or unequal one-sided limits.
    
- **True/False Statements:** Test conceptual understanding of theorems, such as "If $\lim_{x \to a} f(x)$ exists, then so do $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$".
    

### 4. Rigorous (Epsilon-Delta) Proofs (Section 1.4)

- **Definition-Based Proofs:** Use the formal $\epsilon-\delta$ definition to prove specific limits, such as:
    
    - Linear functions: $\lim_{x \to 2} (3x - 5) = 1$.
        
    - Quadratic functions: $\lim_{x \to 3} x^2 = 9$.
        
    - Radical functions: $\lim_{x \to 0^+} \sqrt{x} = 0$.
        
- **Finding Delta:** Determine the largest value of $\delta$ that satisfies a given $\epsilon$ for a specific function.
    
- **Infinite Limit Proofs:** Use Definition 1.4.4 to prove limits like $\lim_{x \to 0} \frac{1}{x^2} = +\infty$.
    

### 5. Applied and Modeling Questions

- **Physics (Relativity):** Interpret limits of length ($l$) and mass ($m$) as speed $v$ approaches the speed of light $c$.
    
- **Environmental Science:** Use limits to describe the "carrying capacity" in population models as time $t \to +\infty$.
    
- **Newton's Law of Universal Gravitation:** Explain the limit of gravitational force as the distance between two masses approaches zero.
    

---








