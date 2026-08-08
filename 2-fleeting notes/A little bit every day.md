---
title: A little bit every day
---
Large goals can often seem daunting, like attempting to scale a mountain in a single effort. Instead, focus on consistent, small actions—such as writing one paragraph [[Writing Habits]], exercising for 10 minutes [[Exercise Routine]], or learning a new vocabulary word each day. These incremental steps accumulate over time, fostering habits [[Atomic Habits]] without overwhelming pressure or risk of burnout. Consistency outperforms sporadic intensity, leading to meaningful progress. Begin with a modest task tomorrow to experience the benefits. Maintain simplicity and steadiness for sustained results.100044101


$$f(x) = \sigma(W^T x + b)$$
$$\begin{bmatrix} w_1 \\ w_2 \end{bmatrix}$$

$$\begin{aligned}
L(w) &= \sum (y_i - \hat{y}_i)^2 \\
     &= \sum (y_i - w^T x_i)^2
\end{aligned}$$
```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Fast data split blueprint
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
