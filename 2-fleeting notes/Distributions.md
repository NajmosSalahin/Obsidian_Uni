# 📊 Complete Guide to Probability Distributions

---

## Table of Contents

1. [Foundational Concepts](https://www.google.com/search?q=%23foundational-concepts&authuser=1)
    
2. [Discrete Distributions](https://www.google.com/search?q=%23discrete-distributions&authuser=1)
    
3. [Continuous Distributions](https://www.google.com/search?q=%23continuous-distributions&authuser=1)
    
4. [Sampling Distributions](https://www.google.com/search?q=%23sampling-distributions&authuser=1)
    
5. [Multivariate Distributions](https://www.google.com/search?q=%23multivariate-distributions&authuser=1)
    
6. [Special / Advanced Distributions](https://www.google.com/search?q=%23special--advanced-distributions&authuser=1)
    
7. [Empirical & Non-Parametric Distributions](https://www.google.com/search?q=%23empirical--non-parametric-distributions&authuser=1)
    
8. [Quick Reference Table](https://www.google.com/search?q=%23quick-reference-table&authuser=1)
    

---

## Foundational Concepts

|**Symbol**|**Meaning**|
|---|---|
|$f(x)$|**Probability Density Function (PDF)** — continuous|
|$P(X=x)$|**Probability Mass Function (PMF)** — discrete|
|$F(x) = P(X \leq x)$|**Cumulative Distribution Function (CDF)**|
|$S(x) = 1 - F(x)$|**Survival / Reliability Function**|
|$h(x) = \frac{f(x)}{S(x)}$|**Hazard Function**|
|$M(t) = E[e^{tX}]$|**Moment Generating Function (MGF)**|
|$\phi(t) = E[e^{itX}]$|**Characteristic Function**|
|$\mu = E[X]$|**Mean**|
|$\sigma^2 = \text{Var}(X) = E[(X-\mu)^2]$|**Variance**|
|$\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3}$|**Skewness**|
|$\gamma_2 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3$|**Excess Kurtosis**|

---

## Discrete Distributions

### 1. Bernoulli Distribution — $\text{Bernoulli}(p)$

A single trial with two outcomes: success (1) or failure (0).

- **PMF:** $P(X = x) = p^x (1-p)^{1-x}, \quad x \in \{0, 1\}$
    
- **Moments:** $E[X] = p, \quad \text{Var}(X) = p(1 - p)$
    
- **MGF:** $M(t) = (1-p) + pe^t$
    

### 2. Binomial Distribution — $\text{Bin}(n, p)$

Number of successes in $n$ independent Bernoulli trials.

- **PMF:** $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \dots, n$
    
- **Moments:** $E[X] = np, \quad \text{Var}(X) = np(1-p)$
    
- **Normal Approximation:** When $np > 5$ and $n(1-p) > 5$: $X \approx N(np, np(1-p))$
    

### 3. Geometric Distribution — $\text{Geo}(p)$

Number of trials until the **first** success.

- **PMF (number of trials):** $P(X = k) = (1-p)^{k-1}p, \quad k = 1, 2, 3, \dots$
    
- **Memoryless Property:** $P(X > m+n \mid X > m) = P(X > n)$
    

### 4. Poisson Distribution — $\text{Poi}(\lambda)$

Number of events in a fixed interval given constant average rate $\lambda$.

- **PMF:** $P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \dots$
    
- **Moments:** $E[X] = \lambda, \quad \text{Var}(X) = \lambda$
    
- **MGF:** $M(t) = \exp(\lambda(e^t - 1))$
    

---

## Continuous Distributions

### 1. Normal (Gaussian) Distribution — $N(\mu, \sigma^2)$

The cornerstone of statistics and the Central Limit Theorem.

- **PDF:**
    
    $$f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$
    
- **Standardized ($Z$):** $f(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$
    
- **68-95-99.7 Rule:** * $P(\mu - \sigma < X < \mu + \sigma) \approx 0.6827$
    
    - $P(\mu - 2\sigma < X < \mu + 2\sigma) \approx 0.9545$
        
    - $P(\mu - 3\sigma < X < \mu + 3\sigma) \approx 0.9973$
        

### 2. Exponential Distribution — $\text{Exp}(\lambda)$

Time between events in a Poisson process.

- **PDF:** $f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$
    
- **CDF:** $F(x) = 1 - e^{-\lambda x}$
    
- **Moments:** $E[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}$
    

### 3. Gamma Distribution — $\text{Gamma}(\alpha, \beta)$

- **PDF:**
    
    $$f(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad x > 0$$
    
- **Moments:** $E[X] = \frac{\alpha}{\beta}, \quad \text{Var}(X) = \frac{\alpha}{\beta^2}$
    

### 4. Student's t-Distribution — $t(\nu)$

Used for inference when the population variance is unknown.

- **Definition:** $T = \frac{Z}{\sqrt{V/\nu}}$ where $Z \sim N(0,1)$ and $V \sim \chi^2(\nu)$
    
- **Limit:** $t(\nu) \to N(0,1)$ as $\nu \to \infty$
    

---

## Sampling Distributions

### 1. Sample Mean — $\bar{X}$

For a random sample of size $n$ from a population with mean $\mu$ and variance $\sigma^2$:

- **Standard Error:** $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$
    
- **Central Limit Theorem (CLT):** As $n \to \infty$, $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)$
    

### 2. Sample Variance — $S^2$

For $X_1, \dots, X_n \sim N(\mu, \sigma^2)$:

- **Chi-Squared Relationship:**
    
    $$\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$
    

---

## Multivariate Distributions

### 1. Multivariate Normal — $\text{MVN}(\mu, \Sigma)$

- **PDF:**
    
    $$f(x) = (2\pi)^{-p/2} |\Sigma|^{-1/2} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right)$$
    
- **Mahalanobis Distance:** $D^2(x) = (x-\mu)^T \Sigma^{-1} (x-\mu) \sim \chi^2(p)$
    

---

## Quick Reference Table

|**Distribution**|**Support**|**Mean**|**Variance**|
|---|---|---|---|
|$\text{Bernoulli}(p)$|$\{0,1\}$|$p$|$p(1-p)$|
|$\text{Binomial}(n,p)$|$\{0,\dots,n\}$|$np$|$np(1-p)$|
|$\text{Poisson}(\lambda)$|$\{0,1,\dots\}$|$\lambda$|$\lambda$|
|$\text{Uniform}(a,b)$|$[a,b]$|$\frac{a+b}{2}$|$\frac{(b-a)^2}{12}$|
|$\text{Normal}(\mu,\sigma^2)$|$\mathbb{R}$|$\mu$|$\sigma^2$|
|$\text{Exponential}(\lambda)$|$\mathbb{R}^+$|$\frac{1}{\lambda}$|$\frac{1}{\lambda^2}$|
|$\text{Gamma}(\alpha,\beta)$|$\mathbb{R}^+$|$\frac{\alpha}{\beta}$|$\frac{\alpha}{\beta^2}$|
|$\chi^2(\nu)$|$\mathbb{R}^+$|$\nu$|$2\nu$|

---

## Key Relationships

- **Normal** $\to$ **$\chi^2(\nu)$**: Sum of squared standard normals.
    
- **Binomial** $\xrightarrow{n \to \infty}$ **Poisson**: When $p$ is small and $np = \lambda$.
    
- **Exponential** $\to$ **Gamma**: Sum of $n$ i.i.d. exponential variables.
    
- **$t(1)$** $\equiv$ **Cauchy**: The Student's t-distribution with 1 degree of freedom.
    

---