# Calculus I Lecture Notes

## 1. Increasing and Decreasing Functions

### 1.1 Definitions

Let $f$ be a function defined on an interval $I$.

- $f$ is **increasing** on $I$ if for any $x_1, x_2 \in I$ with $x_1 < x_2$, we have $f(x_1) < f(x_2)$.
- $f$ is **decreasing** on $I$ if for any $x_1, x_2 \in I$ with $x_1 < x_2$, we have $f(x_1) > f(x_2)$.
- $f$ is **non-decreasing** on $I$ if $x_1 < x_2 \Rightarrow f(x_1) \le f(x_2)$.
- $f$ is **non-increasing** on $I$ if $x_1 < x_2 \Rightarrow f(x_1) \ge f(x_2)$.

### 1.2 Test for Monotonicity

**Theorem.** Let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$.

- If $f'(x) > 0$ for all $x \in (a,b)$, then $f$ is increasing on $[a,b]$.
- If $f'(x) < 0$ for all $x \in (a,b)$, then $f$ is decreasing on $[a,b]$.

*Proof.* For any $x_1, x_2 \in [a,b]$ with $x_1 < x_2$, by the Mean Value Theorem there exists $c \in (x_1, x_2)$ such that

$$f(x_2) - f(x_1) = f'(c)(x_2 - x_1)$$

If $f'(c) > 0$, then $f(x_2) - f(x_1) > 0$, so $f(x_2) > f(x_1)$. Hence $f$ is increasing. Similarly, if $f'(c) < 0$, then $f(x_2) - f(x_1) < 0$, so $f$ is decreasing.

### 1.3 First Derivative Test for Local Extrema

**Theorem.** Let $f$ be continuous at $c$ and differentiable near $c$ (except possibly at $c$).

- If $f'$ changes from positive to negative at $c$, then $f$ has a **local maximum** at $c$.
- If $f'$ changes from negative to positive at $c$, then $f$ has a **local minimum** at $c$.
- If $f'$ does not change sign, then $f$ has no local extremum at $c$.

**Example.** Find the intervals where $f(x) = x^3 - 3x$ is increasing or decreasing.

$$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$$

Setting $f'(x) = 0$ gives $x = -1$ and $x = 1$.

| Interval | $x+1$ | $x-1$ | $f'(x)$ | $f$ |
|---|---|---|---|---|
| $(-\infty, -1)$ | $-$ | $-$ | $+$ | Increasing |
| $(-1, 1)$ | $+$ | $-$ | $-$ | Decreasing |
| $(1, \infty)$ | $+$ | $+$ | $+$ | Increasing |

Thus $f$ is increasing on $(-\infty, -1)$ and $(1, \infty)$, and decreasing on $(-1, 1)$. By the first derivative test, $f$ has a local maximum at $x = -1$ and a local minimum at $x = 1$.

---

## 2. Concavity

### 2.1 Definitions

- A function $f$ is **concave up** (or convex) on an interval $I$ if the graph of $f$ lies above its tangent lines on $I$.
- A function $f$ is **concave down** (or concave) on $I$ if the graph of $f$ lies below its tangent lines on $I$.

**Test for Concavity.** If $f''(x)$ exists on $(a,b)$:

- If $f''(x) > 0$ for all $x \in (a,b)$, then $f$ is concave up on $(a,b)$.
- If $f''(x) < 0$ for all $x \in (a,b)$, then $f$ is concave down on $(a,b)$.

### 2.2 Inflection Points

A point $c$ where the concavity changes is called an **inflection point**. At an inflection point, $f''(c) = 0$ or $f''(c)$ does not exist.

**Example.** Find the inflection points of $f(x) = x^4 - 6x^2$.

$$f'(x) = 4x^3 - 12x$$
$$f''(x) = 12x^2 - 12 = 12(x^2 - 1)$$

Setting $f''(x) = 0$ gives $x = -1$ and $x = 1$.

- For $x < -1$, $f''(x) > 0$, so $f$ is concave up.
- For $-1 < x < 1$, $f''(x) < 0$, so $f$ is concave down.
- For $x > 1$, $f''(x) > 0$, so $f$ is concave up.

Thus $x = -1$ and $x = 1$ are inflection points.

### 2.3 Second Derivative Test for Local Extrema

**Theorem.** Let $f'(c) = 0$ and $f''(c)$ exist.

- If $f''(c) > 0$, then $f$ has a local minimum at $c$.
- If $f''(c) < 0$, then $f$ has a local maximum at $c$.
- If $f''(c) = 0$, the test is inconclusive.

---



