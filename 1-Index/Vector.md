Here is the text formatted with proper Markdown and LaTeX.

## Chapter 1: Vectors

### Definitions

Definition 1.1. Let $X_1 = (x_{11}, x_{12}, \dots, x_{1n})$ and $X_2 = (x_{21}, x_{22}, \dots, x_{2n})$ be any two $n$-dimensional (finite) vectors. Then the inner product of $X_1$ and $X_2$ is the real-valued scalar

$$X_1 \cdot X_2 = \sum_{i=1}^n x_{1i}x_{2i} = x_{11}x_{21} + x_{12}x_{22} + \dots + x_{1n}x_{2n}=\sum_{i=1}^n (x_{1i} . x_{2i})$$

Definition 1.2. Let $X_1 = (x_{11}, x_{12}, \dots, x_{1n})$ and $X_2 = (x_{21}, x_{22}, \dots, x_{2n})$ be any two $n$-dimensional (finite) vectors. Then the distance between $X_1$ and $X_2$ is given by the (nonnegative) function

$$d(X_1, X_2) = ||X_1 - X_2|| = \left[\sum_{i=1}^n (x_{1i} - x_{2i})^2\right]^{1/2}$$

Definition 1.3. Let $X_1 = (x_{11}, x_{12}, \dots, x_{1n})$ be any $n$-dimensional (finite) vector. Then the length, or norm, of $X_1$ is given be the (nonnegative) function

$$||X_1|| = \left[\sum_{i=1}^n x_{1i}^2\right]^{1/2}$$

**Definition 1.4.** A $n$-dimensional vector $Y$ is said to be linearly dependent on a set of $n$-dimensional vectors $X_1, X_2, \dots, X_k$ if and only if $Y$ can be expressed as a linear combination of these vectors.

Definition 1.5. A set of $n$-dimensional vectors $X_1, X_2, \dots, X_k$ is said to be linearly interdependent if and only if there exist scalars $\beta_1, \beta_2, \dots, \beta_k$, not all zero, such that

$$\beta_1X_1 + \beta_2X_2 + \dots + \beta_kX_k = 0$$

**Definition 1.6.** A vector $Y$ is termed a unit vector if and only if it possesses unit length, i.e., $|| Y || = 1$.

Definition 1.7. Two unit vectors $E_i$, and $E_j$ are mutually orthogonal (perpendicular) if and only if

$$E_i \cdot E_j = 0 \text{ for } i \neq j$$

**Definition 1.8.** A norm $n(X)$ defined on a linear vector space is a real-valued scalar function of the vector $X$ if it satisfies the following axioms:

1. $n(X_1 + X_2) \leq n(X_1) + n(X_2)$ for any two vectors $X_1$ and $X_2$.
    
2. $n(kX) = |k|n(X)$, where $|k|$ denotes the modulus.
    
3. $n(X) = 0$ if and only if $X = 0$.
    

**Definition 1.9.** The distance $d(X_1, X_2)$ between two vectors $X_1$ and $X_2$ is a real-valued function that satisfies the following axioms.

1. $d(X_1, X_2) = d(X_2,X_1)$.
    
2. $d(X_1, X_3) \leq d(X_1, X_2)+ d(X_2, X_3)$, where $X_3$ is any third vector.
    
3. $d(X_1, X_2) = 0$ if and only if $X_1 = X_2$.
    

Definition 1.10. Let $X = (x_1, x_2, \dots, x_n)$ denote a $n$-dimensional variable vector with mean $\bar{x}$. Then the variance of $X$, written as $\text{var}(X)$ (or $s^2_x$) is defined as

$$\text{var}(X) = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 = \frac{1}{n-1} ||X^*||^2$$

where $X^* = X - \bar{x} \mathbf{1}$.

Definition 1.11. Let $X_1 = (x_{11}, x_{21}, \dots, x_{n1})$ and $X_2 = (x_{12}, x_{22}, \dots, x_{n2})$ be $n$-dimensional vectors with means $\bar{x}_1$ and $\bar{x}_2$. Then the covariance between $X_1$ and $X_2$, written as $\text{cov}(X_1, X_2)$ is defined as

