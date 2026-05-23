## Image 1

# Recurrence Relation and Generating Functions

There are some basic techniques of counting, such as permutation, combination, etc. Many counting problems can not be solved by using the basic techniques of counting. Such problems can be solved by recurrence relation and generating function.

---

### 📌 Definition of Recurrence Relation

A **recurrence relation** for the sequence ${a_n}$ is an equation that expresses $a_n$ in terms of one or more of the previous terms of the sequence, namely $a_0, a_1, a_2, \ldots, a_n$ for all integer $n$ with $n \geq n_0$, where $n_0$ is a non-negative integer.

**Example:**

$$a_n = a_{n-1} - a_{n-2}$$

> The order of this equation is $n - (n-2) = 2$

---

### 📌 Solving Recurrence Relations

- Basically, when solving such recurrence relations, we try to find solutions of the form $a_n = r^n$, where $r$ is a condition constant.

---

## Image 2

- $a_n = r^n$ is a solution of the recurrence relation.

$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k}$$

if and only if

$$r^n = c_1 r^{n-1} + c_2 r^{n-2} + \cdots + c_k r^{n-k}$$

- Divide this equation by $r^{n-k}$ and subtract the right-hand side from the left:

$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \cdots - c_{k-1} r - c_k = 0$$

This is called the **characteristic equation** of the recurrence relation.

- The solutions of this equation are called the **characteristic roots** of the recurrence relation.
    
- Let us consider **linear homogeneous recurrence relations of degree two**.
    

---

### Theorem

Let $c_1$ and $c_2$ be real numbers. Suppose that $r^2 - c_1 r - c_2 = 0$ has two distinct roots $r_1$ and $r_2$.

Then the sequence ${a_n}$ is a solution of the recurrence relation $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ if and only if

$$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n \quad \text{for } n = 0, 1, 2, \ldots$$

where $\alpha_1$ and $\alpha_2$ are constants.

---

## Image 3

### 📌 Solution of a Recurrence Relation

A sequence is called a **solution** of a recurrence relation if it satisfies the recurrence relation.

**Example:** The sequence ${a_n}$ with $a_n = 3n$ is a solution of the recurrence relation:

$$a_n = 2a_{n-1} - a_{n-2}, \quad \forall\ n \geq 2 \tag{1}$$

**Solution:** The given recurrence relation is:

$$a_n = 2a_{n-1} - a_{n-2}$$

We know $a_n = 3n$, so:

$$a_0 = 3 \cdot 0 = 0, \quad a_{n-1} = 3(n-1), \quad a_{n-2} = 3(n-2)$$

The right-hand side of equation (1):

$$\text{R.H.S.} = 2a_{n-1} - a_{n-2}$$ $$= 2 \cdot 3(n-1) - 3(n-2)$$ $$= 6n - 6 - 3n + 6$$ $$= 3n$$ $$= a_n$$ $$= \text{L.H.S.}$$

$\therefore$ $a_n = 3n$ is the solution of the recurrence relation $a_n = 2a_{n-1} - a_{n-2}$.

---

## Image 4

### 📌 Problem

Someone deposits $10{,}000$ Tk in a savings account at a Bank yielding $5%$ per year with interest compounded annually. How much money will be in the account after $30$ years?

**Solution:** Let $P_n$ be the amount in account after $n$ years. We can derive the following recurrence relation:

$$P_n = P_{n-1} + 0.05, P_{n-1}$$

$$\Rightarrow P_n = P_{n-1}(1 + 0.05)$$

$$\Rightarrow P_n = (1.05), P_{n-1} \tag{1}$$

Now, initial deposit $P_0 = 10{,}000$ Tk.

$$P_1 = (1.05), P_0 = (1.05) \times 10{,}000$$

$$P_2 = (1.05), P_1 = (1.05)(1.05) \times 10{,}000 = (1.05)^2 \times 10{,}000$$

$$\therefore P_{30} = (1.05)^{30} \times 10{,}000 \text{ Tk}$$

