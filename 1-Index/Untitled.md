### 1. Define the terms along with examples: (i) Matrix, (ii) Square Matrix, (iii) Diagonal Matrix, (iv) Triangular Matrix

(i) **Matrix**  
Not found in PDF. A matrix is a rectangular array of numbers arranged in rows and columns. For example, the 2×3 matrix is:  
\[
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}
\]

(ii) **Square Matrix**  
Not found in PDF. A square matrix is a matrix with an equal number of rows and columns. For example, the 2×2 square matrix is:  
\[
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\]

(iii) **Diagonal Matrix**  
From page 152: One of the simplest and most commonly occurring matrices is the diagonal matrix. Generally speaking, a square n × n matrix A = (aij) is said to be in diagonal form when all the elements consist of zeros, except those lying on the main diagonal. We then have for i, j = 1,2,...,n. Thus a diagonal matrix has the general form (3.4).  
Example:  
\[
\begin{pmatrix}
5 & 0 & 0 \\
0 & -2 & 0 \\
0 & 0 & 3
\end{pmatrix}
\]

(iv) **Triangular Matrix**  
From page 154: A square matrix of the form (3.8) is known as a lower triangular matrix. When the nonzero elements are located above the main diagonal, A is known as an upper triangular matrix. When neither form is specified, we say that A is triangular.  
Example (lower triangular):  
\[
\begin{pmatrix}
1 & 0 & 0 \\
2 & 3 & 0 \\
4 & 5 & 6
\end{pmatrix}
\]

### 2. Define the (i) Vectors Inner Product, (ii) Length of a vector, (iii) Distance of two vectors, and (iv) Mutually Orthogonal vectors

(i) **Vectors Inner Product**  
From page 30: As illustrated by Equation (1.6), the inner product X1 ∙X2 is given by the sum of the products of the vector components. More generally we have the following definition. Definition 1.3. Let X1 = (x11, x12,..., x1n) and X2 = (x21, x22,...,x2n) be any two n-dimensional (finite) vectors. Then the inner product of X1 and X2 is the real-valued scalar (1.7).  
Example: For X1 = (1, 2) and X2 = (3, 4), X1 ∙ X2 = 1·3 + 2·4 = 11.

(ii) **Length of a vector**  
Not found in PDF. The length (or norm) of a vector X = (x1, x2, ..., xn) is ||X|| = \sqrt{X \cdot X} = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}.  
Example: For X = (3, 4), ||X|| = \sqrt{9 + 16} = 5.

(iii) **Distance of two vectors**  
Not found in PDF. The distance between two vectors X1 and X2 is ||X1 - X2|| = \sqrt{(X1 - X2) \cdot (X1 - X2)}.  
Example: For X1 = (1, 2) and X2 = (3, 4), distance = \sqrt{(1-3)^2 + (2-4)^2} = \sqrt{8} = 2\sqrt{2}.

(iv) **Mutually Orthogonal vectors**  
Not found in PDF. Vectors X1, X2, ..., Xk are mutually orthogonal if X_i \cdot X_j = 0 for all i \neq j.  
Example: (1, 0) and (0, 1) are mutually orthogonal since 1·0 + 0·1 = 0.

### 3. Prove that (i) The inner product is distributive over addition and subtraction, and (ii) The inner product is commutative

(i) **The inner product is distributive over addition and subtraction**  
From page 32: PROOF: We have, for addition, X1 · (X2 + X3) = X1 · X2 + X1 · X3. A similar result holds for subtraction. □

(ii) **The inner product is commutative**  
From page 32: Theorem 1.3. The inner product is commutative, that is, X1 ∙X2 = X2 ∙X1.  
PROOF: The proof consists in noting that any ith element x1ix2i of X1 ∙X2 can also be written as x2ix1i, which is the ith element of X2 ∙X1. □

### 4. Show that, any n-dimensional vector can be standardized to unit length

From page 41: PROOF: Let Y = (y1, y2,...,yn) be any n-dimensional vector with length || Y ||. Let Y* = Y / || Y ||. Then Y* is a unit vector, since || Y* || = || Y || / || Y || = 1. □

### 5. Let X1 = (1,3, -4) and X2 = (2,4,0). Verify directly that X1 · X2 = X2 · X1 and find the magnitudes of X1 and X2. What is the distance between the two vectors?

Not found in PDF.  
X1 · X2 = 1·2 + 3·4 + (-4)·0 = 2 + 12 + 0 = 14.  
X2 · X1 = 2·1 + 4·3 + 0·(-4) = 2 + 12 + 0 = 14. Thus, X1 · X2 = X2 · X1.  
Magnitude of X1: ||X1|| = \sqrt{1^2 + 3^2 + (-4)^2} = \sqrt{1 + 9 + 16} = \sqrt{26}.  
Magnitude of X2: ||X2|| = \sqrt{2^2 + 4^2 + 0^2} = \sqrt{4 + 16 + 0} = \sqrt{20} = 2\sqrt{5}.  
Distance between X1 and X2: ||X1 - X2|| = \sqrt{(1-2)^2 + (3-4)^2 + (-4-0)^2} = \sqrt{1 + 1 + 16} = \sqrt{18} = 3\sqrt{2}.

### 6. Explain linear dependence and independence of vectors. Prove that the vector Y = (11,16,21) is linearly dependent on vectors X1 = (1,2,3) and X2 = (4,5,6)

Not found in PDF.  
Linear independence: Vectors X1, X2, ..., Xk are linearly independent if the only solution to c1 X1 + c2 X2 + ... + ck Xk = 0 is c1 = c2 = ... = ck = 0. Otherwise, they are linearly dependent.  
To prove Y is linearly dependent on X1 and X2: Solve c1 X1 + c2 X2 = Y.  
This gives the system:  
c1 + 4c2 = 11  
2c1 + 5c2 = 16  
3c1 + 6c2 = 21  
Solving the first two equations: Multiply first by 2: 2c1 + 8c2 = 22. Subtract second: (2c1 + 8c2) - (2c1 + 5c2) = 22 - 16 ⇒ 3c2 = 6 ⇒ c2 = 2. Then c1 + 4·2 = 11 ⇒ c1 + 8 = 11 ⇒ c1 = 3. Check third: 3·3 + 6·2 = 9 + 12 = 21, which holds. Thus, Y = 3 X1 + 2 X2, so Y is linearly dependent on X1 and X2.