$$\text{cov}(X_1, X_2) = \frac{1}{n-1} \sum_{i=1}^n (x_{i1} - \bar{x}_1)(x_{i2} - \bar{x}_2) = \frac{1}{n-1} X_1^* \cdot X_2^*$$

where $X_1^* = X_1 - \bar{x}_1 \mathbf{1}$ and $X_2^* = X_2 - \bar{x}_2 \mathbf{1}$.

---

### Theorems

Theorem 1.1. The negative vector of $- A$ is the vector $A$.

PROOF: Let $A^+$ be the negative vector of $A$, and $A^*$ the negative vector of $- A$. We will now prove that $A^* = A$. By rule 4 we have, 

$$- A + A^* = A + A^+ = 0$$

Adding $A$ to both sides of the equation yields

$$A + (- A) + A^* = A + A^+ + A$$
or
$$0 + A^* = A + 0 \text{ (rule 4)}$$
Thus
$$A^* = A \text{ (rule 3). }\square$$

Theorem 1.2. The inner product is distributive over addition (subtraction), so that
$$X_1 \cdot (X_2 + X_3) = X_1 \cdot X_2 + X_1 \cdot X_3$$
where $X_1, X_2$, and $X_3$ are any $n$-dimensional vectors.

Theorem 1.3. The inner product is commutative, that is,

$$X_1 \cdot X_2 = X_2 \cdot X_1$$

where $X_1$ and $X_2$ are any $n$-dimensional vectors.

Theorem 1.4. The inner product is commutative with respect to scalar multiplication, so that

$$X_1 \cdot (kX_2) = k ( X_1 \cdot X_2) = ( X_1 \cdot X_2) k$$

where $k$ is any scalar and $X_1$, and $X_2$ are $n$-dimensional vectors.

Corollary. Multiplying a vector by a positive scalar alters magnitude but not direction.

PROOF: Let $k > 0$ be any scalar. Then the magnitude of the vector $kX_1$, is

$$||kX_1|| = \left[ (kx_{11})^2 + (kx_{12})^2 + \dots + (kx_{1n})^2 \right]^{1/2} = k ||X_1||$$

so that for $k \neq 1$ scalar multiplication either magnifies or shrinks the length of $X_1$, depending on the magnitude of $k$. Since the relative magnitudes and the positions of the components $x_{1j}$ are not changed, it follows that multiplication by $k$ does not alter the direction of $X_1, \square$

Theorem 1.5. Any $n$-dimensional vector can be standardized to unit length.

PROOF: Let $Y = (y_1, y_2, \dots, y_n)$ be any $n$-dimensional vector with length $|| Y ||$. Let

$$Y^* = \frac{1}{|| Y ||} Y$$

Then $Y^$ is a unit vector, since*

$$|| Y^* || = \left( \sum_{i=1}^n \frac{y_i^2}{|| Y ||^2} \right)^{1/2} = \frac{1}{|| Y ||} \left( \sum_{i=1}^n y_i^2 \right)^{1/2} = \frac{|| Y ||}{|| Y ||} = 1. \square$$

Theorem 1.6. Let $X$ and $Y$ be two linearly dependent nonzero vectors. Then

i. $||X \cdot Y|| = ||X|| ||Y||$,

ii. $||X+Y|| = ||X|| + ||Y||$.

Theorem 1.7. Let $X_1 = (x_{11}, x_{12}, \dots, x_{1n})$ and $X_2 = (x_{21}, x_{22}, \dots, x_{2n})$ be two nonzero vectors in $n$-dimensional space. If $\theta$ is the angle between $X_1$ and $X_2$ and if $a_1, a_2, \dots, a_n$ and $b_1, b_2, \dots, b_n$ are direction cosines of $X_1$ and $X_2$, respectively, then

i. $\cos \theta = a_1b_1 + a_2b_2 + \dots + a_nb_n$, where $\cos \alpha_i = a_i$ and $\cos \beta_i = b_i$, and $\alpha_i$ and $\beta_i$ are angles formed by $X_1, X_2$, and the $n$ coordinate axes;

ii. $X_1 \cdot X_2 = ||X_1|| ||X_2|| \cos \theta$.

Theorem 1.8 (Bunyakovsky-Cauchy-Schwartz Inequality). If $X_1 = (x_{11}, x_{12}, \dots, x_{1n})$, and $X_2 = (x_{21}, x_{22}, \dots, x_{2n})$ are two nonzero $n$-dimensional vectors, then

