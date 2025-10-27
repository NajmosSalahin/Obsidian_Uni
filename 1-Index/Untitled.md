Here are the corrected definitions, proofs, and examples.

## 1. Define the terms along with examples: (i) Matrix, (ii) Square Matrix, (iii) Diagonal Matrix, (iv) Triangular Matrix

(i) Matrix

Not found in PDF. A matrix is a rectangular array of numbers arranged in rows and columns. For example, the $2 \times 3$ matrix is:

$$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$

(ii) Square Matrix

Not found in PDF. A square matrix is a matrix with an equal number of rows and columns. For example, the $2 \times 2$ square matrix is:

$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$

(iii) Diagonal Matrix

From page 152: One of the simplest and most commonly occurring matrices is the diagonal matrix. Generally speaking, a square $n \times n$ matrix $A = (a_{ij})$ is said to be in diagonal form when all the elements consist of zeros, except those lying on the main diagonal. We then have $a_{ij} = 0$ for $i \neq j$, for $i, j = 1, 2, ..., n$. Thus a diagonal matrix has the general form (3.4).

Example:

$$\begin{pmatrix} 5 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

(iv) Triangular Matrix

From page 154: A square matrix of the form (3.8) is known as a lower triangular matrix. When the nonzero elements are located above the main diagonal, $A$ is known as an upper triangular matrix. When neither form is specified, we say that $A$ is triangular.

Example (lower triangular):

$$\begin{pmatrix} 1 & 0 & 0 \\ 2 & 3 & 0 \\ 4 & 5 & 6 \end{pmatrix}$$

---

## 2. Define the (i) Vectors Inner Product, (ii) Length of a vector, (iii) Distance of two vectors, and (iv) Mutually Orthogonal vectors

(i) Vectors Inner Product

From page 30: As illustrated by Equation (1.6), the inner product $X_1 \cdot X_2$ is given by the sum of the products of the vector components. More generally we have the following definition. Definition 1.3. Let $X_1 = (x_{11}, x_{12}, ..., x_{1n})$ and $X_2 = (x_{21}, x_{22}, ..., x_{2n})$ be any two $n$-dimensional (finite) vectors. Then the inner product of $X_1$ and $X_2$ is the real-valued scalar (1.7).

Example: For $X_1 = (1, 2)$ and $X_2 = (3, 4)$, $X_1 \cdot X_2 = 1 \cdot 3 + 2 \cdot 4 = 11$.

(ii) Length of a vector

Not found in PDF. The length (or norm) of a vector $X = (x_1, x_2, ..., x_n)$ is $||X|| = \sqrt{X \cdot X} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$.

Example: For $X = (3, 4)$, $||X|| = \sqrt{9 + 16} = 5$.

(iii) Distance of two vectors

Not found in PDF. The distance between two vectors $X_1$ and $X_2$ is $||X_1 - X_2|| = \sqrt{(X_1 - X_2) \cdot (X_1 - X_2)}$.

Example: For $X_1 = (1, 2)$ and $X_2 = (3, 4)$, distance = $\sqrt{(1-3)^2 + (2-4)^2} = \sqrt{8} = 2\sqrt{2}$.

(iv) Mutually Orthogonal vectors

Not found in PDF. Vectors $X_1, X_2, ..., X_k$ are mutually orthogonal if $X_i \cdot X_j = 0$ for all $i \neq j$.

Example: $(1, 0)$ and $(0, 1)$ are mutually orthogonal since $1 \cdot 0 + 0 \cdot 1 = 0$.

---

## 3. Prove that (i) The inner product is distributive over addition and subtraction, and (ii) The inner product is commutative

(i) The inner product is distributive over addition and subtraction

From page 32: PROOF: We have, for addition, $X_1 \cdot (X_2 + X_3) = X_1 \cdot X_2 + X_1 \cdot X_3$. A similar result holds for subtraction. $\Box$

(ii) The inner product is commutative

From page 32: Theorem 1.3. The inner product is commutative, that is, $X_1 \cdot X_2 = X_2 \cdot X_1$.

