# STAT-2101: Probability Theory
# Chapter 5 — Convergence
## Exam Question Bank

---

## SECTION 5.1 — CONVERGENCE IN DISTRIBUTION

### A. Definitions

**Question 1:** Give the formal definition of convergence in distribution (also called convergence weakly or convergence in law) for a sequence of real-valued random variables $\{X_n\}$.

**Answer:**

A sequence of real valued random variables $\{X_n\}$, $n = 1, 2, \cdots$ is said to **converge in distribution**, or **converge weakly**, or **converge in law** to a random variable $X$ if it follows as

$$\lim_{n \to \infty} F_n(x) = F(x),$$

for every number $x \in \mathbb{R}$ at which $F$ is continuous. Here $F_n$ and $F$ are the cumulative distribution functions of random variables $X_n$ and $X$, respectively.

---

**Question 3:** What notation is used to denote convergence in distribution?

**Answer:**

Convergence in distribution may be denoted as

$$X_n \xrightarrow{L} X \quad \text{or} \quad X_n \xrightarrow{d} X.$$

---

### B. Properties

**Question 4:** If $X_n \xrightarrow{L} X$ and $c$ is a constant, what can be said about $X_n + c$ and $cX_n$?

**Answer:**

1. Let $X_n \xrightarrow{L} X$ and $c$ is a constant, then
   (i) $X_n + c \xrightarrow{L} X + c$, and
   (ii) $cX_n \xrightarrow{L} cX$.

---

**Question 5:** If $X_n \xrightarrow{L} X$ and $Y_n \xrightarrow{L} c$, what can be said about $X_n + Y_n$, $X_nY_n$, and $\dfrac{X_n}{Y_n}$?

**Answer:**

2. $X_n \xrightarrow{L} X$ and $Y_n \xrightarrow{L} c$, then

   (i) $X_n + Y_n \xrightarrow{L} X + c$,

   (ii) $X_n Y_n \xrightarrow{L} cX$, and

   (iii) $\dfrac{X_n}{Y_n} \xrightarrow{L} \dfrac{X}{c}$ $(c \neq 0)$.

---

### C. Examples

**Question 6 (Example 1):** A sequence of binomial variates $\{X_n\}$ has distribution $Pr[X_n=r] = \binom{n}{r}P_n^{\,r}(1-P_n)^{n-r}$, with $E[X_n] = nP_n = \lambda$ held fixed. Find the limiting distribution of $Pr[X_n = r]$ as $n \to \infty$.

**Answer:**

Let $\{X_n\}$ be a sequence of binomial variates having distribution

$$Pr[X_n = r] = \binom{n}{r} P_n^{\ r} (1 - P_n)^{n-r}.$$

Let $E[X_n] = nP_n = \lambda$ be a finite constant, then

$$Pr[X_n = r] \to \frac{e^{-\lambda} \lambda^r}{r!} \quad \text{as } n \to \infty.$$

---

**Question 7 (Example 2):** A sequence of $t$-distributed variates $\{X_n\}$ has density $f(X_n=t) = \frac{1}{\sqrt{n}\,B(1/2,\,n/2)}\cdot\frac{1}{(1+t^2/n)^{(n+1)/2}}$. Find the limiting form of this density as $n \to \infty$.

**Answer:**

Let $\{X_n\}$ be a sequence of $t$ variates having distribution

$$f(X_n = t) = \frac{1}{\sqrt{n}\, B\left(\frac{1}{2}, \frac{n}{2}\right)} \cdot \frac{1}{\left(1 + \frac{t^2}{n}\right)^{\frac{n+1}{2}}}.$$

then it follows that

$$f(X_n = t) = \frac{1}{\sqrt{2\pi}} \cdot e^{-\frac{1}{2}t^2} \quad \text{as } n \to \infty.$$

---

## SECTION 5.2 — CONVERGENCE IN PROBABILITY

### A. Definitions

**Question 1:** Describe the intuitive idea behind convergence in probability, and explain how it relates to the definition of a consistent estimator.

**Answer:**

The basic idea behind this type of convergence is that the probability of an "unusual" outcome becomes smaller and smaller as the sequence progresses. The concept of convergence in probability is used very often in statistics. *For example*, an estimator is called consistent if it converges in probability to the quantity being estimated. Convergence in probability is also the type of convergence established by the weak law of large numbers.

---

**Question 2:** Give the formal definition of convergence in probability for a sequence of random variables $\{X_n\}$ toward a random variable $X$.

**Answer:**

A sequence of random variables $\{X_n\}$, $n = 1, 2, \cdots$ is said to **converge in probability** towards the random variable $X$ if for all $\epsilon > 0$