$$|X_1 \cdot X_2| \leq ||X_1|| ||X_2||$$

Theorem 1.9 (Minkowski Triangle Inequality). If $X_1 = (x_{11}, x_{12}, \dots, x_{1n})$ and $X_2 = (x_{21}, x_{22}, \dots, x_{2n})$ are two nonzero $n$-dimensional vectors, then

$$||X_1 + X_2|| \leq ||X_1|| + ||X_2||$$

Theorem 1.10. A set of $k$ distinct $n$-dimensional vectors $X_1, X_2, \dots, X_k$ lie on the same straight line if and only if there exist $k$ nonzero coefficients $\beta_1, \beta_2, \dots, \beta_k$ such that

$$\beta_1X_1 + \beta_2X_2 + \dots + \beta_kX_k = 0$$

**Theorem 1.11.** A linear vector equation of the form $\gamma_1X_1 + \gamma_2X_2 + \dots + \gamma_kX_k = 0$ is independent of the position of the origin if and only if $\gamma_1 + \gamma_2 + \dots + \gamma_k = 0$.

**Theorem 1.12.** Let $d_p(X_1, X_2)$ be the generalized Minkowski metric distance function (1.24). Then $d_p(X_1, X_2)$ is invariant with respect to a parallel translation of axes.

---

### Examples

Example 1.1. The two vectors

$$A = (3,8,1), B = (3,8,1)$$

are equal.

Example 1.2 Find the sum and difference of the vectors $A = (3, -1, 0)$ and $B = (1, 4, -7)$.

SOLUTION: We have

$$A + B = (3+1, -1+4, 0-7) = (4, 3, -7)$$

and

$$A - B = (3-1, -1-4, 0-(-7)) = (2, -5, 7)$$

Example 1.3 Find, for the vector $A = (a_1, a_2, \dots, a_n)$, the negative vector $- A$.

SOLUTION:

$$- A = (- a_1, - a_2, \dots, - a_n)$$

Thus $A + (- A) = A - A = 0$.

Example 1.4. The vector $Y = (11, 16, 21 )$ is linearly dependent on vectors $X_1 = (1, 2, 3)$ and $X_2 = (4, 5, 6)$, since

$$(11, 16, 21) = 3(1,2,3)+2(4,5,6)$$

also, it can be verified that

$$(11, 16, 21) - 3(1, 2, 3) - 2(4, 5, 6) = (0, 0, 0) = 0$$

so that Definition 1.5 applies, where we let

$$\beta_1 = 1, \beta_2 = - 3, \beta_3 = - 2$$

Example 1.5. i. The vectors

$$E_1 = (1,0,0), E_2 = (0, 1, 0), E_3 = (0, 0, 1)$$

are three-dimensional unit vectors, since (see also Figure 1.3)

$$|| E_1|| = || E_2|| = || E_3|| = 1$$

ii. The vector

$$E = (0.267,0.534,0.802)$$

is a three-dimensional unit vector, since

$$|| E || = (0.267^2 + 0.534^2 + 0.802^2)^{1/2} = 1$$

**Example 1.6.** The vectors $E_1, E_2$, and $E_3$ of the previous example are orthogonal unit vectors.

Example 1.7. To normalize $Y = (2,3,4)$ and $Y^*$ to unit length we proceed as follows. We have

$$|| Y || = (2^2 + 3^2 + 4^2)^{1/2} = \sqrt{29} = 5.385$$

and unit vectors $\mathbf{E}_1$ and $\mathbf{E}_2$ are given by

$$E = (2/5.385, 3/5.385, 4/5.385) = (0.371, 0.557, 0.743)$$

Example 1.8. Let $Y = (3, 6)$ be a vector whose coordinates are given with respect to the unit vector axes $E_1 = (1,0)$ and $E_2 = (0,1)$.

i. Find the components of $Y$ with respect to axes $X_1 = (2, 0)$ and $X_2 = (0,3)$.

ii. Find the magnitude of $Y$ with respect to both coordinate axes.

SOLUTION: i. Y can be expressed as