---

## Image 5

### 📌 Linear Homogeneous Recurrence Relations

**Problem:** What is the solution of the recurrence relation

$$a_n = a_{n-1} + 2a_{n-2}$$

with $a_0 = 2$ and $a_1 = 7$?

**Solution:** Given that,

$$a_n = a_{n-1} + 2a_{n-2} \tag{1}$$

Let $a_n = r^n$ be a solution of equation (1).

$$\therefore r^n = r^{n-1} + 2r^{n-2}$$

Dividing both sides by $r^{n-2}$:

$$\frac{r^n}{r^{n-2}} = \frac{r^{n-1}}{r^{n-2}} + 2\frac{r^{n-2}}{r^{n-2}}$$

$$\Rightarrow r^2 = r + 2$$

$$\Rightarrow r^2 - r - 2 = 0$$

$$\Rightarrow r^2 - 2r + r - 2 = 0$$

$$\Rightarrow r(r-2) + (r-2) = 0$$

$$\Rightarrow (r+1)(r-2) = 0$$

$$\therefore r = 2,\ -1$$

$\therefore$ Roots are real and distinct.

$\therefore$ The general solution is:

$$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n = \alpha_1 \cdot 2^n + \alpha_2 \cdot (-1)^n \tag{2}$$

---

## Image 6

When $n = 0$:

$$a_0 = \alpha_1 \cdot 2^0 + \alpha_2 \cdot (-1)^0$$

$$\Rightarrow 2 = \alpha_1 + \alpha_2 \qquad [\because a_0 = 2]$$

$$\therefore \alpha_1 + \alpha_2 - 2 = 0 \tag{3}$$

When $n = 1$:

$$a_1 = \alpha_1 \cdot 2^1 + \alpha_2 \cdot (-1)^1$$

$$\Rightarrow 7 = 2\alpha_1 - \alpha_2 \tag{4}$$

$$\Rightarrow 2\alpha_1 - \alpha_2 - 7 = 0$$

Now solving (3) and (4):

$$\frac{\alpha_1}{-7-2} = \frac{\alpha_2}{-4+7} = \frac{1}{-1-2}$$

$$\Rightarrow \alpha_1 = \frac{-9}{-3},\quad \alpha_2 = \frac{3}{-3}$$

$$\therefore \alpha_1 = 3,\quad \alpha_2 = -1$$

Putting the values of $\alpha_1$ and $\alpha_2$ in equation (2):

$$\boxed{a_n = 3 \cdot 2^n - (-1)^n}$$

which is the solution of the given recurrence relation.

---

**Problem:** What is the solution of the recurrence relation

$$a_n = -6a_{n-1} - 9a_{n-2},\quad n \geq r$$

with $a_0 = -6$ and $a_1 = 3$?

**Solution:** Given that,

$$a_n = -6a_{n-1} - 9a_{n-2} \tag{1}$$

Let $a_n = r^n$ be a solution of equation (1).

$$\therefore r^n = -6r^{n-1} - 9r^{n-2}$$

---

## Image 7

Dividing both sides by $r^{n-2}$, we get:

$$r^2 = -6r - 9$$

$$\Rightarrow r^2 + 6r + 9 = 0$$

$$\Rightarrow (r+3)^2 = 0$$

$$\Rightarrow (r+3)(r+3) = 0$$

$$\therefore r = -3,\ -3$$

$\therefore$ The roots are real and **equal**.

$\therefore$ The general solution is:

$$a_n = \alpha_1 r_1^n + n\alpha_2 r_2^n \tag{2}$$

When $n = 0$:

$$a_0 = \alpha_1 + 0$$

$$\Rightarrow -6 = \alpha_1 + 0$$

$$\Rightarrow \alpha_1 + 6 = 0 \tag{3}$$

$$\therefore \alpha_1 = -6$$

When $n = 1$:

$$a_1 = \alpha_1 r_1 + \alpha_2 r_2$$