$$\lim_{n \to \infty} Pr\left(|X_n - X| > \epsilon\right) = 0.$$

---

**Question 3:** What notation is used to denote convergence in probability?

**Answer:**

Convergence in probability is denoted by adding the letter $p$ over an arrow indicating convergence, or using the "plim" probability limit operator:

$$X_n \xrightarrow{p} X \quad \text{or} \quad X_n \xrightarrow{P} X \quad \text{or} \quad \operatorname{plim}_{n \to \infty} X_n = X.$$

---

### B. Properties

**Question 4:** List properties 1 through 9 of convergence in probability given in the text.

**Answer:**

1. $X_n \xrightarrow{P} X \implies X_n - X \xrightarrow{P} 0$.

2. $X_n \xrightarrow{P} X$, $X_n \xrightarrow{P} Y \implies Pr[X = Y] = 1$.

3. $X_n \xrightarrow{P} X$, $Y_n \xrightarrow{P} Y$, then

   (i) $X_n \pm Y_n \xrightarrow{P} X \pm Y$

   (ii) $X_n Y_n \xrightarrow{P} XY$

   (iii) $\dfrac{X_n}{Y_n} \xrightarrow{P} \dfrac{X}{Y}$

4. $X_n \xrightarrow{P} X$, and $k$ is a constant $\implies kX_n \xrightarrow{P} kX$.

5. $X_n \xrightarrow{P} k \implies X_n^2 \xrightarrow{P} k^2$.

6. $X_n \xrightarrow{P} a$, $Y_n \xrightarrow{P} b \implies X_n Y_n \xrightarrow{P} ab$, where $a, b$ are constants.

7. $X_n \xrightarrow{P} X$ and $Y$ is a random variable $\implies X_n Y \xrightarrow{P} XY$.

8. $X_n \xrightarrow{P} 1 \implies X_n^{-1} \xrightarrow{P} 1$.

9. Convergence in probability implies convergence in distribution: $X_n \xrightarrow{P} X \implies X_n \xrightarrow{d} X$.

All the above statement can be easily verified.

---

### C. Examples

**Question 5 (Example 1):** Let $X_1, X_2, \cdots$ be a sequence of independent and identically distributed random variables with $\mu = E(X_i)$ and $\sigma^2 = Var(X_i) < \infty$ for $i = 1, 2, \cdots, \infty$. Show that the sample mean $\bar{X}_n$ converges in probability to $\mu$.

**Answer:**

Let $X_1, X_2, \cdots$ be a sequence of independent and identically distributed random variables with $\mu = E(X_i)$ and $\sigma^2 = Var(X_i) < \infty$ for $i = 1, 2, \cdots, \infty$. Then sample mean $\bar{X}_n$ converges in probability to $\mu$.

*Solution:* We have the following

$$E\left(\bar{X}_n\right) = \mu \quad \text{and} \quad Var\left(\bar{X}_n\right) = \frac{\sigma^2}{n}.$$

By Chebyshev's inequality

$$Pr\left(\left|\bar{X}_n - E\left(\bar{X}_n\right)\right| \geq \epsilon\right) \leq \frac{Var\left(\bar{X}_n\right)}{\epsilon^2},$$

for $\epsilon > 0$. Hence

$$Pr\left(\left|\bar{X}_n - \mu\right| \geq \epsilon\right) \leq \frac{\sigma^2}{n\epsilon^2}.$$

Taking the limit as $n$ tends to infinity, we get

$$\lim_{n \to \infty} Pr\left(\left|\bar{X}_n - \mu\right| \geq \epsilon\right) \leq \lim_{n \to \infty} \frac{\sigma^2}{n\epsilon^2},$$

which yields

$$\lim_{n \to \infty} Pr\left(\left|\bar{X}_n - \mu\right| \geq \epsilon\right) = 0.$$

So the sample mean $\bar{X}_n$ converges in probability to $\mu$, also written as $\bar{X}_n \xrightarrow{P} \mu$.

---

**Question 6 (Example 2):** Let $X_n \sim Exponential(n)$. Show that $X_n \xrightarrow{P} 0$; that is, the sequence $X_1, X_2, \cdots$ converges in probability to the zero random variable $X$.

**Answer:**

Let $X_n \sim Exponential(n)$, show that $X_n \xrightarrow{P} 0$. That is, the sequence $X_1, X_2, \cdots$ converges in probability to the zero random variable $X$.

*Solution:* We have