$$Y = 3E_1 + 6E_2 = 3(1,0) + 6(0,1) = (3, 6)$$

with respect to $E_1$ and $E_2$. To find the components of $Y$ relative to $X_1 = (2, 0)$ and $X_2 = (0,3)$ we have

$$Y = aX_1 + bX_2$$

where $a$ and $b$ are the unknown components. Then $Y = a(2, 0) + b(0, 3) = (2a, 3b)$ or $(3, 6) = (2a, 3b)$. Since equal vectors must have equal components, we obtain $2a = 3$ and $3b = 6$. Thus $a = 3/2$ and $b = 2$ are the components with respect to $X_1$ and $X_2$; that is,

$$Y = \frac{3}{2}(2, 0) + 2(0, 3) = (3, 6)$$

ii. Since changing the reference system can not alter vector magnitude, we have

$$|| Y || = (3^2 + 6^2)^{1/2} = \sqrt{45}$$

where $Y \cdot Y = 3^2 + 6^2$. Similarly, we find

$$|| Y ||^2 = (3/2)^2 || X_1 ||^2 + 2^2 || X_2 ||^2 = 9/4(4) + 4(9) = 9 + 36 = 45$$

since $E_1 \cdot E_2 = 0$.

Example 1.9 Show that the vectors $X = (1, 2)$ and $Y = (2, 4)$ have the same direction cosines.

SOLUTION: Vector $X$ has direction cosines

$$\cos \theta_1 = 1/\sqrt{5} = 0.447 \quad \text{and} \quad \cos \theta_2 = 2/\sqrt{5} = 0.894$$

which are identical to those of $Y$ since

$$|| Y || = (4 + 16)^{1/2} = 4.47$$

Example 1.10. Find the angle that lies between the vectors $X_1 = (1,2,3,4)$ and $X_2 = (1,1,1,1)$.

SOLUTION: The inner product and vector lengths are

$$X_1 \cdot X_2 = 1 + 2 + 3 + 4 = 10 \quad \text{and} \quad || X_1 || = (1+4+9+16)^{1/2} = \sqrt{30} \approx 5.48$$

$$|| X_2 || = (1+1+1+1)^{1/2} = \sqrt{4} = 2$$

Applying Equation (1.18g) then yields

$$\cos \theta = \frac{X_1 \cdot X_2}{|| X_1 || || X_2 ||} = \frac{10}{5.48(2)} = 0.912$$

so that $\theta = 69^\circ$. It is also easy to verify Equations (1.19) and (1.20), since $||X_1|| ||X_2|| = 5.48(4.61) = 25.3$, and evidently $10 < 25.3$. Also, the Minkowski inequality holds, since $||X_1 + X_2|| = ||(2, 3, 4, 5)|| = \sqrt{54} \approx 7.35$ and $||X_1|| + ||X_2|| = 5.48 + 2.0 = 7.48$, so that $7.35 < 7.48$.

Example 1.11. Find the inner product of the vectors $X_1$ and $X_2$ when $\theta = 30^\circ$, $||X_1|| = 2$, and $||X_2|| = 3$.

SOLUTION: Using Equation (1.18g), we have

$$X_1 \cdot X_2 = || X_1 || || X_2 || \cos 30^\circ = 2(3) \times 0.866 = 5.196$$

Example 1.12. The vector $Y = (3.5, 2.5, 9, 3)$ segments the distance between $X_1 = (2, 1, 0, 4)$ and $X_2 = (4, 3, 6, 2)$ into two segments, in the ratio $3:5$, since it is easy to verify that

$$Y = \frac{5}{8}(2, 1, 0, 4) + \frac{3}{8}(4, 3, 6, 2)$$

Also, $Y, X_1$, and $X_2$ must lie on the same straight line.

Example 1.13. Express the vector $X = (2, -3, 1, 4)$ with respect to the new origin $Y = (2, -1, 0, 6)$.

SOLUTION: Taking $Y = (2, -1, 0, 6)$ as the new origin, we have $X' = X - Y = (0, -2, 1, -2)$ as the new coordinates of $X$.

Example 1.14. Find the mean vector of the following vectors: $X_1 = (1,4), X_2 = (1, 3), X_3 = (4, 5)$, and $X_4 = (6, 8)$. Show that it is not affected when the origin $(0, 0)$ is translated to $(2, 3)$.