PROOF: The proof consists in noting that any $i$-th element $x_{1i}x_{2i}$ of $X_1 \cdot X_2$ can also be written as $x_{2i}x_{1i}$, which is the $i$-th element of $X_2 \cdot X_1$. $\Box$

---

## 4. Show that, any n-dimensional vector can be standardized to unit length

From page 41: PROOF: Let $Y = (y_1, y_2, ..., y_n)$ be any $n$-dimensional vector with length $||Y||$. Let $Y^* = Y / ||Y||$. Then $Y^*$ is a unit vector, since $||Y^*|| = ||Y|| / ||Y|| = 1$. $\Box$

---

## 5. Let X1 = (1, 3, -4) and X2 = (2, 4, 0). Verify directly that X1 · X2 = X2 · X1 and find the magnitudes of X1 and X2. What is the distance between the two vectors?

Not found in PDF.

$X_1 \cdot X_2 = 1 \cdot 2 + 3 \cdot 4 + (-4) \cdot 0 = 2 + 12 + 0 = 14$.

$X_2 \cdot X_1 = 2 \cdot 1 + 4 \cdot 3 + 0 \cdot (-4) = 2 + 12 + 0 = 14$.

Thus, $X_1 \cdot X_2 = X_2 \cdot X_1$.

Magnitude of $X_1$: $||X_1|| = \sqrt{1^2 + 3^2 + (-4)^2} = \sqrt{1 + 9 + 16} = \sqrt{26}$.

Magnitude of $X_2$: $||X_2|| = \sqrt{2^2 + 4^2 + 0^2} = \sqrt{4 + 16 + 0} = \sqrt{20} = 2\sqrt{5}$.

Distance between $X_1$ and $X_2$: $||X_1 - X_2|| = \sqrt{(1-2)^2 + (3-4)^2 + (-4-0)^2} = \sqrt{1 + 1 + 16} = \sqrt{18} = 3\sqrt{2}$.

---

## 6. Explain linear dependence and independence of vectors. Prove that the vector Y = (11, 16, 21) is linearly dependent on vectors X1 = (1, 2, 3) and X2 = (4, 5, 6)

Not found in PDF.

**Linear independence:** Vectors $X_1, X_2, ..., X_k$ are linearly independent if the only solution to $c_1 X_1 + c_2 X_2 + ... + c_k X_k = 0$ (the zero vector) is $c_1 = c_2 = ... = c_k = 0$.

**Linear dependence:** If there exists a set of scalars $c_1, c_2, ..., c_k$, not all zero, such that $c_1 X_1 + c_2 X_2 + ... + c_k X_k = 0$, then the vectors are linearly dependent.

Proof of dependence:

To prove $Y = (11, 16, 21)$ is linearly dependent on $X_1 = (1, 2, 3)$ and $X_2 = (4, 5, 6)$, we need to find scalars $c_1$ and $c_2$ (not both zero) such that $c_1 X_1 + c_2 X_2 = Y$.

This gives the system of linear equations:

1. $c_1 + 4c_2 = 11$
    
2. $2c_1 + 5c_2 = 16$
    
3. $3c_1 + 6c_2 = 21$
    

Solving the first two equations:

Multiply equation (1) by 2: $2c_1 + 8c_2 = 22$.

Subtract equation (2) from this: $(2c_1 + 8c_2) - (2c_1 + 5c_2) = 22 - 16 \Rightarrow 3c_2 = 6 \Rightarrow c_2 = 2$.

Substitute $c_2 = 2$ back into equation (1): $c_1 + 4(2) = 11 \Rightarrow c_1 + 8 = 11 \Rightarrow c_1 = 3$.

Check this solution with equation (3): $3(3) + 6(2) = 9 + 12 = 21$. The solution holds.

Thus, $Y = 3X_1 + 2X_2$. Since we found non-zero scalars $c_1 = 3$ and $c_2 = 2$, $Y$ is linearly dependent on $X_1$ and $X_2$.