$$\begin{aligned}
\lim_{n \to \infty} Pr\left(|X_n - 0| \geq \epsilon\right) &= \lim_{n \to \infty} Pr\left(X_n \geq \epsilon\right) \\
&= \lim_{n \to \infty} \left[1 - Pr\left(X_n \leq \epsilon\right)\right] \\
&= \lim_{n \to \infty} \left[1 - \left(1 - e^{-n\epsilon}\right)\right] \\
&= \lim_{n \to \infty} e^{-n\epsilon} \\
&= 0, \quad \text{for all } \epsilon > 0.
\end{aligned}$$

Hence the sequence of random variables $X_1, X_2, \cdots$ convergence in probability to the zero random variable $X$.

---

**Question 7 (Example 3):** State and prove the convergence in probability result for $X \sim Binomial(n, p)$.

**Answer:**

If $X \sim Binomial(n, p)$, then $X_n \xrightarrow{P} p$.

*Solution:* Assignment

---

### D. Theorems

**Question 8:** State Theorem 5.2.1 and give its proof.

**Answer:**

**Theorem 5.2.1.** *Convergence in probability implies convergence in distribution. That can be also written as*

$$X_n \xrightarrow{P} X \implies X_n \xrightarrow{d} X.$$

*Proof.* In order to prove convergence in distribution, one must show that the sequence of cumulative distribution functions converges to the $F_X$ at every point where $F_X$ is continuous. Let $a$ be such a point. For every $\epsilon > 0$, we have

$$Pr(X_n \leq a) \leq Pr(X \leq a + \varepsilon) + Pr(|X_n - X| > \varepsilon)$$

$$Pr(X \leq a - \varepsilon) \leq Pr(X_n \leq a) + Pr(|X_n - X| > \varepsilon)$$

So, we have

$$Pr(X \leq a - \varepsilon) - Pr(|X_n - X| > \varepsilon) \leq Pr(X_n \leq a)$$

$$\leq Pr(X \leq a + \varepsilon) + Pr(|X_n - X| > \varepsilon).$$

Taking the limit as $n \to \infty$, we obtain:

$$F_X(a - \varepsilon) \leq \lim_{n \to \infty} Pr(X_n \leq a) \leq F_X(a + \varepsilon),$$

where $F_X = Pr(X \leq a)$ is the cumulative distribution function of $X$. This function is continuous at $a$ by assumption, and therefore both $F_X(a - \epsilon)$ and $F_X(a + \epsilon)$ converge to $F_X(a)$ as $\epsilon \to 0^+$. Taking this limit, we obtain

$$\lim_{n \to \infty} Pr(X_n \leq a) = Pr(X \leq a),$$

which means that $\{X_n\}$ converges to $X$ in distribution. $\blacksquare$

---

## SECTION 5.3 — ALMOST SURE CONVERGENCE

### A. Definitions

**Question 1:** Almost sure convergence is described as the type of stochastic convergence most similar to a familiar concept from elementary real analysis. Name that concept.

**Answer:**

This is the type of stochastic convergence that is most similar to pointwise convergence known from elementary real analysis.

---

**Question 2:** Give the formal definition of almost sure convergence, including the equivalent formulation in terms of a supremum.

**Answer:**

A sequence of random variables $\{X_n\}$, $n = 1, 2, \cdots$ is said to converge **almost surely (a.s)** or **almost everywhere** or **with probability 1** or **strongly** to another random variable $X$ if and only if

$$Pr\left[\lim_{n \to \infty} X_n = X\right] = 1,$$

or, equivalently,

$$\lim_{N \to \infty} Pr\left[\sup_{n \geq N} |X_n - X| > \epsilon\right] = 0 \quad \text{for every } \epsilon.$$

---

**Question 3:** What notation is used to denote almost sure convergence?

**Answer:**

Almost sure convergence is often denoted by adding the letters a.s. over an arrow indicating convergence: $X_n \xrightarrow{a.s.} X$ or $X_n \to X$ with probability 1.

---

### B. Properties

**Question 4:** List properties 1 through 5 of almost sure convergence given in the text.

**Answer:**

Some of the properties of almost surely are as follow:

1. If $X_n \xrightarrow{a.s.} X$ and $X_n \xrightarrow{a.s.} Y$, then $X = Y$ almost surely.

2. If $X_n \xrightarrow{a.s.} X$ and $Y_n \xrightarrow{a.s.} Y$, then $aX_n + bY_n \xrightarrow{a.s.} aX + bY$, $\forall\ a, b \in \mathbb{R}$.

3. If $X_n \xrightarrow{a.s.} X$ and $Y_n \xrightarrow{a.s.} Y$, then $X_n Y_n \xrightarrow{a.s.} XY$.

4. Almost sure convergence implies convergence in probability, and hence implies convergence in distribution: $X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{P} X \implies X_n \xrightarrow{d} X$.

