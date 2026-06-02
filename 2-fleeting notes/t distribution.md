## 3.1 Student's $t$-distribution

Let $x_i$ $(i = 1, 2, \cdots, n)$ be a random sample of size $n$ from a normal population with mean $\mu$ and variance $\sigma^2$. Then Student's $t$ is defined by the statistic

$$t = \frac{\bar{x} - \mu}{\frac{S}{\sqrt{n}}},$$

where $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$, is the sample mean and $S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$, is an unbiased estimate of the population variance $\sigma^2$, and it follows Student's $t$- distribution with $\nu = (n - 1)$ degrees of freedom with probability density function

$$f(t) = \frac{1}{\sqrt{\nu} \ B \left(\frac{1}{2}, \frac{\nu}{2}\right)} \cdot \frac{1}{\left(1 + \frac{t^2}{\nu}\right)^{\frac{\nu+1}{2}}} ; \ -\infty < t < \infty. \tag{3.1}$$

## 3.2 Derivation of Student's $t$-distribution

The expression of Student's $t$- statistic can be written as

$$\begin{aligned} t &= \frac{\bar{x} - \mu}{\frac{S}{\sqrt{n}}} \\ \Rightarrow t^2 &= \frac{n(\bar{x} - \mu)^2}{S^2}, \end{aligned}$$

further expressed as

$$\begin{aligned} \frac{t^2}{n - 1} &= \frac{n(\bar{x} - \mu)^2}{(n - 1)S^2} \\ &= \frac{\frac{(\bar{x} - \mu)^2}{\frac{\sigma^2}{n}}}{\frac{(n - 1)S^2}{\sigma^2}} \\ &= \frac{\left(\frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}}\right)^2}{\frac{(n - 1)S^2}{\sigma^2}}. \end{aligned}$$



Since $x_i$ $(i = 1, 2, \cdots, n)$ is a random sample from the normal distribution with mean $\mu$ and variance $\sigma^2$, then

$$\begin{aligned} \bar{x} &\sim N\left(\mu, \frac{\sigma^2}{n}\right) \\ \Rightarrow \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} &\sim N(0, 1). \end{aligned}$$



Hence $\left(\frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}}\right)^2$, being the square of a standard normal variate is a $\chi^2$-variate with 1 d.f. Also $\frac{(n-1)S^2}{\sigma^2}$ is a $\chi^2$-variate with $\nu = (n - 1)$ d.f.

Further since $\bar{x} and S^2$ are independently distributed, $\frac{t^2}{n-1}$ being the ratio of two independent $\chi^2$-variate with 1 and $\nu = (n - 1)$ degrees of freedom respectively, is $\beta_2 \left(\frac{1}{2}, \frac{\nu}{2}\right)$ variate and its distribution is given by

$$\begin{aligned} dF(t) &= \frac{1}{\beta_2 \left(\frac{1}{2}, \frac{\nu}{2}\right)} \cdot \frac{\left(\frac{t^2}{\nu}\right)^{\frac{1}{2}-1}}{\left(1 + \frac{t^2}{\nu}\right)^{\frac{\nu+1}{2}}} d\left(\frac{t^2}{\nu}\right), \ 0 \le t^2 \le \infty \\ & \qquad \qquad \qquad \qquad \qquad \left[ f(x) = \frac{1}{B(\alpha, \beta)} \cdot \frac{x^{\alpha-1}}{(1+x)^{\alpha+\beta}} \right] \\ &= \frac{1}{\beta_2 \left(\frac{1}{2}, \frac{\nu}{2}\right)} \cdot \frac{\frac{\sqrt{\nu}}{t}}{\left(1 + \frac{t^2}{\nu}\right)^{\frac{\nu+1}{2}}} \frac{2t}{\nu} dt, \ 0 \le t \le \infty \\ &= \frac{1}{\sqrt{\nu} \ B \left(\frac{1}{2}, \frac{\nu}{2}\right)} \cdot \frac{1}{\left(1 + \frac{t^2}{\nu}\right)^{\frac{\nu+1}{2}}} dt ; \ -\infty < t < \infty, \end{aligned}$$

the factor 2 disappearing since the integral from $-\infty$ to $\infty$ must be unity. This is the required probability density function of Student's $t$-distribution with $\nu = (n - 1)$ degrees of freedom.


