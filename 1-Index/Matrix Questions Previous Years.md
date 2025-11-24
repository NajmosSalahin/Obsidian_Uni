**1.** What do you mean by a Symmetric matrix? Explain with an example. Prove that the products of symmetric matrices are not generally symmetric by an example.

**2.** Define (i) idempotent matrix, (ii) nilpotent matrix, (iii) unipotent matrix, (iv) orthogonal matrix, (v) Norm of the vector, and (vi) orthogonal vector. Show that $A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \\ -1 & -2 & -3 \end{bmatrix}$ is a nilpotent matrix.

**3.** Write a Helmert matrix (H) of order 4 and show that it is an orthogonal matrix. Also, verify that, $A = \frac{1}{\sqrt{6}}\begin{bmatrix} \sqrt{2} & \sqrt{2} & \sqrt{2} \\ \sqrt{3} & -\sqrt{3} & 0 \\ 1 & 1 & -2 \end{bmatrix}$ is orthogonal matrix.

**4.** Prove that the determinants of the transpose of matrix equals the determinants of the matrix itself for the matrix $B = \begin{bmatrix} 1 & -1 & 0 \\ 2 & 7 & 2 \\ 4 & 4 & 9 \end{bmatrix}$. Also show that if the two rows of a matrix are the same, then the determinant of the matrix is zero. 

**5.** Show that

$$\begin{vmatrix} a+b+c & a+b & a & a \\ a+b & a+b+c & a & a \\ a & a & a+b+c & a+b \\ a & a & a+b & a+b+c \end{vmatrix} = c^2(4a+2b+c)(2b+c)$$

6. Let $A = \begin{bmatrix} 6 & -1 & 4 \\ 2 & 5 & -3 \\ 1 & 1 & 2 \end{bmatrix}$.

(a) Calculate the transpose of $A^{-1}$ and the inverse of $A'$ and

(b) Calculate the inverse of $A^{-1}$. 

**7.** Write down the properties of the inverse of a matrix.


**1.** Explain the difference between linear combination and linear transformation of vectors along with example.
**2.** For $\mathbf{x}_1 = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}, \mathbf{x}_2 = \begin{bmatrix} -1 \\ 3 \\ 2 \end{bmatrix}, \mathbf{x}_3 = \begin{bmatrix} -13 \\ -1 \\ 2 \end{bmatrix}$ and $\mathbf{x}_4 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$, show the following.

(a) $\mathbf{x}_1, \mathbf{x}_2$ and $\mathbf{x}_3$ are linearly dependent, and find a linear relationship among them.

(b) $\mathbf{x}_1, \mathbf{x}_2$ and $\mathbf{x}_4$ are LIN, and find the linear combination of them that equals $[a \quad b \quad c]'$.

**3.** Define the rank of a matrix. Write down the important properties of rank.

**4.** Show that, the number of LIN rows in a matrix is the same as the number of LIN columns.

**5.** Define generalized inverse. What are the benefits of generalized inverse matrix. Also, describe the general procedure to find generalized inverse.

**6.** When $\mathbf{G}$ is a generalized inverse of $\mathbf{X}'\mathbf{X}$ :

(i) $\mathbf{G}'$ is also a generalized inverse of $\mathbf{X}'\mathbf{X}$.

(ii) $\mathbf{XGX}'\mathbf{X} = \mathbf{X}$; i.e., $\mathbf{GX}'$ is a generalized inverse of $\mathbf{X}$.

(iii) $\mathbf{XGX}'$ is invariant to $\mathbf{G}$.

(iv) $\mathbf{XGX}'$ is symmetric, whether $\mathbf{G}$ is or not.

**7.** Define characteristic equation, characteristic roots and characteristic vectors. Show that, the sum of the eigenvalues of a matrix equals its trace, and their product equals its determinant.

**8.** Let $B$ be an $n \times n$ matrix. Prove that, the solutions to $Bx = 0$ can always be found that are orthogonal to one another.

#### Semester

**1.**

- **(a)** Define matrix. Explain with an example. Show that the product of a matrix and its transpose is symmetric. 
  
- **(b)** Explain with examples: Square matrix, null matrix, identity/unit matrix, diagonal matrix, scalar matrix, skew-symmetric matrix, Hadamard product, Kronecker sum and products.
  
- **(c)** Define norm of a real vector. Find the norm of the vector $x' = [4 \quad 3 \quad 1 \quad -2]$. Is it a unit vector? If not find the normalized form of $x$. Also, define orthogonal and orthonormal vectors.
   

**2.**

- **(a)** Define the (i) Vectors Inner Product, (ii) Length of a vector, (iii) Distance of two vectors, and (iv) Mutually Orthogonal vectors. 
   
- **(b)** Prove that (i) The inner product is distributive over addition and subtraction, and (ii) The inner product is commutative. 
  
- **(c)** Let $X_1 = (1, 3, -4)$ and $X_2 = (2, 4, 0)$. Verify directly that $X_1 \cdot X_2 = X_2 \cdot X_1$ and find the magnitudes of $X_1$ and $X_2$. What is the distance between the two vectors?
   

**3.**

- **(a)** What do you mean by minors and cofactors of a matrix determinant? Notationally show the difference between the two. Explain n-order determinants using minors. 
  
- **(b)** Prove that $|A'| = |A|$ for $A = \begin{bmatrix} 1 & -1 & 0 \\ 2 & 1 & 2 \\ 4 & 4 & 9 \end{bmatrix}$. What happens to the determinant when (i) two rows of a matrix are the same and (ii) every element of a particular row is zero?
  
- **(c)** Define triangular form of a matrix. Find the determinant of the matrix $C = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 4 \\ 3 & 2 & 1 \end{bmatrix}$ reducing it to a triangular form. 

**4.**

- **(a)** Define the inverse of a matrix. Find the inverse of the matrix $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{bmatrix}$ by deriving the cofactors of it. What is the adjoint matrix of $A$?
    
- **(b)** What are the conditions for the existence of the inverse of a matrix? If such conditions are satisfied, prove that, (i) $|A^{-1}| = \frac{1}{|A|}$, (ii) $(A')^{-1} = (A^{-1})'$, and (iii) $(AB)^{-1} = B^{-1}A^{-1}$.
    
- **(c)** What are the inverses of the matrices which have the form: (i) A matrix of order 2, (ii) Diagonal matrices, (iii) $I, J,$ and $(aI_n + bJ_n)$ where $I$ is an identity matrix and $J$ is a matrix of 1's, and (iv) Orthogonal matrices.
    

**5.**

- **(a)** Explain the difference between linear combination and linear transformation of vectors along with example.
    
- **(b)** For $\mathbf{x}_1 = \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}, \mathbf{x}_2 = \begin{bmatrix} -1 \\ 3 \\ 2 \end{bmatrix}, \mathbf{x}_3 = \begin{bmatrix} -13 \\ -1 \\ 2 \end{bmatrix}$ and $\mathbf{x}_4 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$, show the following.
 
    - (i) $\mathbf{x}_1, \mathbf{x}_2$ and $\mathbf{x}_3$ are linearly dependent, and find a linear relationship among them.
   
    - (ii) $\mathbf{x}_1, \mathbf{x}_2$ and $\mathbf{x}_4$ are LIN, and find the linear combination of them that equals $[a \quad b \quad c]'$.
 
- **(c)** Show that, the number of LIN rows in a matrix is the same as the number of LIN columns. 


