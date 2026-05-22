---
links:
  - "[[Calculus]]"
---
## Increasing/Decreasing Functions

The derivative of a function may be used to determine whether the function is increasing or decreasing on any intervals in its domain. If $f'(x) > 0$ at each point in an interval I, then the function is said to be increasing on I. $f'(x) < 0$ at each point in an interval I, then the function is said to be _decreasing on I_. Because the derivative is zero or does not exist only at critical points of the function, it must be positive or negative at all other points where the function exists.

---

### Second Image

Figure 5.1.1
![[Pasted image 20260519154138.png]]

> **5.1.1 DEFINITION.** Let $f$ be defined on an interval, and let $x_1$ and $x_2$ denote points in that interval.
> 
> (a) $f$ is **increasing** on the interval if $f(x_1) < f(x_2)$ whenever $x_1 < x_2$.
> 
> (b) $f$ is **decreasing** on the interval if $f(x_1) > f(x_2)$ whenever $x_1 < x_2$.
> 
> (c) $f$ is **constant** on the interval if $f(x_1) = f(x_2)$ for all points $x_1$ and $x_2$.
![[Pasted image 20260519184140.png]]
### Example 1

Find the intervals on which the following functions are increasing and the intervals on which they are decreasing.

(a) $f(x) = x^2 - 4x + 3$ (b) $f(x) = x^3$

_Solution (a)._ The graph of $f$ in Figure 5.1.4 suggests that $f$ is decreasing for $x \le 2$ and increasing for $x \ge 2$. To confirm this, we differentiate $f$ to obtain

$$f'(x) = 2x - 4 = 2(x - 2)$$

It follows that

$$f'(x) < 0 \text{ if } -\infty < x < 2$$

$$f'(x) > 0 \text{ if } 2 < x < +\infty$$

Since $f$ is continuous at $x = 2$, it follows from Theorem 5.1.2 and the subsequent remark that

$$f \text{ is decreasing on } (-\infty, 2]$$

$$f \text{ is increasing on } [2, +\infty)$$

These conclusions are consistent with the graph of $f$ in Figure 5.1.4.

_Solution (b)._ The graph of $f$ in Figure 5.1.5 suggests that $f$ is increasing over the entire $x$-axis. To confirm this, we differentiate $f$ to obtain $f'(x) = 3x^2$. Thus,

$$f'(x) > 0 \text{ if } -\infty < x < 0$$

$$f'(x) > 0 \text{ if } 0 < x < +\infty$$

Their Graphs

Since $f$ is continuous at $x = 0$,

$$f \text{ is increasing on } (-\infty, 0]$$

$$f \text{ is increasing on } [0, +\infty)$$

Hence $f$ is increasing over the entire interval $(-\infty, +\infty)$, which is consistent with the graph.

### Example 2

(a) Use the graph of $f(x) = 3x^4 + 4x^3 - 12x^2 + 2$ in Figure 5.1.6 to make a conjecture about the intervals on which $f$ is increasing or decreasing.

(b) Use Theorem 5.1.2 to determine whether your conjecture is correct.

_Solution (a)._ The graph suggests that $f$ is decreasing if $x \le -2$, increasing if $-2 \le x \le 0$, decreasing if $0 \le x \le 1$, and increasing if $x \ge 1$.

_Solution (b)._ Differentiating $f$ we obtain

$$f'(x) = 12x^3 + 12x^2 - 24x = 12x(x^2 + x - 2) = 12x(x + 2)(x - 1)$$

The sign analysis of $f'$ in Table 5.1.1 can be obtained using the method of test points discussed in Appendix A. The conclusions in that table confirm the conjecture in part (a). ◄

---

### Table 5.1.1

| **INTERVAL** | **12x** | **x+2** | **x−1** | **f′** | **CONCLUSION**                       |
| ------------ | ------- | ------- | ------- | ------ | ------------------------------------ |
| $x < -2$     | $-$     | $-$     | $-$     | $-$    | $f$ is decreasing on $(-\infty, -2]$ |
| $-2 < x < 0$ | $-$     | $+$     | $-$     | $+$    | $f$ is increasing on $[-2, 0]$       |
| $0 < x < 1$  | $+$     | $+$     | $-$     | $-$    | $f$ is decreasing on $[0, 1]$        |
| $1 < x$      | $+$     | $+$     | $+$     | $+$    | $f$ is increasing on $[1, +\infty)$  |


**Example 1:** For $f(x) = x^4 - 8x^2$ determine all intervals where $f$ is increasing or decreasing.

The domain of $f(x)$ is all real numbers, and its critical points occur at $x = -2, 0$, and $2$. Testing all intervals to the left and right of these values for $f'(x) = 4x^3 - 16x$, you find that

$$f'(x) < 0 \text{ on } (-\infty, -2)$$

$$f'(x) > 0 \text{ on } (-2, 0)$$

$$f'(x) < 0 \text{ on } (0, 2)$$

$$f'(x) > 0 \text{ on } (2, +\infty)$$

hence, $f$ is increasing on $(-2,0)$ and $(2, +\infty)$ and decreasing on $(-\infty, -2)$ and $(0,2)$.



## Increasing and Decreasing Functions Definition

- **Increasing Function** - A function $f(x)$ is said to be increasing on an interval $I$ if for any two numbers $x$ and $y$ in $I$ such that $x < y$, we have $f(x) \le f(y)$.
    
- **Decreasing Function** - A function $f(x)$ is said to be decreasing on an interval $I$ if for any two numbers $x$ and $y$ in $I$ such that $x < y$, we have $f(x) \ge f(y)$.
    
- **Strictly Increasing Function** - A function $f(x)$ is said to be strictly increasing on an interval $I$ if for any two numbers $x$ and $y$ in $I$ such that $x < y$, we have $f(x) < f(y)$.
    
- **Strictly Decreasing Function** - A function $f(x)$ is said to be strictly decreasing on an interval $I$ if for any two numbers $x$ and $y$ in $I$ such that $x < y$, we have $f(x) > f(y)$.