SOLUTION: We have

$$\bar{X} = \frac{1}{4}(1+1+4+6, 4+3+5+8) = \frac{1}{4}(12, 20) = (3, 5)$$

Translating the axes to the new origin $(2,3)$ then yields new coordinates $X'_1 = (-1, 1), X'_2 = (-1, 0), X'_3 = (2, 2)$, and $X'_4 = (4, 5)$, and the mean point with respect to the new origin is then

$$\bar{X}' = \frac{1}{4}(-1-1+2+4, 1+0+2+5) = \frac{1}{4}(4, 8) = (1, 2)$$

which is the same as the coordinates of $\bar{X} = (3, 5)$ with respect to the origin $(2, 3)$, so that we still have

$$\bar{X} = (3, 5)$$

Example 1.15. Consider two points in a city that are measured, in kilometers (from some reference point), by the vectors $X_1 = (8,2)$ and $X_2 = (4,7)$. Compute the distance between the two points in $L_1, L_2$, and $L_\infty$ vector spaces.

SOLUTION: If a helicopter, say, is available, then the relevant distance between $X_1$ and $X_2$ is given by the metric

$$d_2(X_1, X_2) = [(8-4)^2 + (2-7)^2]^{1/2} = \sqrt{16+25} = 6.4 \text{ km}$$

since $d_2(X_1, X_2)$ measures distance along the straight line that joins $X_1$ and $X_2$.

However, when streets of a city intersect at right angles, then for a pedestrian $d_2(X_1, X_2)$ is misleading, and the relevant metric is

$$d_1(X_1, X_2) = |8-4| + |2-7| = 4 + 5 = 9 \text{ km}$$

evidently a greater distance than $d_2(X_1, X_2)$.

The $L_\infty$ distance is given by

$$d_\infty(X_1, X_2) = \max(|8-4|, |2-7|) = \max(4, 5) = 5 \text{ km}$$

Example 1.16. In Northwestern Tanzania, 20 borehole soil samples (Table 1.2) taken at constant depth of 0–10 cm revealed the following soil composition. Depicting $X_3$ and $X_4$, say, as $n = 20$ points in a two-dimensional vector space, we obtain the so-called scatter diagram, as in Figure

1.11. The mean vector is then

$$\bar{X} = (77.77, 0.0549)$$

Note that $\bar{X}$ does not lie in the center of the clustered scatter of points owing to the extreme influence of the isolated point $o_3 = (53, 0.274)$. In what follows we will rescale the values of $X_4$ by multiplying by 100. The rescaled means are then $\bar{X}^ = (77.77, 5.49)$.*

Example 1.17. From the data of Example 1.16, we have the vector magnitudes (norms)

$$|| X_3 || = 350 \text{ and } || X_4 || = 30.5$$

and the inner product measures

$$X_3 \cdot X_4 = 428.5 \text{ and } X_3 \cdot X_4 = 4285$$

Then

$$\cos \theta = \frac{4285}{350(30.5)} = 0.40$$

so that $X_3$ and $X_4$ contain an angle of $\theta = 46.85^\circ$ in $n = 20$ dimensional measurement (sample) space. Due to the extreme influence of $o_3$ (Figure 1.11), $\cos \theta$ is positive, whereas the relationship between the two vectors is in fact negative. Finally, the squared distance between $X_3$ and $X_4$ is given from Equation (1.31) as

$$d_2^2(X_3, X_4) = 350^2 + 30.5^2 - 2(4285) = 122,500 + 930 - 8570 = 114,860$$

Example 1.18. Referring to Examples 1.16 and 1.17, we have

$$s_3 = 6.44 \quad s_4 = 6.55 \quad \text{and} \quad \text{cov}(X_3, X_4) = 0.48$$

using well-known computing formulas for the variance and covariance (see Exercise 10). The correlation coefficient (1.38) is therefore given by

$$r_{12} = \frac{0.48}{6.44 \times 6.55} = 0.011$$