5. Convergence in probability implies there exists a sub-sequence $(k_n)$ which almost surely converges: $X_n \xrightarrow{P} X \implies X_{k_n} \xrightarrow{a.s.} X$.

---

### C. Examples

**Question 5 (Example 1):** Using the example of a short-lived animal's daily food consumption, explain what we can be certain of about this sequence in terms of almost sure convergence.

**Answer:**

Consider an animal of some short-lived species. We record the amount of food that this animal consumes per day. This sequence of numbers will be unpredictable, but we may be quite certain that one day the number will become zero, and will stay zero forever after.

---

**Question 6 (Example 2):** A man tosses seven coins each morning and donates one pound per head to charity each afternoon, stopping permanently the first time all tosses come up tails. Let $X_1, X_2, \cdots$ be the daily donation amounts. What can we be almost sure of about this sequence?

**Answer:**

Consider a man who tosses seven coins every morning. Each afternoon, he donates one pound to a charity for each head that appeared. The first time the result is all tails, however, he will stop permanently.

Let $X_1, X_2, \cdots$ be the daily amounts the charity received from him. We may be almost sure that one day this amount will be zero, and stay zero forever after that.

---

### D. Theorems

**Question 7:** State Theorem 5.3.1 and give its proof.

**Answer:**

**Theorem 5.3.1.** *Convergence almost surely implies convergence in probability. That can be also written as*

$$X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{P} X.$$

*Proof.* We have

$$|X_n - X| > \epsilon \implies \sup_{n \geq N} |X_n - X| > \epsilon.$$

So that

$$Pr\left[|X_n - X| > \epsilon\right] \leq Pr\left[\sup_{n \geq N} |X_n - X| > \epsilon\right].$$

According to the law of large numbers

$$Pr\left[\sup_{n \geq N} |X_n - X| > \epsilon\right] = 0 \quad \text{as } n \to \infty.$$

Therefore,

$$Pr\left[|X_n - X| > \epsilon\right] \to 0 \quad \text{as } n \to \infty.$$

Hence, $X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{P} X$. $\blacksquare$

---

## SECTION 5.4 — LAWS OF LARGE NUMBERS

### A. Definitions / General Concepts

**Question 1:** Define the law of large numbers (LLN) and state what it says about the average of a large number of trials.

**Answer:**

The law of large numbers (LLN) is a theorem that describes the result of performing the same experiment a large number of times. According to the law, the average of the results obtained from a large number of trials should be close to the expected value, and will tend to become closer as more trials are performed.

---

**Question 2:** Why is the LLN considered important?

**Answer:**

The $LLN$ is important because it guarantees stable long-term results for the averages of some random events.

---

**Question 3:** In the classic dice-rolling illustration of the LLN, what value does the running average approach as the number of rolls increases?

**Answer:**

An illustration of the law of large numbers using a particular run of rolls of a single dice. As the number of rolls in this run increases, the average of the values of all the results approaches 3.5. While different runs would show a different shape over a small number of throws (at the left), over a large number of rolls (to the right) they would be extremely similar.

---

**Question 4:** Name the two versions of the law of large numbers described in the text.

**Answer:**

Two different versions of the law of large numbers are described below; they are called the **strong law of large numbers**, and the **weak law of large numbers**.

---

**Question 5:** State Chebyshev's inequality for a random variable $X$ with mean $\mu$ and standard deviation $\sigma$.

**Answer:**

**Chebyshev's Inequality:** Let $X$ be a random variable with mean $\mu$ and standard deviation $\sigma$. Then Chebyshev's inequality states that

$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2} \qquad Or, \quad P(|X - \mu| < k\sigma) \geq 1 - \frac{1}{k^2},$$

for any nonzero positive constant $k$.

---

### B. Weak Law of Large Numbers (5.4.1)

**Question 6:** State the weak law of large numbers (WLLN), including its formulation as a limiting probability statement.

**Answer:**

The weak law of large numbers (WLLN) states that the sample average converges in probability towards the expected value

$$\overline{X}_n \xrightarrow{P} \mu, \qquad \text{when } n \to \infty.$$

That is, for any positive number $\epsilon$,

$$\lim_{n \to \infty} Pr\left(\ |\overline{X}_n - \mu| > \varepsilon\ \right) = 0.$$

---

**Question 7:** Give the interpretation of the WLLN in terms of margins and sample size.

**Answer:**

Interpreting this result, the weak law states that for any nonzero margin specified, no matter how small, with a sufficiently large sample there will be a very high probability that the average of the observations will be close to the expected value; that is, within the margin.

---