$$\Rightarrow 3 = (-6)(-3) + \alpha_2(-3)$$

$$\Rightarrow 3 = 18 - 3\alpha_2$$

$$\Rightarrow 3\alpha_2 = 15$$

$$\therefore \alpha_2 = 5$$

Putting the values of $\alpha_1$ and $\alpha_2$ in equation (2):

$$a_n = -6r_1^n + 5n, r_2^n$$

$$= -6(-3)^n + 5n(-3)^n$$

which is the solution of the given recurrence relation.

---

## Image 8

> **V.I.P** — Exam 18 ✓ _(2020)_

**Problem:** What is the solution of the recurrence relation

$$a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3}$$

where $a_0 = 2,\ a_1 = 5,\ a_2 = 15$?

**Solution:** Given that,

$$a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3} \tag{1}$$

Let $a_n = r^n$ be a solution of equation (1).

$$\therefore r^n = 6r^{n-1} - 11r^{n-2} + 6r^{n-3}$$

Dividing both sides by $r^{n-3}$, we get:

$$r^3 = 6r^2 - 11r + 6$$

$$\Rightarrow r^3 - 6r^2 + 11r - 6 = 0$$

$$\Rightarrow r^3 - r^2 - 5r^2 + 5r + 6r - 6 = 0$$

$$\Rightarrow r^2(r-1) - 5r(r-1) + 6(r-1) = 0$$

$$\Rightarrow (r-1)(r^2 - 5r + 6) = 0$$

$$\Rightarrow (r-1)(r^2 - 3r - 2r + 6) = 0$$

$$\Rightarrow (r-1){r(r-3) - 2(r-3)} = 0$$

$$\Rightarrow (r-1)(r-2)(r-3) = 0$$

$$\therefore r = 1,\ 2,\ 3$$

Here, the roots are real and distinct.

---

## Image 9

The general solution is:

$$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + \alpha_3 r_3^n \tag{2}$$

When $n = 0$:

$$a_0 = \alpha_1 + \alpha_2 + \alpha_3 \qquad [\because a_0 = 2]$$

$$\Rightarrow 2 = \alpha_1 + \alpha_2 + \alpha_3$$

$$\Rightarrow \alpha_1 + \alpha_2 + \alpha_3 - 2 = 0 \tag{3}$$

When $n = 1$:

$$a_1 = \alpha_1 r_1 + \alpha_2 r_2 + \alpha_3 r_3 \qquad [\because a_1 = 5]$$

$$\Rightarrow 5 = \alpha_1 r_1 + \alpha_2 r_2 + \alpha_3 r_3$$

$$\Rightarrow \alpha_1 r_1 + \alpha_2 r_2 + \alpha_3 r_3 - 5 = 0 \tag{4}$$

$$\Rightarrow \alpha_1 + 2\alpha_2 + 3\alpha_3 - 5 = 0 \tag{4}$$

When $n = 2$:

$$a_2 = \alpha_1 r_1^2 + \alpha_2 r_2^2 + \alpha_3 r_3^2 \qquad [\because a_2 = 15]$$

$$\Rightarrow 15 = \alpha_1 r_1^2 + \alpha_2 r_2^2 + \alpha_3 r_3^2$$

$$\Rightarrow \alpha_1 r_1^2 + \alpha_2 r_2^2 + \alpha_3 r_3^2 - 15 = 0 \tag{5}$$

$$\Rightarrow \alpha_1 + 4\alpha_2 + 9\alpha_3 - 15 = 0 \tag{5}$$

$(4) - (3)$: $\quad \alpha_2 + 2\alpha_3 - 3 = 0 \tag{6}$

$(5) - (3)$: $\quad 3\alpha_2 + 8\alpha_3 - 13 = 0 \tag{7}$

Solving (6) and (7), we get:

$$\frac{\alpha_2}{-26+24} = \frac{\alpha_3}{-9+13} = \frac{1}{8-6}$$

---

## Image 10