## 3. Rolle's Theorem

**Theorem (Rolle).** Let $f$ be a function that satisfies:

1. $f$ is continuous on the closed interval $[a,b]$.
2. $f$ is differentiable on the open interval $(a,b)$.
3. $f(a) = f(b)$.

Then there exists at least one $c \in (a,b)$ such that $f'(c) = 0$.

*Proof.* Since $f$ is continuous on $[a,b]$, by the Extreme Value Theorem, $f$ attains its maximum and minimum values on $[a,b]$.

If both the maximum and minimum occur at the endpoints $a$ and $b$, then since $f(a) = f(b)$, $f$ is constant on $[a,b]$, so $f'(x) = 0$ for all $x \in (a,b)$.

Otherwise, at least one extremum occurs at an interior point $c \in (a,b)$. Since $f$ is differentiable at $c$ and $c$ is a local extremum, by Fermat's Theorem, $f'(c) = 0$.

**Example.** Verify Rolle's Theorem for $f(x) = x^2 - 4x + 3$ on $[1,3]$.

- $f$ is a polynomial, hence continuous on $[1,3]$ and differentiable on $(1,3)$.
- $f(1) = 1 - 4 + 3 = 0$ and $f(3) = 9 - 12 + 3 = 0$, so $f(1) = f(3)$.
- $f'(x) = 2x - 4$. Setting $f'(c) = 0$ gives $2c - 4 = 0$, so $c = 2 \in (1,3)$.

Thus Rolle's Theorem is verified.

---

## 4. The Mean Value Theorem

**Theorem (Mean Value Theorem).** Let $f$ be a function that satisfies:

1. $f$ is continuous on $[a,b]$.
2. $f$ is differentiable on $(a,b)$.

Then there exists at least one $c \in (a,b)$ such that

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

*Proof.* Define a function $g(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a)$.

Then $g(a) = f(a) - f(a) - \frac{f(b) - f(a)}{b - a}(a - a) = 0$.
Also $g(b) = f(b) - f(a) - \frac{f(b) - f(a)}{b - a}(b - a) = f(b) - f(a) - (f(b) - f(a)) = 0$.

Thus $g(a) = g(b) = 0$. Since $g$ is continuous on $[a,b]$ and differentiable on $(a,b)$, by Rolle's Theorem there exists $c \in (a,b)$ such that $g'(c) = 0$.

$$g'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$$

Setting $g'(c) = 0$ gives $f'(c) = \frac{f(b) - f(a)}{b - a}$.

### 4.1 Geometrical Interpretation

The Mean Value Theorem states that there is at least one point $c \in (a,b)$ where the tangent line to the curve $y = f(x)$ is parallel to the secant line joining $(a, f(a))$ and $(b, f(b))$.

### 4.2 Consequences of the MVT

**Corollary 1.** If $f'(x) = 0$ for all $x \in (a,b)$, then $f$ is constant on $(a,b)$.

**Corollary 2.** If $f'(x) = g'(x)$ for all $x \in (a,b)$, then $f(x) = g(x) + C$ for some constant $C$.

**Corollary 3.** If $f'(x) > 0$ for all $x \in (a,b)$, then $f$ is increasing on $(a,b)$. If $f'(x) < 0$ for all $x \in (a,b)$, then $f$ is decreasing on $(a,b)$.

**Example.** Verify the Mean Value Theorem for $f(x) = \sqrt{x}$ on $[0,4]$.

- $f$ is continuous on $[0,4]$ and differentiable on $(0,4)$.
- $f(4) - f(0) = 2 - 0 = 2$ and $b - a = 4$.
- $\frac{f(b) - f(a)}{b - a} = \frac{2}{4} = \frac{1}{2}$.
- $f'(x) = \frac{1}{2\sqrt{x}}$. Setting $f'(c) = \frac{1}{2}$ gives $\frac{1}{2\sqrt{c}} = \frac{1}{2}$, so $\sqrt{c} = 1$, hence $c = 1 \in (0,4)$.

**Example (Velocity).** A car travels 120 km in 2 hours. Show that at some instant, the car's speed was exactly 60 km/h.

Let $s(t)$ be the position at time $t$. By the MVT, there exists $c \in (0,2)$ such that $s'(c) = \frac{s(2) - s(0)}{2 - 0} = \frac{120}{2} = 60$ km/h.

---

## 5. Successive Differentiation

### 5.1 Notation

If $y = f(x)$ is a differentiable function, then its derivative is denoted by

$$y' = f'(x) = \frac{dy}{dx}$$

The derivative of $y'$ is the **second derivative**:

$$y'' = f''(x) = \frac{d^2y}{dx^2}$$

In general, the **$n$th derivative** is denoted by

$$y^{(n)} = f^{(n)}(x) = \frac{d^n y}{dx^n}$$

### 5.2 nth Derivatives of Standard Functions

1. **Power function:** If $y = x^m$, then
   $$y^{(n)} = m(m-1)(m-2)\cdots(m-n+1)x^{m-n}$$

2. **Exponential function:** If $y = e^{ax}$, then
   $$y^{(n)} = a^n e^{ax}$$

3. **Sine function:** If $y = \sin(ax + b)$, then
   $$y^{(n)} = a^n \sin\left(ax + b + \frac{n\pi}{2}\right)$$

4. **Cosine function:** If $y = \cos(ax + b)$, then
   $$y^{(n)} = a^n \cos\left(ax + b + \frac{n\pi}{2}\right)$$

5. **Logarithmic function:** If $y = \ln(ax + b)$, then
   $$y^{(n)} = \frac{(-1)^{n-1}(n-1)!\, a^n}{(ax + b)^n}$$

6. **Rational function:** If $y = \frac{1}{ax + b}$, then
   $$y^{(n)} = \frac{(-1)^n n!\, a^n}{(ax + b)^{n+1}}$$

### 5.3 Examples

**Example 1.** Find the $n$th derivative of $y = \frac{1}{1 - x}$.