**Question 8:** State the necessary and sufficient conditions for the existence of the WLLN, and indicate which condition is necessary and which is sufficient.

**Answer:**

Necessary and sufficient conditions for the existence of WLLN are

(i) $E\left(X_i\right)$ exists for all $i$,

(ii) $B_n = Var\left[X_1, X_2, \cdots, X_n\right]$ exists and

(iii) $\dfrac{B_n}{n^2} \to 0$ as $n \to \infty$.

Condition (i) is necessary without it the law itself cannot be stated. But the condition (ii) and (iii) are not necessary, (iii) is however a sufficient condition.

---

**Question 9:** State Theorem 5.4.1 (Chebyshev's Law of Large Numbers) and prove the weak law of large numbers, using the assumption of finite $Var(X_i) = \sigma^2$ (for all $i$) and Chebyshev's inequality.

**Answer:**

**Theorem 5.4.1 (Chebyshev's Law of Large Numbers).** *Given $X_1, X_2, \cdots$ an infinite sequence of i.i.d. random variables with finite expected value $E(X_i) = \mu < \infty\ \forall\ i$, we are interested in the convergence of the sample average $\overline{X}_n = \frac{1}{n}(X_1 + \cdots + X_n)$.*

*The weak law of large numbers states:*

$$\overline{X}_n \xrightarrow{P} \mu \quad \text{when } n \to \infty.$$

*Proof.* This proof uses the assumption of finite $Var(X_i) = \sigma^2$ (for all $i$). The independence of the random variables implies no correlation between them, and we have that as the following

$$\begin{aligned}
Var\left(\overline{X}_n\right) &= Var\left(\frac{1}{n}(X_1 + \cdots + X_n)\right) \\
&= \frac{1}{n^2} Var(X_1 + \cdots + X_n) \\
&= \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}.
\end{aligned}$$

The common mean $\mu$ of the sequence is the mean of the sample average:

$$E\left(\overline{X}_n\right) = \mu.$$

Using Chebyshev's inequality on $\overline{X}_n$ results in

$$P\left(\left|\overline{X}_n - \mu\right| \geq \varepsilon\right) \leq \frac{\sigma^2}{n\varepsilon^2}.$$

This may be used to obtain the following:

$$P\left(\left|\overline{X}_n - \mu\right| < \varepsilon\right) = 1 - P\left(\left|\overline{X}_n - \mu\right| \geq \varepsilon\right) \geqslant 1 - \frac{\sigma^2}{n\varepsilon^2}.$$

As $n$ approaches infinity, the expression approaches 1. And by definition of convergence in probability, we have obtained

$$\overline{X}_n \xrightarrow{P} \mu \quad \text{when } n \to \infty.$$

Hence the theorem. $\blacksquare$

---

### C. Strong Law of Large Numbers (5.4.2)

**Question 10:** State the strong law of large numbers (SLLN) and explain its probabilistic interpretation.

**Answer:**

The strong law of large numbers states that the sample average converges almost surely to the expected value

$$\bar{X}_n \xrightarrow{\text{a.s.}} \mu, \qquad \text{when } n \to \infty.$$

That is,

$$Pr\left(\lim_{n \to \infty} \bar{X}_n = \mu\right) = 1.$$

What this means is that the probability that, as the number of trials "n" goes to infinity, the average of the observations converges to the expected value, is equal to one.

---

**Question 11:** State the necessary and sufficient conditions for the existence of the SLLN, and indicate which is necessary and which is sufficient.

**Answer:**

Necessary and sufficient conditions for the existence of SLLN are

(i) $E\left(X_i\right)$ exists for all $i$, and

(ii) $\sum_{i=1}^{\infty} \dfrac{\sigma_i^2}{i^2} < \infty$.

Condition (i) is necessary for the existence of strong law of large numbers and condition (ii) is sufficient. That is convergence of $\sum_{i=1}^{\infty} \dfrac{\sigma_i^2}{i^2}$ is sufficient for the existence of strong law of large numbers.

---

**Question 12:** State Theorem 5.4.2 (Kolmogorov Law of Large Numbers).

**Answer:**

**Theorem 5.4.2 (Kolmogorov Law of Large Numbers).** *Let $\{X_i\}$, $i = 1, 2, \cdots$, be a sequence of independent random variables such that $E(X_i) = \mu_i$ and $Var(X_i) = \sigma_i^2$. Then hold the following*

$$\sum_{i=1}^{\infty} \frac{\sigma_i^2}{i^2} < \infty \quad \implies \quad \bar{X}_n - \bar{\mu}_n \xrightarrow{\text{a.s.}} 0,$$

*that is, the sequence $X_1, X_2, \cdots$ obeys the strong law of large numbers.*

*Proof.* **Assignment

---

### D. Examples

**Question 13:** Let $X_i$ assume two values $i$ and $-i$ with equal probabilities. Show that the law of large numbers cannot be applied to the independent random variables $X_1, X_2, \cdots$, i.e., $X'$s.

**Answer:**

**Example:** Let $X_i$ assume two values $i$ and $-i$ with equal probabilities. Show that the law of large numbers cannot be applied to the independent random variables $X_1, X_2, \cdots$, i.e., $X'$s.

*Solution:* We have

$$P\left[X_i = i\right] = \frac{1}{2}, \quad P\left[X_i = -i\right] = \frac{1}{2}.$$

So we can obtain as

$$E\left[X_i\right] = \frac{1}{2}(i) + \frac{1}{2}(-i) = 0, \quad i = 1, 2, \cdots,$$

and

$$Var\left[X_i\right] = E\left[X_i^2\right] = \frac{i^2}{2} + \frac{i^2}{2} = i^2, \quad i = 1, 2, \cdots.$$

Since $X_1, X_2, \cdots, X_n$ are independent random variables, we can obtain as

$$\begin{aligned}
\frac{B_n}{n^2} &= \frac{1}{n^2} Var\left[X_1 + X_2 + \cdots + X_n\right] \\
&= \frac{1}{n^2}\left[1^2 + 2^2 + \cdots + n^2\right] \\
&= \frac{n(n+1)(2n+1)}{6n^2} \\
&= \frac{n\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)}{6} \to \infty \quad \text{as } n \to \infty.
\end{aligned}$$