so that apparently clay and calcium content are unrelated (orthogonal). The zero correlation, however, is due almost entirely to the outlier point $o_3 = (53.3, 27.4)$. Once $o_3$ is removed, we have $\bar{x}_3 = 79.2$, $\bar{x}_4 = 4.0$, $||X_3||^2 = 11,307.0$, $||X_4||^2 = 1402.2$, and $X_3 \cdot X_4 = 2315.5$, so that the new correlation coefficient is

$$r_{12} = -0.76$$

---

## Chapter 2: Vector Spaces

### Definitions

**Definition 2.1.** Any set of vectors that is closed under vector addition and scalar multiplication is known as a vector space.

**Definition 2.2.** Let $X_1, X_2, \dots, X_k$ represent a generating system of a Euclidean vector space. If a subset of $1 \leq r \leq k$ vectors in the generating system is linearly independent, then it is known as a basis of $E(r)$.

**Definition 2.3.** The dimension of a vector space $E(k)$ is equal to the maximum number of linearly independent vectors in $E(k)$.

**Definition 2.4.** Consider two vector spaces $S$ and $T$ such that all vectors contained in $S$ are also contained in $T$, but not all vectors of $T$ are necessarily contained in $S$. Then $S$ is said to be a proper subspace of $T$, written $S \subset T$. More generally, $S$ is a subspace of $T$ when $S \subseteq T$; that is, both $S$ and $T$ may contain identical vectors.

**Definition 2.5.** Let $S$ and $T$ denote any two vector spaces. Then the following applies:

1. The vector space consisting of all vectors common to both $S$ and $T$ is called the intersection of $S$ and $T$, written $S \cap T$.
    
2. The vector space consisting of all vectors $X_1 + X_2$, where $X_1$ lies in $S$ ($X_1 \in S$) and $X_2$ lies in $T$ ($X_2 \in T$), is called the sum or the union of $S$ and $T$, written $S \cup T$.
    

**Definition 2.6.** The vector spaces $S$ and $T$ are said to be mutually orthogonal if every vector of $S$ is orthogonal to every vector in $T$.

**Definition 2.7.** Let $S$ be a subspace of $E(n)$. Then the set of all vectors in $E(n)$ that are perpendicular to $S$ is known as the orthogonal complement of $S$, denoted as $S^\perp$.

Definition 2.8. Let $S$ be a Euclidean vector space, $T$ a subspace of $S$, and $Y$ any vector in $S$. Then if there exists a vector $\hat{Y} \in T$ such that

$$|| Y - \hat{Y} || \leq || Y - Z ||$$

for any other vector $Z \in T$, then vector $\hat{Y}$ is said to be the minimizing vector (of the distance) between $Y$ and $T$.

---

### Theorems

Theorem 2.1. If the $n$-dimensional vectors $X_1, X_2, \dots, X_k$ form a basis of $E(k)$ ($n \geq k$), then every vector $Y$ of $E(k)$ is expressed uniquely as the linear combination

$$Y = a_1X_1 + a_2X_2 + \dots +a_kX_k$$

PROOF: Assume there exists another set of coefficients $b_1, b_2, \dots, b_k$ such that

$$Y = b_1X_1 + b_2X_2 + \dots +b_kX_k$$

Subtracting the two linear combinations then yields

$$(a_1 - b_1)X_1 + (a_2 - b_2)X_2 + \dots + (a_k - b_k)X_k = 0$$

and since $X_1, X_2, \dots, X_k$ are linearly independent, by Definition 1.5 we have

$$(a_1 - b_1)=(a_2 - b_2)= \dots =(a_k - b_k)=0$$

so that $a_1 = b_1, a_2 = b_2, \dots, a_k = b_k$. The coefficients are therefore unique and the linear combination $Y$ is uniquely determined once the basis vectors $X_i$ ($i = 1,2, \dots, k$) are given. $\square$

Theorem 2.2. Let $X_1, X_2, \dots, X_k$ be nonzero $n$-dimensional vectors ($k \leq n$).

i. If there exists a subset of $r \leq k$ vectors $X_1, X_2, \dots, X_r$ that are linearly dependent, then the entire set of $k$ vectors is linearly dependent.

ii. If the $k$ vectors $X_1, X_2, \dots, X_k$ are linearly independent, then any subset of $r \leq k$ vectors is linearly independent.

iii. A set of vectors $X_1, X_2, \dots, X_k$ is linearly dependent if and only if any one of the vectors $X_i$ is a linear combination of the remaining $k- 1$ vectors (see Section 1.5).