$$y = \frac{1}{1 - x} = (1 - x)^{-1}$$
$$y' = (1 - x)^{-2}$$
$$y'' = 2(1 - x)^{-3}$$
$$y''' = 6(1 - x)^{-4}$$

In general:

$$y^{(n)} = \frac{n!}{(1 - x)^{n+1}}$$

**Example 2.** Find the $n$th derivative of $y = e^{2x}\sin(3x)$.

This requires Leibnitz Theorem (see next section).

---



## 6. Leibnitz Theorem

**Theorem (Leibnitz).** If $u$ and $v$ are functions of $x$ that possess $n$th derivatives, then the $n$th derivative of their product is given by

$$(uv)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} u^{(n-k)} v^{(k)}$$

where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ are the binomial coefficients.

*Proof.* By induction on $n$.

**Base case $n = 1$:** $(uv)' = u'v + uv' = \binom{1}{0}u'v + \binom{1}{1}uv'$. ✓

**Inductive step:** Assume the formula holds for $n$. Then

$$(uv)^{(n+1)} = \frac{d}{dx}\left[\sum_{k=0}^{n} \binom{n}{k} u^{(n-k)} v^{(k)}\right]$$
$$= \sum_{k=0}^{n} \binom{n}{k} \left[u^{(n+1-k)} v^{(k)} + u^{(n-k)} v^{(k+1)}\right]$$
$$= \sum_{k=0}^{n} \binom{n}{k} u^{(n+1-k)} v^{(k)} + \sum_{k=1}^{n+1} \binom{n}{k-1} u^{(n+1-k)} v^{(k)}$$
$$= \binom{n}{0} u^{(n+1)} v^{(0)} + \sum_{k=1}^{n} \left[\binom{n}{k} + \binom{n}{k-1}\right] u^{(n+1-k)} v^{(k)} + \binom{n}{n} u^{(0)} v^{(n+1)}$$
$$= \sum_{k=0}^{n+1} \binom{n+1}{k} u^{(n+1-k)} v^{(k)}$$

using Pascal's identity $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$.

### 6.1 Examples

**Example 1.** Find $y^{(n)}$ if $y = x^2 e^{ax}$.

Let $u = e^{ax}$ and $v = x^2$.

$$u^{(k)} = a^k e^{ax}$$
$$v' = 2x, \quad v'' = 2, \quad v^{(k)} = 0 \text{ for } k \ge 3$$

By Leibnitz Theorem:

$$y^{(n)} = \sum_{k=0}^{n} \binom{n}{k} u^{(n-k)} v^{(k)}$$
$$= \binom{n}{0} e^{ax} \cdot a^n \cdot x^2 + \binom{n}{1} e^{ax} \cdot a^{n-1} \cdot 2x + \binom{n}{2} e^{ax} \cdot a^{n-2} \cdot 2$$
$$= e^{ax} \left[a^n x^2 + 2n a^{n-1} x + n(n-1) a^{n-2}\right]$$

**Example 2.** Find $y^{(n)}$ if $y = x \sin x$.

Let $u = \sin x$ and $v = x$.

$$u^{(k)} = \sin\left(x + \frac{k\pi}{2}\right)$$
$$v' = 1, \quad v^{(k)} = 0 \text{ for } k \ge 2$$

By Leibnitz Theorem:

$$y^{(n)} = \binom{n}{0} \sin\left(x + \frac{n\pi}{2}\right) \cdot x + \binom{n}{1} \sin\left(x + \frac{(n-1)\pi}{2}\right) \cdot 1$$
$$= x \sin\left(x + \frac{n\pi}{2}\right) + n \sin\left(x + \frac{(n-1)\pi}{2}\right)$$

**Example 3.** Find $y^{(n)}$ if $y = e^{2x} \sin(3x)$.

Let $u = e^{2x}$ and $v = \sin(3x)$.

$$u^{(k)} = 2^k e^{2x}$$
$$v^{(k)} = 3^k \sin\left(3x + \frac{k\pi}{2}\right)$$

By Leibnitz Theorem:

$$y^{(n)} = \sum_{k=0}^{n} \binom{n}{k} 2^{n-k} e^{2x} \cdot 3^k \sin\left(3x + \frac{k\pi}{2}\right)$$
$$= e^{2x} \sum_{k=0}^{n} \binom{n}{k} 2^{n-k} 3^k \sin\left(3x + \frac{k\pi}{2}\right)$$

---

## 7. Maclaurin's Theorem

**Theorem (Maclaurin).** If $f$ is a function that can be differentiated $n$ times in an interval containing $0$, then

$$f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots + \frac{f^{(n)}(0)}{n!}x^n + R_n(x)$$

where $R_n(x)$ is the remainder term given by

$$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}x^{n+1}$$

for some $\xi$ between $0$ and $x$.

### 7.1 Maclaurin Series of Standard Functions

**Exponential function:**

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$

**Sine function:**

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$$

**Cosine function:**

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$$

**Logarithmic function:**

$$\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}, \quad -1 < x \le 1$$

**Binomial series:**

$$(1+x)^m = 1 + mx + \frac{m(m-1)}{2!}x^2 + \frac{m(m-1)(m-2)}{3!}x^3 + \cdots, \quad |x| < 1$$

### 7.2 Examples

**Example 1.** Find the Maclaurin series for $f(x) = \sin x$ up to the $x^5$ term.

$$f(x) = \sin x, \quad f(0) = 0$$
$$f'(x) = \cos x, \quad f'(0) = 1$$
$$f''(x) = -\sin x, \quad f''(0) = 0$$
$$f'''(x) = -\cos x, \quad f'''(0) = -1$$
$$f^{(4)}(x) = \sin x, \quad f^{(4)}(0) = 0$$
$$f^{(5)}(x) = \cos x, \quad f^{(5)}(0) = 1$$

Thus:

$$\sin x = 0 + 1\cdot x + 0\cdot x^2 + \frac{-1}{3!}x^3 + 0\cdot x^4 + \frac{1}{5!}x^5 + \cdots$$
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

**Example 2.** Find the Maclaurin series for $f(x) = e^{2x}$.

Using $e^u = \sum_{n=0}^{\infty} \frac{u^n}{n!}$ with $u = 2x$:

$$e^{2x} = \sum_{n=0}^{\infty} \frac{(2x)^n}{n!} = \sum_{n=0}^{\infty} \frac{2^n x^n}{n!} = 1 + 2x + \frac{4x^2}{2!} + \frac{8x^3}{3!} + \cdots$$

---

## 8. Taylor's Theorem

**Theorem (Taylor).** If $f$ is a function that can be differentiated $n$ times in an interval containing $a$, then

$$f(x) = f(a) + \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n(x)$$

where $R_n(x)$ is the remainder term given by

$$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}$$

for some $\xi$ between $a$ and $x$.

Note that Taylor's Theorem generalizes Maclaurin's Theorem (which is the special case $a = 0$).

### 8.1 Taylor Series

The Taylor series of $f$ about $x = a$ is

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

### 8.2 Examples

**Example 1.** Find the Taylor series for $f(x) = \ln x$ about $x = 1$.

$$f(x) = \ln x, \quad f(1) = 0$$
$$f'(x) = \frac{1}{x}, \quad f'(1) = 1$$
$$f''(x) = -\frac{1}{x^2}, \quad f''(1) = -1$$
$$f'''(x) = \frac{2}{x^3}, \quad f'''(1) = 2$$
$$f^{(4)}(x) = -\frac{6}{x^4}, \quad f^{(4)}(1) = -6$$

Thus:

$$\ln x = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \frac{(x-1)^4}{4} + \cdots$$

**Example 2.** Find the Taylor series for $f(x) = e^x$ about $x = 2$.

$$f^{(n)}(x) = e^x, \quad f^{(n)}(2) = e^2$$

Thus:

$$e^x = e^2 + e^2(x-2) + \frac{e^2}{2!}(x-2)^2 + \frac{e^2}{3!}(x-2)^3 + \cdots = e^2 \sum_{n=0}^{\infty} \frac{(x-2)^n}{n!}$$

---



## 9. Partial Derivatives

### 9.1 Definition

Let $z = f(x,y)$ be a function of two variables. The **partial derivative** of $f$ with respect to $x$ at $(x_0, y_0)$ is

$$\frac{\partial f}{\partial x}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}$$

provided the limit exists. Similarly, the partial derivative with respect to $y$ is

$$\frac{\partial f}{\partial y}(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0, y_0 + h) - f(x_0, y_0)}{h}$$

### 9.2 Notation

$$\frac{\partial f}{\partial x} = f_x = D_x f = \partial_x f$$
$$\frac{\partial f}{\partial y} = f_y = D_y f = \partial_y f$$

### 9.3 Higher Order Partial Derivatives

$$\frac{\partial^2 f}{\partial x^2} = f_{xx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right)$$
$$\frac{\partial^2 f}{\partial y^2} = f_{yy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$$
$$\frac{\partial^2 f}{\partial x \partial y} = f_{xy} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$$
$$\frac{\partial^2 f}{\partial y \partial x} = f_{yx} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$$

**Theorem (Clairaut).** If $f_{xy}$ and $f_{yx}$ are continuous at $(a,b)$, then $f_{xy}(a,b) = f_{yx}(a,b)$. That is, mixed partial derivatives are equal under continuity.

### 9.4 Examples

**Example 1.** Find the first and second order partial derivatives of $f(x,y) = x^3y^2 + 2xy + \sin x$.

$$f_x = 3x^2y^2 + 2y + \cos x$$
$$f_y = 2x^3y + 2x$$
$$f_{xx} = 6xy^2 - \sin x$$
$$f_{yy} = 2x^3$$
$$f_{xy} = 6x^2y + 2$$
$$f_{yx} = 6x^2y + 2$$

Note that $f_{xy} = f_{yx}$, confirming Clairaut's Theorem.

**Example 2.** Find $\frac{\partial z}{\partial x}$ and $\frac{\partial z}{\partial y}$ if $z = e^{xy}\ln(1 + x^2y)$.

$$\frac{\partial z}{\partial x} = ye^{xy}\ln(1 + x^2y) + e^{xy} \cdot \frac{2xy}{1 + x^2y}$$
$$\frac{\partial z}{\partial y} = xe^{xy}\ln(1 + x^2y) + e^{xy} \cdot \frac{x^2}{1 + x^2y}$$

### 9.5 Chain Rule for Partial Derivatives

If $z = f(x,y)$ and $x = g(t)$, $y = h(t)$, then

$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

If $z = f(x,y)$ and $x = g(s,t)$, $y = h(s,t)$, then

$$\frac{\partial z}{\partial s} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial s}$$
$$\frac{\partial z}{\partial t} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial t}$$

**Example.** If $z = x^2y + y^2$, where $x = \sin t$ and $y = e^t$, find $\frac{dz}{dt}$.

$$\frac{\partial z}{\partial x} = 2xy, \quad \frac{\partial z}{\partial y} = x^2 + 2y$$
$$\frac{dx}{dt} = \cos t, \quad \frac{dy}{dt} = e^t$$

$$\frac{dz}{dt} = 2xy\cos t + (x^2 + 2y)e^t$$
$$= 2\sin t \cdot e^t \cdot \cos t + (\sin^2 t + 2e^t)e^t$$
$$= 2e^t\sin t\cos t + e^t\sin^2 t + 2e^{2t}$$
$$= e^t(2\sin t\cos t + \sin^2 t) + 2e^{2t}$$

---

## 10. Euler's Theorem on Homogeneous Functions

### 10.1 Homogeneous Functions

**Definition.** A function $f(x,y)$ is said to be **homogeneous of degree $n$** if for any scalar $t \neq 0$,

$$f(tx, ty) = t^n f(x,y)$$

**Examples:**

- $f(x,y) = x^2 + y^2$ is homogeneous of degree 2.
- $f(x,y) = \frac{x^2 + y^2}{x + y}$ is homogeneous of degree 1.
- $f(x,y) = \sqrt{x^2 + y^2}$ is homogeneous of degree 1.
- $f(x,y) = \sin\left(\frac{y}{x}\right)$ is homogeneous of degree 0.

### 10.2 Euler's Theorem

**Theorem (Euler).** If $f(x,y)$ is a homogeneous function of degree $n$, then

$$x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = n f(x,y)$$

*Proof.* Since $f$ is homogeneous of degree $n$,

$$f(tx, ty) = t^n f(x,y)$$

Differentiate both sides with respect to $t$ using the chain rule:

$$\frac{\partial}{\partial t}f(tx, ty) = x\frac{\partial f}{\partial (tx)} + y\frac{\partial f}{\partial (ty)} = n t^{n-1} f(x,y)$$

Setting $t = 1$:

$$x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = n f(x,y)$$

### 10.3 Examples

**Example 1.** Verify Euler's Theorem for $f(x,y) = x^3 + y^3$.

$$f(tx, ty) = (tx)^3 + (ty)^3 = t^3(x^3 + y^3) = t^3 f(x,y)$$

So $f$ is homogeneous of degree 3.

$$\frac{\partial f}{\partial x} = 3x^2, \quad \frac{\partial f}{\partial y} = 3y^2$$

$$x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = x(3x^2) + y(3y^2) = 3x^3 + 3y^3 = 3(x^3 + y^3) = 3f(x,y)$$

Euler's Theorem is verified.

**Example 2.** Verify Euler's Theorem for $f(x,y) = \frac{x}{x^2 + y^2}$.

$$f(tx, ty) = \frac{tx}{(tx)^2 + (ty)^2} = \frac{tx}{t^2(x^2 + y^2)} = t^{-1} \frac{x}{x^2 + y^2} = t^{-1} f(x,y)$$

So $f$ is homogeneous of degree $-1$.

$$\frac{\partial f}{\partial x} = \frac{(x^2 + y^2)(1) - x(2x)}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}$$
$$\frac{\partial f}{\partial y} = \frac{0 - x(2y)}{(x^2 + y^2)^2} = \frac{-2xy}{(x^2 + y^2)^2}$$

$$x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = x\frac{y^2 - x^2}{(x^2 + y^2)^2} + y\frac{-2xy}{(x^2 + y^2)^2}$$
$$= \frac{xy^2 - x^3 - 2xy^2}{(x^2 + y^2)^2} = \frac{-x^3 - xy^2}{(x^2 + y^2)^2}$$
$$= -\frac{x(x^2 + y^2)}{(x^2 + y^2)^2} = -\frac{x}{x^2 + y^2} = -f(x,y)$$

Euler's Theorem is verified with $n = -1$.

### 10.4 Second Order Euler's Theorem

**Theorem.** If $f(x,y)$ is a homogeneous function of degree $n$, then

$$x^2\frac{\partial^2 f}{\partial x^2} + 2xy\frac{\partial^2 f}{\partial x \partial y} + y^2\frac{\partial^2 f}{\partial y^2} = n(n-1)f(x,y)$$

---



## 11. Integration

### 11.1 Indefinite Integrals

**Definition.** A function $F$ is called an **antiderivative** (or primitive) of $f$ on an interval $I$ if $F'(x) = f(x)$ for all $x \in I$.

The **indefinite integral** of $f$ with respect to $x$ is denoted by

$$\int f(x)\,dx = F(x) + C$$

where $C$ is an arbitrary constant called the **constant of integration**.

### 11.2 Basic Integration Formulas

1. $\int x^n\,dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1$

2. $\int \frac{1}{x}\,dx = \ln|x| + C$

3. $\int e^{ax}\,dx = \frac{1}{a}e^{ax} + C$

4. $\int a^x\,dx = \frac{a^x}{\ln a} + C$

5. $\int \sin x\,dx = -\cos x + C$

6. $\int \cos x\,dx = \sin x + C$

7. $\int \sec^2 x\,dx = \tan x + C$

8. $\int \csc^2 x\,dx = -\cot x + C$

9. $\int \sec x \tan x\,dx = \sec x + C$

10. $\int \csc x \cot x\,dx = -\csc x + C$

11. $\int \frac{1}{\sqrt{1-x^2}}\,dx = \sin^{-1} x + C$

12. $\int \frac{1}{1+x^2}\,dx = \tan^{-1} x + C$

13. $\int \frac{1}{|x|\sqrt{x^2-1}}\,dx = \sec^{-1} x + C$

### 11.3 Properties of Indefinite Integrals

1. **Constant multiple:** $\int k f(x)\,dx = k \int f(x)\,dx$

2. **Sum/Difference:** $\int [f(x) \pm g(x)]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$

### 11.4 Examples

**Example 1.** Evaluate $\int (3x^2 + 2x - 5)\,dx$.

$$\int (3x^2 + 2x - 5)\,dx = 3\int x^2\,dx + 2\int x\,dx - 5\int 1\,dx$$
$$= 3\cdot\frac{x^3}{3} + 2\cdot\frac{x^2}{2} - 5x + C$$
$$= x^3 + x^2 - 5x + C$$

**Example 2.** Evaluate $\int \left(\frac{1}{x} + e^x + \cos x\right)dx$.

$$\int \left(\frac{1}{x} + e^x + \cos x\right)dx = \ln|x| + e^x + \sin x + C$$

---

## 12. The Substitution Rule

**Theorem (Substitution Rule).** If $u = g(x)$ is a differentiable function and $f$ is continuous on the range of $g$, then

$$\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$$

### 12.1 Examples

**Example 1.** Evaluate $\int 2x\cos(x^2)\,dx$.

Let $u = x^2$, so $du = 2x\,dx$.

$$\int 2x\cos(x^2)\,dx = \int \cos u\,du = \sin u + C = \sin(x^2) + C$$

**Example 2.** Evaluate $\int \frac{2x}{1 + x^2}\,dx$.

Let $u = 1 + x^2$, so $du = 2x\,dx$.

$$\int \frac{2x}{1 + x^2}\,dx = \int \frac{du}{u} = \ln|u| + C = \ln|1 + x^2| + C$$

**Example 3.** Evaluate $\int xe^{x^2}\,dx$.

Let $u = x^2$, so $du = 2x\,dx$, which implies $x\,dx = \frac{1}{2}du$.

$$\int xe^{x^2}\,dx = \int e^u \cdot \frac{1}{2}du = \frac{1}{2}e^u + C = \frac{1}{2}e^{x^2} + C$$

**Example 4.** Evaluate $\int \tan x\,dx$.

$$\int \tan x\,dx = \int \frac{\sin x}{\cos x}\,dx$$

Let $u = \cos x$, so $du = -\sin x\,dx$.

$$\int \frac{\sin x}{\cos x}\,dx = -\int \frac{du}{u} = -\ln|u| + C = -\ln|\cos x| + C = \ln|\sec x| + C$$

---

## 13. Trigonometric Integrals

### 13.1 Integrals of Powers of Sine and Cosine

**Type 1:** $\int \sin^n x\,dx$ or $\int \cos^n x\,dx$ (odd $n$)

If $n$ is odd, factor out one power and use $\sin^2 x = 1 - \cos^2 x$ (or $\cos^2 x = 1 - \sin^2 x$), then substitute.

**Example.** Evaluate $\int \sin^3 x\,dx$.

$$\int \sin^3 x\,dx = \int \sin^2 x \cdot \sin x\,dx = \int (1 - \cos^2 x)\sin x\,dx$$

Let $u = \cos x$, $du = -\sin x\,dx$.

$$\int (1 - \cos^2 x)\sin x\,dx = -\int (1 - u^2)\,du = -\left(u - \frac{u^3}{3}\right) + C$$
$$= -\cos x + \frac{\cos^3 x}{3} + C$$

**Type 2:** $\int \sin^n x\,dx$ or $\int \cos^n x\,dx$ (even $n$)

Use the half-angle formulas:

$$\sin^2 x = \frac{1 - \cos(2x)}{2}, \quad \cos^2 x = \frac{1 + \cos(2x)}{2}$$

**Example.** Evaluate $\int \sin^2 x\,dx$.

$$\int \sin^2 x\,dx = \int \frac{1 - \cos(2x)}{2}\,dx = \frac{1}{2}\int (1 - \cos(2x))\,dx$$
$$= \frac{1}{2}\left(x - \frac{\sin(2x)}{2}\right) + C = \frac{x}{2} - \frac{\sin(2x)}{4} + C$$

**Type 3:** $\int \sin^m x \cos^n x\,dx$

- If $m$ is odd, factor out $\sin x$, write the rest in terms of $\cos x$, substitute $u = \cos x$.
- If $n$ is odd, factor out $\cos x$, write the rest in terms of $\sin x$, substitute $u = \sin x$.
- If both $m$ and $n$ are even, use half-angle formulas.

**Example.** Evaluate $\int \sin^2 x \cos^3 x\,dx$.

Since $n = 3$ is odd:

$$\int \sin^2 x \cos^3 x\,dx = \int \sin^2 x \cos^2 x \cos x\,dx = \int \sin^2 x (1 - \sin^2 x) \cos x\,dx$$

Let $u = \sin x$, $du = \cos x\,dx$.

$$\int u^2 (1 - u^2)\,du = \int (u^2 - u^4)\,du = \frac{u^3}{3} - \frac{u^5}{5} + C = \frac{\sin^3 x}{3} - \frac{\sin^5 x}{5} + C$$

**Example.** Evaluate $\int \sin^2 x \cos^2 x\,dx$.

Both powers are even. Use half-angle formulas:

$$\sin^2 x \cos^2 x = \frac{1 - \cos(2x)}{2} \cdot \frac{1 + \cos(2x)}{2} = \frac{1 - \cos^2(2x)}{4} = \frac{1}{4} - \frac{\cos^2(2x)}{4}$$
$$= \frac{1}{4} - \frac{1}{4} \cdot \frac{1 + \cos(4x)}{2} = \frac{1}{4} - \frac{1}{8} - \frac{\cos(4x)}{8} = \frac{1}{8} - \frac{\cos(4x)}{8}$$

$$\int \sin^2 x \cos^2 x\,dx = \int \left(\frac{1}{8} - \frac{\cos(4x)}{8}\right)dx = \frac{x}{8} - \frac{\sin(4x)}{32} + C$$

### 13.2 Integrals of Powers of Tangent and Secant

$$\int \tan x\,dx = \ln|\sec x| + C$$
$$\int \sec x\,dx = \ln|\sec x + \tan x| + C$$
$$\int \sec^2 x\,dx = \tan x + C$$
$$\int \sec x \tan x\,dx = \sec x + C$$

**Example.** Evaluate $\int \tan^3 x\,dx$.

$$\int \tan^3 x\,dx = \int \tan x (\sec^2 x - 1)\,dx = \int \tan x \sec^2 x\,dx - \int \tan x\,dx$$

For the first integral, let $u = \tan x$, $du = \sec^2 x\,dx$.

$$\int \tan x \sec^2 x\,dx = \int u\,du = \frac{u^2}{2} + C_1 = \frac{\tan^2 x}{2} + C_1$$

Thus:

$$\int \tan^3 x\,dx = \frac{\tan^2 x}{2} - \ln|\sec x| + C$$

### 13.3 Trigonometric Substitution

For integrals involving $\sqrt{a^2 - x^2}$, use $x = a\sin\theta$.
For $\sqrt{a^2 + x^2}$, use $x = a\tan\theta$.
For $\sqrt{x^2 - a^2}$, use $x = a\sec\theta$.

**Example.** Evaluate $\int \sqrt{1 - x^2}\,dx$.

Let $x = \sin\theta$, so $dx = \cos\theta\,d\theta$, and $\sqrt{1 - x^2} = \cos\theta$.

$$\int \sqrt{1 - x^2}\,dx = \int \cos^2\theta\,d\theta = \int \frac{1 + \cos(2\theta)}{2}d\theta$$
$$= \frac{1}{2}\left(\theta + \frac{\sin(2\theta)}{2}\right) + C = \frac{1}{2}(\theta + \sin\theta\cos\theta) + C$$
$$= \frac{1}{2}(\sin^{-1} x + x\sqrt{1 - x^2}) + C$$

---

## 14. The Fundamental Theorem of Calculus

### 14.1 FTC Part 1

**Theorem (FTC Part 1).** If $f$ is continuous on $[a,b]$, then the function $F$ defined by

$$F(x) = \int_a^x f(t)\,dt$$

is continuous on $[a,b]$, differentiable on $(a,b)$, and

$$F'(x) = f(x)$$

### 14.2 FTC Part 2

**Theorem (FTC Part 2).** If $f$ is continuous on $[a,b]$ and $F$ is any antiderivative of $f$, then

$$\int_a^b f(x)\,dx = F(b) - F(a)$$

### 14.3 Examples

**Example 1.** Evaluate $\int_0^1 x^2\,dx$.

$$\int_0^1 x^2\,dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3} - 0 = \frac{1}{3}$$

**Example 2.** Evaluate $\int_0^{\pi} \sin x\,dx$.

$$\int_0^{\pi} \sin x\,dx = [-\cos x]_0^{\pi} = -\cos\pi + \cos 0 = -(-1) + 1 = 2$$

**Example 3.** Evaluate $\frac{d}{dx}\int_0^{x^2} \sin(t^2)\,dt$.

By FTC Part 1 and the chain rule:

$$\frac{d}{dx}\int_0^{x^2} \sin(t^2)\,dt = \sin((x^2)^2) \cdot 2x = 2x \sin(x^4)$$

---

*End of Calculus I Lecture Notes*