Hence law of large numbers does not hold.

---

**Question 14:** Let $X_i$ can have two values $i^{\alpha}$ and $-i^{\alpha}$ with equal probabilities. Show that the law of large numbers can be applied to the independent random variables $X_1, X_2, \cdots$, if $\alpha < \frac{1}{2}$.

**Answer:**

**Example:** Let $X_i$ can have two values $i^{\alpha}$ and $-i^{\alpha}$ with equal probabilities. Show that the law of large numbers can be applied to the independent random variables $X_1, X_2, \cdots$, if $\alpha < \frac{1}{2}$.

*Solution:* We have

$$P\left[X_i = i^{\alpha}\right] = \frac{1}{2}, \quad P\left[X_i = -i^{\alpha}\right] = \frac{1}{2}.$$

So we can obtain as

$$E\left[X_i\right] = \frac{1}{2}\left(i^{\alpha}\right) + \frac{1}{2}\left(-i^{\alpha}\right) = 0, \quad i = 1, 2, \cdots,$$

and

$$Var\left[X_i\right] = E\left[X_i^2\right] = \frac{\left(i^{\alpha}\right)^2}{2} + \frac{\left(-i^{\alpha}\right)^2}{2} = i^{2\alpha}, \quad i = 1, 2, \cdots.$$

Since $X_1, X_2, \cdots, X_n$ are independent random variables, we can obtain as

