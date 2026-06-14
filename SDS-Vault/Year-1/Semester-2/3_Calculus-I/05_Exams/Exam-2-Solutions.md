# Exam-2 Solutions

*Answers taken **verbatim** from the lecture notes only.*

---

### 1. What do you mean by mean value theorem? **[3]**

The mean value theorem states that for a curve passing through two given points there is one point on the curve where the tangent is parallel to the secant passing through the two given points. The mean value theorem states that for any function f(x) whose graph passes through two given points (a, f(a)), (b, f(b)), there is at least one point (c, f(c)) on the curve where the tangent is parallel to the secant passing through the two given points. The mean value theorem is defined herein calculus for a function f(x): [a, b] → R, such that it is continuous and differentiable across an interval.

- The function f(x) is continuous over the interval [a, b].
- The function f(x) is differentiable over the interval (a, b).
- There exists a point c in (a, b) such that f'(c) = [f(b) — f(a)] / (b — a)

---

### 2. State and prove mean value theorem. **[7]**

**Statement:** The mean value theorem states that if a function f is continuous over the closed interval [a, b], and differentiable over the open interval (a, b), then there exists at least one point c in the interval (a, b) such that f '(c) is the average rate of change of the function over [a, b] and it is parallel to the secant line over [a, b].

**Proof:** Let g(x) be the secant line to f(x) passing through (a, f(a)) and (b, f(b)). We know that the equation of the secant line is y — y₁ = m (x — x₁).

g(x) — f(a) = [f(b) — f(a)] / (b — a) (x — a)

g(x) = [f(b) — f(a)] / (b — a) (x — a) + f(a) ----->(1)

Let h(x) be f(x) — g(x)

h(x) = f(x) — [ [f(b) — f(a)] / (b — a) (x — a) + f(a) ] (From (1))

h(a) = h(b) = 0 and h(x) is continuous on [a, b] and differentiable on (a, b).

Thus applying the Rolles theorem, there is some x = c in (a, b) such that h'(c) = 0.

h'(x) = f'(x) — [f(b) — f(a)] / (b — a)

For some c in (a, b), h'(c) = 0. Thus

h'(c) = f'(c) — [f(b) — f(a)] / (b — a) = 0

f'(c) = [f(b) — f(a)] / (b — a)

Thus the mean value theorem is proved.

Note: The result may not hold if the function is not differentiable, even at a single point in the open interval.

---

### 3. Illustrate mean value theorem graphically. **[5]**

The graphical representation of the function f(x) helps in understanding the mean value theorem. Here we consider two distinct points (a, f(a)), (b, f(b)). The line connecting these points is the secant of the curve, which is parallel to the tangent cutting the curve at (c, f(c)). The slope of the secant of the curve joining these points is equal to the slope of the tangent at the point (c, f(c)). We know that the derivative of the tangent is the slope at that point.

Slope of the Tangent = Slope of the Secant

f'(c) = [f(b) — f(a)] / (b — a)

Graph of Mean Value Theorem:

```
Y
|
|          (b,f(b))
|         /
|        /
| (a,f(a))
|       c
|___________________
x'← 0 a c b → x
Y'
```

Here we observe that the point (c, f(c)), lies between the two points (a, f(a)), (b, f(b)).

Geometrically the mean value theorem says that somewhere between A and B, the graph has a tangent parallel to the chord(secant) AB.

---

### 4. Verify the function f(x) = x² + 1 satisfies the mean value theorem in the interval [1,4]. If so, find the value of 'c'. **[5]**

The given function is f(x) = x² + 1. To verify the mean value theorem, the function f(x) = x² + 1 must be continuous in [1, 4] and differentiable in (1, 4).

Since f(x) is a polynomial function, both of the above conditions hold true.

The derivative f'(x) = 2x (power rule) is defined in the interval (1, 4)

f(1) = 1² + 1 = 1 + 1 = 2

f(4) = 4² + 1 = 16 + 1 = 17

f'(c) = [f(4) — f(1)] / (4 — 1)

= (17 — 2) / (4 — 1) = 15/3 = 5

f'(c) = 5

2c = 5

c = 2.5 which lies in the interval (1, 4)

Answer: The given function satisfies the mean value theorem and c = 2.5.

---

### 5. State and prove Rolle's theorem. **[7]**

**Statement:** Rolle's theorem states that "If a function f is defined in the closed interval [a, b] in such a way that it satisfies the following condition: i) f is continuous on [a, b], ii) f is differentiable on (a, b), and iii) f(a) = f(b), then there exists at least one value of x, let us assume this value to be c, which lies between a and b i.e. (a < c < b) in such a way that f'(c) = 0."

**Proof:** When proving a theorem directly, you start by assuming all of the conditions are satisfied. So, our discussion below relates only to functions

- that is continuous over [a, b],
- that is differentiable (a, b),
- and have f(a) = f(b).

With that in mind, notice that when a function satisfies Rolle's Theorem, the place where f'(x)=0 occurs at a maximum or a minimum value (i_e., extrema).

How do we know that a function will even have one of these extrema? the Extreme Value Theorem theorem says that if a function is continuous, then it is guaranteed to have both a maximum and a minimum point in the interval.

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

### 6. Show that Rolle's theorem is a special case of the mean value theorem. **[2]**

Rolle's Theorem is a special case of the mean value theorem.

Also note that if it weren't for the fact that we needed Rolle's Theorem to prove this we could think of Rolle's Theorem as a special case of the Mean Value Theorem. To see that just assume that f(a) = f(b) and then the result of the Mean Value Theorem gives the result of Rolle's Theorem.

---

### 7. Distinguish the mean value theorem from Rolle's theorem including graphical representation. **[5]**

Both the mean value theorem and Rolle's theorem define the function f(x) such that it is continuous across the interval [a, b], and it is differentiable across the interval (a, b). In the mean value theorem, the two referred points (a, f(a)), (b, f(b)) are distinct and f(a) ≠ f(b). In Rolle's theorem, the points are defined such that f(a) = f(b).

The value of c in the mean value theorem is defined such that the slope of the tangent at the point (c, f(c)) is equal to the slope of the secant joining the two points. The value of c in Rolle's theorem is defined such that the slope of the tangent at the point (c, f(c)) is equal to the slope of the x-axis. The slope in the mean value theorem is f'(c) = [f(b) — f(a)] / (b — a), and the slope in Rolle's theorem is equal to f'(c) = 0.

Mean Value Theorem:

```
Y
|
|        /
|       /  (b,f(b))
|      /
|     / (a,f(a))
|    /
|   c
|___________________
x'← 0 a c b → x
Y'
```

Rolle's Theorem:

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

---

### 8. Verify the Rolle's theorem for the function f(x) = x² + 2 in the interval [-2,2]. **[5]**

Verify Rolle's theorem for the functions y = x² + 2, a = -2, and b = 2

The function y = x² + 2 is continuous in [-2, 2] and differentiable in (-2, 2), according to Rolle's theorem formulation.

Given the circumstances,

f(x) = x² + 2

f(-2) = (-2)² + 2 = 4 + 2 = 6

f(2) = (2)² + 2 = 4 + 2 = 6

Thus, f(-2) = f(2) = 6

As a result, the function f(x) is continuous in the range [-2, 2].

Now, f'(x) = 2x

According to Rolle's theorem, there is a point c ∈ (-2, 2) where f'(c) = 0.

f'(c) = 2(c) = 0 at c = 0, when c = 0 ∈ (-2, 2)

As a result, Rolle's theorem is proven.