iv. Let $Y= a_1X_1 + a_2X_2 + \dots + a_kX_k$ so that $Y$ is linearly dependent on $X_1, X_2, \dots, X_k$. Then if any vector $X_i$ ($i=1,2, \dots, k$), say, $X_k$, is linearly dependent on the remaining $X_1, X_2, \dots, X_{k-1}$, then $Y$ is linearly dependent on $X_1, X_2, \dots, X_{k-1}$.

**Theorem 2.3 (The Completing Theorem).** Let $E(n)$ be a $n$-dimensional Euclidean vector space and let $X_1, X_2, \dots, X_k$ be any $k \leq n$ nonzero linearly independent vectors of $E(n)$. Then there exist $r = n - k$ linearly independent vectors $X_{k+1}, X_{k+2}, \dots X_n$, which together with $X_1, X_2, \dots, X_k$ form a basis of $E(n)$.

Theorem 2.4. Let $S$ and $T$ be any two vector spaces such that $\text{dim}(S) = s$, $\text{dim}(T) = t$, $\text{dim}(S \cap T) = m$, and $\text{dim}(S \cup T) = r$. Then

$$\text{dim}(S \cup T) = \text{dim}(S) + \text{dim}(T) - \text{dim}(S \cap T)$$

**Theorem 2.5.** Let $X_1, X_2, \dots, X_r$ be any $r$ vectors in $S$. If another vector $Y$ is orthogonal to the $r$ vectors, then it is orthogonal to every vector that lies in the space generated by $X_1, X_2, \dots, X_r$.

Theorem 2.6. If $E(n)$ is a $n$-dimensional vector space and $E(r)$

is a subspace of dimension $r$, then $E(n)$ contains a nonzero vector $Y$ that is orthogonal to $E(r)$.

**Theorem 2.7.** Every vector space $E(n)$ contains exactly $n$ mutually orthogonal vectors.

**Theorem 2.8.** Let $S$ be a vector space and $T$ any subspace of $S$. Then the direct sum $T \oplus T^\perp = S$ where $T^\perp$ is the orthogonal complement of $T \subset S$.

**Theorem 2.9 (Orthogonal Projection Theorem).** Let $S$ be a vector space, $T$ a subspace of $S$, and $Y$ any vector in $S$. Then a vector $\hat{Y} \in T$ is a minimizing vector if and only if $e = Y - \hat{Y}$ is orthogonal to $T$.

---

### Examples

Example 2.1. The following provide examples of vector spaces.

i. The (infinite) set of all $n$-component vectors $(x_1, x_2, \dots, x_n)$, since the vector sums and scalar product defined for a $n$-component vector is again a $n$-component vector.

ii. The zero vector $0 = (0, 0, \dots, 0)$ forms, on its own, a vector space, since the sum of two zero vectors and the scalar product of a zero vector again yield a zero vector, that is, $0+0 = 0$ and $k0 = 0$ for any scalar $k$.

Example 2.2. Consider Figure 2.2, where $\text{dim}(S) = 2$, $\text{dim}(T) = 2$, and $\text{dim}(S \cap T) = 1$, since the two orthogonal planes intersect in a straight line. By Theorem 2.4, we have

$$\text{dim}(S \cup T) = 2 + 2 - 1 = 3$$

so that $Z = (z_1, z_2, z_3)$ is in $S \cup T$.

Example 2.3. Find the orthogonal projection of $Y = (2,7,1)$ onto the vector $X = (5,6,4)$.

SOLUTION: Let $\hat{Y}$ be the projection vector. The magnitude of $\hat{Y}$ is

$$||\hat{Y}|| = || X || \cos \theta = \frac{X \cdot Y}{|| X ||}$$

with direction given by the unit vector

$$\frac{X}{|| X ||}$$

Then

$$X \cdot Y = 10 + 42 + 4 = 56 \quad \text{and} \quad || X || = (25 + 36 + 16)^{1/2} = \sqrt{77} \approx 8.775$$

and

$$|| \hat{Y} || = \frac{56}{8.775} = 6.38$$

so that $\hat{Y}$ can be expressed as

$$\hat{Y} = 0.73X$$