$$\begin{aligned}
\frac{B_n}{n^2} &= \frac{1}{n^2} Var\left[X_1 + X_2 + \cdots + X_n\right] \\
&= \frac{1}{n^2}\left[1^{2\alpha} + 2^{2\alpha} + \cdots + n^{2\alpha}\right] \\
&= \frac{1}{n^2} \int_0^n x^{2\alpha}\, dx \qquad \text{[From Euler-Maclaurin's Formula]} \\
&= \frac{1}{n^2} \left[\frac{x^{2\alpha+1}}{2\alpha+1}\right]_0^n \\
&= \frac{1}{n^2} \boldsymbol{\cdot} \frac{n^{2\alpha+1}}{2\alpha+1} \\
&= \frac{n^{2\alpha-1}}{2\alpha+1} \to 0 \quad \text{as } n \to \infty \text{ if } \alpha < \frac{1}{2}.
\end{aligned}$$

Hence the results follows law of large numbers.

---

**Question 15:** Let $\{X_n\}$ be mutually independent and identically distributed random variables with mean $\mu$ and finite variance. If $S_n = X_1 + X_2 + \cdots + X_n$, prove that the law of large numbers does not hold for the sequence $\{S_n\}$.

**Answer:**

**Example:** Let $\{X_n\}$ be mutually independent and identically distributed random variables with mean $\mu$ and finite variance. If $S_n = X_1 + X_2 + \cdots + X_n$, prove that the low of large numbers does not hold for the sequence $\{S_n\}$.

*Solution:* Since $S_1, S_2, \cdots, S_n$ are mutually independent and identically distributed random variables, so

$$\begin{aligned}
\frac{B_n}{n^2} &= \frac{1}{n^2} Var\left[S_1 + S_2 + \cdots + S_n\right] \\
&= \frac{1}{n^2} Var\left[X_1 + (X_1 + X_2) + \cdots + (X_1 + X_2 + \cdots + X_n)\right] \\
&= \frac{1}{n^2} Var\left[nX_1 + (n-1)X_2 + \cdots + 2X_{n-1} + X_n\right] \\
&= \frac{1}{n^2}\left[n^2 Var\left(X_1\right) + (n-1)^2 Var\left(X_2\right) + \cdots + 2^2 Var\left(X_{n-1}\right) + 1^2 Var\left(X_n\right)\right]
\end{aligned}$$

Let $Var(X_i) = \sigma^2$ for all $i$, therefore

$$\begin{aligned}
\frac{B_n}{n^2} &= \frac{\sigma^2}{n^2}\left[1^2 + 2^2 + \cdots + n^2\right] \\
&= \frac{\sigma^2 n(n+1)(2n+1)}{6n^2} \\
&= \frac{\sigma^2 n\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)}{6} \to \infty \quad \text{as } n \to \infty.
\end{aligned}$$

Hence law of large numbers does not hold for the sequence $\{S_n\}$.

---

**Question 16 (Assignment):** Differentiate between the WLLN and the SLLN.

**Answer:**

**Assignment:** Differentiate between WLLN and SLLN.

---

## SECTION 5.5 — CENTRAL LIMIT THEOREM

### A. Definitions / General Concepts

**Question 1:** State what the central limit theorem (CLT) establishes about sums of independent random variables, and explain why it is considered a key result in probability theory.

**Answer:**

The central limit theorem (CLT) establishes that, in some situations, when independent random variables are added, their properly normalized sum tends toward a normal distribution (informally a "bell curve" distribution) even if the original variables themselves are not normally distributed. The theorem is a key concept in probability theory because it implies that probabilistic and statistical methods that work for normal distributions can be applicable to many problems involving other types of distributions.

---

**Question 2:** Using the example of repeatedly computing the mean of a large number of independent observations, explain what the CLT predicts about the distribution of that mean. Illustrate with the coin-flipping example.

**Answer:**

For example, suppose that a sample is obtained containing a large number of observations, each observation being randomly generated in a way that does not depend on the values of the other observations, and that the arithmetic mean of the observed values is computed. If this procedure is performed many times, the central limit theorem says that the distribution of the average will be closely approximated by a normal distribution. A simple example of this is that if one flips a coin many times the probability of getting a given number of heads in a series of flips will approach a normal curve, with mean equal to half the total number of flips in each series.

---

**Question 3:** Who first stated the CLT, and in what year? Who gave a rigorous proof under fairly general conditions, and in what year? Name the four special cases of the general CLT listed in the text.

**Answer:**

This theorem was first stated by Laplace in 1812 and a rigorous proof under fairly general conditions was given by Liapounov in 1901. Below list some particular cases of this general central limit theorem.

(i) De Moivre–Laplace theorem,

(ii) Lindeberge-Levy theorem,

(iii) Liapounov's theorem, and

(iv) Lindeberg-Feller theorem.

---

### B. Classical Central Limit Theorem (5.5.1)

**Question 4:** For a random sample $\{X_1, X_2, \cdots, X_n\}$ i.i.d. with mean $\mu$ and variance $\sigma^2$, define the sample average $S_n$ and state what it converges to according to the law of large numbers.

**Answer:**

Let $\{X_1, X_2, \cdots, X_n\}$ be a random sample of size $n$, that is, a sequence of independent and identically distributed random variables drawn from a distribution of expected value given by $\mu$ and finite variance given by $\sigma^2$. Suppose we are interested in the sample average

$$S_n = \frac{X_1 + \cdots + X_n}{n}$$

of these random variables. By the law of large numbers, the sample averages converge in probability and almost surely to the expected value $\mu$ as $n \to \infty$.

---

**Question 5:** Explain what the classical CLT says about the fluctuations of $S_n$ around $\mu$ as $n$ grows, in terms of $\sqrt{n}(S_n - \mu)$, and describe the approximate distribution of $S_n$ for large $n$.

**Answer:**

The classical central limit theorem describes the size and the distributional form of the stochastic fluctuations around the deterministic number $\mu$ during this convergence. More precisely, it states that as $n$ gets larger, the distribution of the difference between the sample average $S_n$ and its limit $\mu$, when multiplied by the factor $\sqrt{n}$ (that is $\sqrt{n}(S_n - \mu)$), approximates the normal distribution with mean 0 and variance $\sigma^2$. For large enough $n$, the distribution of $S_n$ is close to the normal distribution with mean $\mu$ and variance $\dfrac{\sigma^2}{n}$.

---

**Question 6:** What makes the CLT useful with respect to the shape of the underlying distribution of the $X_i$?

**Answer:**

The usefulness of the theorem is that the distribution of $\sqrt{n}(S_n - \mu)$ approaches normality regardless of the shape of the distribution of the individual $X_i$.

---

**Question 7:** State Theorem 5.5.1 (Lindeberg–Lévy CLT).

**Answer:**

**Theorem 5.5.1** (Lindeberg–Lévy CLT). *Suppose $\{X_1, X_2, \cdots\}$ is a sequence of independent and identically distributed random variables with $E(X_i) = \mu$ and $Var(X_i) = \sigma^2 < \infty$. Then as $n$ approaches infinity, the random variables $\sqrt{n}(S_n - \mu)$ converge in distribution to a normal $N(0, \sigma^2)$:*

$$\sqrt{n}\left(S_n - \mu\right)\ \xrightarrow{d}\ N\left(0, \sigma^2\right).$$

---

### C. Proof of Theorem 5.5.1

**Question 8:** Prove Theorem 5.5.1 up through deriving the characteristic function $\varphi_{Y_1}(t/\sqrt{n})$ via Taylor's theorem. Define $Z_n$ and $Y_i$ along the way.

**Answer:**

*Proof.* The central limit theorem has a simple proof using characteristic function. It is similar to the proof of the (weak) law of large numbers.

Assume $\{X_1, X_2, \cdots, X_n\}$ are independent and identically distributed random variables, each with mean $\mu$ and finite variance $\sigma^2$. The sum $X_1 + X_2 + \cdots + X_n$ has mean $n\mu$ and variance $n\sigma^2$. Consider the random variable

$$Z_n = \frac{X_1 + \cdots + X_n - n\mu}{\sqrt{n\sigma^2}} = \sum_{i=1}^{n} \frac{X_i - \mu}{\sqrt{n\sigma^2}} = \sum_{i=1}^{n} \frac{1}{\sqrt{n}} Y_i,$$

where in the last step we defined the new random variables $Y_i = \dfrac{X_i - \mu}{\sigma}$, each with zero mean and unit variance. The characteristic function of $Z_n$ is given by

$$\varphi_{Z_n}(t) = \varphi_{\sum_{i=1}^{n} \frac{1}{\sqrt{n}}Y_i}(t) = \varphi_{Y_1}\left(\frac{t}{\sqrt{n}}\right) \varphi_{Y_2}\left(\frac{t}{\sqrt{n}}\right) \cdots \varphi_{Y_n}\left(\frac{t}{\sqrt{n}}\right) = \left[\varphi_{Y_1}\left(\frac{t}{\sqrt{n}}\right)\right]^n,$$

where in the last step we used the fact that all of the $Y_i$ are identically distributed. The characteristic function of $Y_1$ is, by Taylor's theorem,

$$\varphi_{Y_1}\left(\frac{t}{\sqrt{n}}\right) = 1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right), \qquad \left(\frac{t}{\sqrt{n}}\right) \to 0$$