$$\Rightarrow \frac{\alpha_2}{-2} = \frac{\alpha_3}{4} = \frac{1}{2}$$

$$\therefore \alpha_2 = -1,\quad \alpha_3 = 2$$

From (3): $\quad \alpha_1 - 1 + 2 - 2 = 0$

$$\therefore \alpha_1 = 1$$

$$\therefore \alpha_1 = 1,\quad \alpha_2 = -1,\quad \alpha_3 = 2$$

$\therefore$ The general solution is:

$$a_n = 1\cdot(1)^n + (-1)(2)^n + (2)(3)^n$$

$$\boxed{\therefore a_n = 1 - 2^n + 2 \cdot 3^n}$$

which is the required solution of the given recurrence relation.

---

## Image 11

> **TU · V.V.I.P · 100%** — Exam 18 _(2020)_

**Problem:** Find the solution of the recurrence relation

$$f_n = f_{n-1} + f_{n-2},\quad f_0 = 0,\ f_1 = 1$$

Find the explicit formula for the Fibonacci sequence/number.

**Solution:** Given that,

$$f_n = f_{n-1} + f_{n-2} \tag{1}$$

Let $f_n = r^n$ be a solution of equation (1).

Now, $r^n = r^{n-1} + r^{n-2}$

Dividing both sides by $r^{n-2}$:

$$r^2 = r + 1$$

$$\Rightarrow r^2 - r - 1 = 0$$

$$\Rightarrow r = \frac{1 \pm \sqrt{1+4}}{2} \qquad \left[\because x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\right]$$

$$\therefore r = \frac{1+\sqrt{5}}{2},\quad \frac{1-\sqrt{5}}{2}$$

$\therefore$ The roots are real and distinct.

$\therefore$ The general solution is:

$$f_n = \alpha_1 r_1^n + \alpha_2 r_2^n \tag{2}$$

When $n = 0$:

$$f_0 = \alpha_1 + \alpha_2 \qquad [\because f_0 = 0]$$

$$\Rightarrow 0 = \alpha_1 + \alpha_2$$

$$\therefore \alpha_1 + \alpha_2 = 0 \tag{3}$$

$$\therefore \alpha_1 = -\alpha_2$$

When $n = 1$:

$$f_1 = \alpha_1 r_1 + \alpha_2 r_2 \qquad [\because f_1 = 1]$$

$$\Rightarrow 1 = \alpha_1 r_1 + \alpha_2 r_2$$

---

## Image 12

$$\Rightarrow \alpha_1 r_1 + \alpha_2 r_2 - 1 = 0 \tag{4}$$

Solving (3) and (4):

From (4): $\quad -\alpha_2 r_1 + \alpha_2 r_2 - 1 = 0$

$$\Rightarrow \alpha_2(r_2 - r_1) - 1 = 0$$

$$\Rightarrow \alpha_2 = \frac{1}{r_2 - r_1}$$

$$= \frac{1}{\dfrac{1-\sqrt{5}}{2} - \dfrac{1+\sqrt{5}}{2}}$$

$$= \frac{1}{\dfrac{1-\sqrt{5}-1-\sqrt{5}}{2}} = \frac{2}{-2\sqrt{5}} = -\frac{1}{\sqrt{5}}$$

$$\therefore \alpha_2 = -\frac{1}{\sqrt{5}} \quad \text{and} \quad \alpha_1 = \frac{1}{\sqrt{5}}$$

From (2):

$$f_n = \frac{1}{\sqrt{5}}, r_1^n - \frac{1}{\sqrt{5}}, r_2^n$$

$$\therefore f_n = \frac{1}{\sqrt{5}}\left(r_1^n - r_2^n\right) \quad \text{(solution of the given recurrence relation)}$$

$$= \frac{1}{\sqrt{5}}\left{\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right}$$
$$\boxed{\therefore f_n = \frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^n - \frac{1}{\sqrt{5}}\left(\frac{1-\sqrt{5}}{2}\right)^n}$$

which is the required formula. $\blacksquare$