Example 2.4. Find the orthogonal projection of $Y = (7,7,8)$ onto the plane spanned by $X_1 = (5,12,1)$ and $X_2 = (9,5,1)$.

SOLUTION: The orthogonal projection is illustrated in Figure 2.7. Since $\hat{Y}$ must lie in the plane spanned by $X_1$ and $X_2$, we have

$$\hat{Y} = \beta_1X_1 + \beta_2X_2$$

where coefficients $\beta_1$ and $\beta_2$ are to be determined. Then

$$Y = \beta_1X_1 + \beta_2X_2 + e$$

and forming inner products with $X_1$ and $X_2$, we have the equations

$$Y \cdot X_1 = \beta_1X_1 \cdot X_1 + \beta_2X_2 \cdot X_1$$

$$Y \cdot X_2 = \beta_1X_1 \cdot X_2 + \beta_2X_2 \cdot X_2$$

where $X_1 \cdot e = X_2 \cdot e = 0$. To obtain $\hat{Y}$ we solve for $\beta_1$ and $\beta_2$. Since $Y \cdot X_1 = 127, Y \cdot X_2 = 106, X_1 \cdot X_1 =170, X_2 \cdot X_2 =107$, and $X_1 \cdot X_2 = X_2 \cdot X_1 =106$, we have

$$127 = 170\beta_1 + 106\beta_2$$

$$106 = 106\beta_1 + 107\beta_2$$

and $\beta_1 = 0.339, \beta_2= 0.655$. The projection vector is therefore given by

$$\hat{Y} = 0.339(5, 12, 1) + 0.655(9, 5, 1)$$

where

$$\hat{Y} = (7.58, 7.358, 0.994)$$

Example 2.6. Let $V = (4,5)$ be given with respect to the orthonormal basis $E_1 = (1,0), E_2 = (0,1)$. Find the coordinates of $V$ for the following:

i. Axes rotated clockwise through $\theta = 20^\circ$. ii. With respect to the oblique system $F_1 = (1,3)$ and $F_2 = (4,1)$.

SOLUTION: i. Let $V^ = ( x^, y^ )$ be the coordinates with respect to the rotated*

orthogonal system. Since $\cos 20^\circ = 0.9397$ and $\sin 20^\circ = 0.3420$, we have from Equation (2.31)

$$x^* = (0.9397)(4) - (0.3420)(5) = 2.0388$$

$$y^* = (0.3420)(4) + (0.9397)(5) = 6.0565$$

with respect to the new (orthogonal) coordinated system. Alternatively, the rotation can be viewed as an anticlockwise shift of $V = (4,5)$ through an angle $\theta = 20^\circ$.

ii. From Equation (2.37) we have

$$4 = 1x^* + 4y^*$$

$$5 = 3x^* + 1y^*$$

or

$$3x^* + y^* = 5$$

$$x^* + 4y^* = 4$$

so that $x^ = 16/11$ and $y^* = 7/11$ are the new coordinates of $V$ with respect to the oblique basis $F_1 = (1,3), F_2 = (4,1)$.*

Example 2.7. Find the equation of the circle $x^2 + y^2 = r^2$

relative to the oblique coordinate axes that form angles $\alpha$ and $\beta$ with the orthonormal basis $E_1, E_2$.

SOLUTION: Let $V = (x,y)$ be any point on the circle. The equation of the circle with respect to $E_1$ and $E_2$ is given by the inner product

$$V \cdot V = r^2$$

With respect to oblique axes $F_1$ and $F_2$, vector $V$ is given by $V = x^*F_1 + y^*F_2$, so that

$$r^2 = (x^*F_1 + y^*F_2) \cdot (x^*F_1 + y^*F_2) = x^{*2}F_1 \cdot F_1 + y^{*2}F_2 \cdot F_2 + 2x^*y^*F_1 \cdot F_2$$

where without loss of generality we assume that $F_1$ and $F_2$ are of unit length. Since

$$F_1 \cdot F_2 = || F_1 || || F_2 || \cos(\beta - \alpha)$$

we have

$$r^2 = x^{*2} + y^{*2} + 2x^*y^*\cos(\beta - \alpha)$$

as the equation of the circle with respect to $F_1$ and $F_2$.