where $o(t^2)$ is little $o$ notation for some function of $t$ that goes to zero more rapidly than $t^2$. By the limit of the exponential function $\left(e^x = \left(1 + \dfrac{x}{n}\right)^n\right)$, the characteristic

---

**Question 9:** Complete the proof of Theorem 5.5.1: find $\lim_{n\to\infty}\varphi_{Z_n}(t)$, identify the resulting distribution, and state what this implies for $X_1+\cdots+X_n$ and for $S_n$.

**Answer:**

function of $Z_n$ equals

$$\varphi_{Z_n}(t) = \left(1 - \frac{t^2}{2n} + o\left(\frac{t^2}{n}\right)\right)^n \to e^{-\frac{1}{2}t^2}, \qquad n \to \infty.$$

All of the higher order terms vanish in the limit $n \to \infty$. The right hand side equals the characteristic function of a standard normal distribution $N(0,1)$, which implies through Lévy's continuity theorem that the distribution of $Z_n$ will approach $N(0,1)$ as $n \to \infty$. Therefore, the sum $X_1 + \cdots + X_n$ will approach that of the normal distribution $N\left(n\mu, n\sigma^2\right)$, and the sample average

$$S_n = \frac{X_1 + \cdots + X_n}{n}$$

converges to the normal distribution, $N\left(\mu, \dfrac{\sigma^2}{n}\right)$. $\blacksquare$

---

*End of Question Bank — Chapter 5: Convergence, STAT-2101: Probability Theory*